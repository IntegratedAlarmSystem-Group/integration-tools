from kafka import KafkaProducer
from datetime import datetime
import time
import sys

producer = KafkaProducer(bootstrap_servers=sys.argv[1])

message = "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"DV01:A045,DV02:A104,DV03:A049,DV04:A066,DV05:A007,DV06:A027,DV07:A001,DV08:A042,DV09:A074,DV10:A062,DV11:A044,DV12:A092,DV13:A111,DV14:A087,DV15:A047,DV16:A069,DV17:A060,DV18:A075,DV19:A093,DV20:A072,DV21:A011,DV22:A083,DV23:A022,DV24:A088,DV25:A086,DA41:A023,DA42:A008,DA43:A058,DA44:A016,DA45:A134,DA46:A096,DA47:A035,DA48:A070,DA49:A024,DA50:A105,DA51:A101,DA52:A082,DA53:A033,DA54:A073,DA55:A108,DA56:A091,DA57:A089,DA58:A090,DA59:A076,DA60:A043,DA61:A094,DA62:A135,DA63:A085,DA64:A015,DA65:A068,CM01:N602,CM02:J502,CM03:J503,CM04:N605,CM05:J506,CM06:N606,CM07:N601,CM08:J505,CM09:N603,CM10:J501,CM11:N604,CM12:J504,PM01:T703,PM02:T701,PM03:T702,PM04:T704\",\"id\":\"Array-AntennasToPads\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"ANTPAD\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\""

while True:
    time_now = datetime.utcnow()
    time_now_formatted = time_now.strftime('%Y-%m-%dT%H:%M:%S.') + str(int(time_now.microsecond/1000))
    data = "{" + message.format(time_now_formatted, time_now_formatted, time_now_formatted, time_now_formatted) + "}"
    producer.send('PluginsKTopic', data.encode())
    time.sleep(1)
