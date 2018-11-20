from kafka import KafkaProducer
from datetime import datetime
import json
import time
import sys

messages = [
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"DV01:A045,DV02:A104,DV03:A049,DV04:A066,DV05:A007,DV06:A027,DV07:A001,DV08:A042,DV09:A074,DV10:A062,DV11:A044,DV12:A092,DV13:A111,DV14:A087,DV15:A047,DV16:A069,DV17:A060,DV18:A075,DV19:A093,DV20:A072,DV21:A011,DV22:A083,DV23:A022,DV24:A088,DV25:A086,DA41:A023,DA42:A008,DA43:A058,DA44:A016,DA45:A134,DA46:A096,DA47:A035,DA48:A070,DA49:A024,DA50:A105,DA51:A101,DA52:A082,DA53:A033,DA54:A073,DA55:A108,DA56:A091,DA57:A089,DA58:A090,DA59:A076,DA60:A043,DA61:A094,DA62:A135,DA63:A085,DA64:A015,DA65:A068,CM01:N602,CM02:J502,CM03:J503,CM04:N605,CM05:J506,CM06:N606,CM07:N601,CM08:J505,CM09:N603,CM10:J501,CM11:N604,CM12:J504,PM01:T703,PM02:T701,PM03:T702,PM04:T704\",\"id\":\"Array-AntennasToPads\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"ANTPAD\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#1!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#2!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#3!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#4!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#5!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#6!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#7!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#8!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#9!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:1,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#10!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#11!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#12!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#13!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#14!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#15!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#16!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#17!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#18!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#19!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#20!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:1,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#21!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:1,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#22!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:1,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#23!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#24!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#25!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#26!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#27!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#28!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#29!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#30!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#31!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#32!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#33!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#34!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#35!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#36!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#37!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#38!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:0,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#39!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:1,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#40!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#41!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#42!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#43!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#44!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#45!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#46!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#47!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#48!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#49!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:0,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#50!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#51!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#52!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#53!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#54!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#55!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#56!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#57!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#58!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#59!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#60!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#61!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:0,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#62!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:0,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#63!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:0,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#64!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:0,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#65!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\"",
    "\"sampleTime\":\"{}\",\"filteredTime\":\"{}\",\"value\":\"AC-POWER:0,AT-ZENITH:0,HVAC:0,FIRE:0,UPS-POWER:1,STOW-PIN:1,RX-CAB-TEMP:0,DRIVE-CAB-TEMP:1,ANTENNA-POS:0,E-STOP:0\",\"id\":\"Array-UMStatus-Ant[!#66!]\",\"operationalMode\":\"OPERATIONAL\",\"validity\":\"RELIABLE\",\"pluginID\":\"UtilityModules\",\"monitoredSystemID\":\"array\",\"producedByPluginTime\":\"{}\",\"publishTime\":\"{}\""
]

producer = KafkaProducer(bootstrap_servers=sys.argv[1])

while True:
    for message in messages:
        time_now = datetime.utcnow()
        time_now_formatted = time_now.strftime('%Y-%m-%dT%H:%M:%S.') + str(int(time_now.microsecond/1000)).zfill(3)
        print('message: ', message)
        data = "{" + message.format(time_now_formatted, time_now_formatted, time_now_formatted, time_now_formatted) + "}"
        print('data: ', data)
        producer.send('PluginsKTopic', data.encode())
    time.sleep(1)
