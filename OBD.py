import obd
from obd import ECU
import time

ports = obd.scan_serial()      # return list of valid USB or RF ports
print (ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
# connection = obd.OBD(ports[0]) # connect to the first port in the list

def RPMTest():
    connection = obd.Async(ports[0],delay_cmds=0.01, fast=True)
    connection.watch(obd.commands.RPM) # keep track of the RPM
    connection.start() # start the async update loop
    # print (connection.query(obd.commands.RPM)) # non-blocking, returns immediately
    # for x in range (1000):
    #     cmd = obd.commands[1][12]
    #     cmd.fast = True
    #     response = connection.query(cmd)
    #     print(response.value)

    for x in range (1000):
        print(connection.query(obd.commands.RPM))
        time.sleep(0.01)

def VINReadout():
    connection = obd.OBD(ports[0])
    cmd = obd.commands[9][2]
    response = connection.query(cmd)
    print(response.value)

print("Connection Successful!")
userChoice = input("1 for RPMTest, 2 for VIN Readout")
print(userChoice)

if userChoice == "1":
    RPMTest()
elif userChoice == "2":
    VINReadout()
else:
    print("very funny...")
