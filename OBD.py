import obd
from obd import ECU
import time
import os
import random
import keyboard

ports = obd.scan_serial()      # return list of valid USB or RF ports
print (ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
# connection = obd.OBD(ports[0]) # connect to the first port in the list

def RPMTest():
    connection = obd.Async(ports[0],delay_cmds=0.01, fast=True)
    connection.watch(obd.commands.RPM) # keep track of the RPM
    connection.start() # start the async update loop

    for x in range (1000): # A Testing loop just to see if the commands are actually being read properly
        print(connection.query(obd.commands.RPM))
        time.sleep(0.01)

def RPMGraphicTest():

    while True:
        print("########## Graphical Gauge Cluster ##########", end='\n')
        print('\n')
        test = random.randint(1,9000)
        print("#" * round(9000/200))
        print("RPM " + str(test))
        time.sleep(0.01)
        os.system('cls' if os.name == 'nt' else 'clear')


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
elif userChoice == "3":
    RPMGraphicTest()
else:
    print("very funny...")
