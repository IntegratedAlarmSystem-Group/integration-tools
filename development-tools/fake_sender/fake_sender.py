import os
import random
import sys
import tornado
import pprint
from clients import WSClient
from readers import CdbReader
from datetime import datetime

DEFAULT_HOST = 'localhost:8000'
DEFAULT_PASS = 'dev_pass'
DEFAULT_SEND_RATE = 500
DEFAULT_RECONNECTION_RATE = 1000  # One second to evaluate reconnection
VALUES = ['CLEARED', 'SET_LOW', 'SET_MEDIUM', 'SET_HIGH', 'SET_CRITICAL']
counter = 0


def get_websocket_url(kwargs):
    """
    Returns the url to send websocket messages

    Args:
        kwargs (dict): optional arguments passed to the command

    Returns:
        string: the url
    """

    if kwargs['host'] is not None:
        host = kwargs['host']

    if kwargs['password'] is not None:
        password = kwargs['password']

    if password and password != '':
        return 'ws://{}/core/?password={}'.format(host, password)
    else:
        return 'ws://{}/core/'.format(host)


def get_alarm_msg(id):
    time_now = datetime.utcnow()
    time_now_formatted = time_now.strftime('%Y-%m-%dT%H:%M:%S.') + \
        str(int(time_now.microsecond/1000)).zfill(3)

    value_num = random.randint(0, 4)

    value = VALUES[value_num]
    validity = 'RELIABLE'

    msg = {
        "value": value,
        "readFromMonSysTStamp": time_now_formatted,
        "productionTStamp": time_now_formatted,
        "sentToConverterTStamp": time_now_formatted,
        "receivedFromPluginTStamp": time_now_formatted,
        "convertedProductionTStamp": time_now_formatted,
        "sentToBsdbTStamp": time_now_formatted,
        "mode": "OPERATIONAL",
        "iasValidity": validity,
        "fullRunningId": "(ConverterID:CONVERTER)@({}:IASIO)".format(id),
        "valueType": "ALARM"
    }
    return msg


def main(**kwargs):
    """
    Sends alarms wiht random values for every Alarm ID in the CDB
    """
    url = get_websocket_url(kwargs)
    print('Going to send messages to: ', url)

    send_rate = int(kwargs['rate'])
    print('With rate: ', send_rate)
    reconnection_rate = DEFAULT_RECONNECTION_RATE

    print('\n Reading from cdb:', CdbReader.get_cdb_location())
    alarm_ids = CdbReader.get_alarm_ids()
    print('\n Number of alarms to send:', len(alarm_ids))

    # print('\n Alarm IDs:')
    # pprint.pprint(alarm_ids)

    # Open WS Connection
    ws_client = WSClient(url, kwargs)

    def send_alarm():
        """ Send an alarm, to be used in a tornado task """
        global counter

        if not ws_client.is_connected():
            return

        counter = counter + 1
        print('Sending batch ', counter)

        for id in alarm_ids:
            msg = get_alarm_msg(id)
            # print('\n Sending message:')
            # pprint.pprint(msg)
            ws_client.send_message(msg)

    def ws_reconnection():
        """ Reconnects if not connected, to be used in a tornado task """
        if not ws_client.is_connected():
            ws_client.reconnect()

    broadcast_task = tornado.ioloop.PeriodicCallback(
        send_alarm,
        send_rate
    )

    reconnection_task = tornado.ioloop.PeriodicCallback(
        ws_reconnection,
        reconnection_rate
    )
    tasks = [broadcast_task, reconnection_task]

    for task in tasks:
        task.start()

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = DEFAULT_HOST

    if len(sys.argv) > 2:
        rate = sys.argv[2]
    else:
        rate = DEFAULT_SEND_RATE
    password = os.getenv('WS_CONNECTION_PASS', DEFAULT_PASS)
    main(host=host, password=password, rate=rate, verbosity=1)
