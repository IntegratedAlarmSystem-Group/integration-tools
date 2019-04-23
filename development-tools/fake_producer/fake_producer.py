import random
import time
import sys
import pprint
from json import dumps
from kafka import KafkaProducer
from readers import CdbReader
from datetime import datetime

DEFAULT_HOST = 'localhost:9092'
DEFAULT_SEND_RATE = 500
DEFAULT_TOPIC = "BsdbCoreKTopic"
DEFAULT_RECONNECTION_RATE = 1000  # One second to evaluate reconnection
VALUES = ['CLEARED', 'SET_LOW', 'SET_MEDIUM', 'SET_HIGH', 'SET_CRITICAL']
MODES = [
    'STARTUP',
    'INITIALIZATION',
    'CLOSING',
    'SHUTTEDDOWN',
    'MAINTENANCE',
    'OPERATIONAL',
    'DEGRADED',
    'UNKNOWN',
    'MALFUNCTIONING',
]


def get_alarm_msg(id):
    time_now = datetime.utcnow()
    time_now_formatted = time_now.strftime('%Y-%m-%dT%H:%M:%S.') + \
        str(int(time_now.microsecond/1000)).zfill(3)

    # value_num = random.randint(0, 4)
    value_num = 0
    value = VALUES[value_num]

    # mode_num = random.randint(0, 8)
    mode_num = 5
    mode = MODES[mode_num]

    validity = 'RELIABLE'

    msg = {
        "value": value,
        "readFromMonSysTStamp": time_now_formatted,
        "productionTStamp": time_now_formatted,
        "sentToConverterTStamp": time_now_formatted,
        "receivedFromPluginTStamp": time_now_formatted,
        "convertedProductionTStamp": time_now_formatted,
        "sentToBsdbTStamp": time_now_formatted,
        "mode": mode,
        "iasValidity": validity,
        "fullRunningId": "(ConverterID:CONVERTER)@({}:IASIO)".format(id),
        "valueType": "ALARM"
    }
    return msg


def main(**kwargs):
    """
    Sends alarms for every Alarm ID in the CDB
    """
    host = kwargs['host']
    topic = DEFAULT_TOPIC
    print('Going to write messages to host {}, and topic {} '.format(host, topic))

    send_rate = int(kwargs['rate'])
    print('With rate: ', send_rate)
    reconnection_rate = DEFAULT_RECONNECTION_RATE / 1000

    print('\n Reading from cdb:', CdbReader.get_cdb_location())
    alarm_ids = CdbReader.get_alarm_ids()
    print('\n Number of alarms to send:', len(alarm_ids))

    # print('\n Alarm IDs:')
    # pprint.pprint(alarm_ids)

    counter = 0
    connection_pending = True
    while connection_pending:
        try:
            producer = KafkaProducer(
                bootstrap_servers=host,
                value_serializer=lambda x: dumps(x).encode('utf-8')
            )
            connection_pending = False
        except:
            print('Error connecting to kafka, trying again in 1 second')
            time.sleep(reconnection_rate)

    while True:
        print('Sending batch number ', counter)
        counter = counter + 1
        for id in alarm_ids:
            alarm_msg = get_alarm_msg(id)
            producer.send(topic, value=alarm_msg)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = DEFAULT_HOST

    if len(sys.argv) > 2:
        rate = sys.argv[2]
    else:
        rate = DEFAULT_SEND_RATE

    main(host=host, rate=rate, verbosity=1)
