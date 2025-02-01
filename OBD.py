import obd
from obd import ECU
import time

ports = obd.scan_serial()      # return list of valid USB or RF ports
print (ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
connection = obd.OBD(ports[0]) # connect to the first port in the list
