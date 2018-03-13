import bluetooth
from bluetooth.btcommon import BluetoothError
import time

class DeviceConnector:

TARGET_NAME = "Device name"
TARGET_ADDRESS = None
SOCKET = None

def __init__(self):
    pass

def getConnectionInstance(self):
    self.deviceDiscovery()
    if(DeviceConnector.TARGET_ADDRESS is not None):
        print('Device found!')
        self.connect_bluetooth_addr()
        return DeviceConnector.SOCKET
    else:
        print('Could not find target bluetooth device nearby')

def deviceDiscovery(self):
    try:
        nearby_devices = bluetooth.discover_devices(lookup_names = True, duration=5)
        while nearby_devices.__len__() == 0 and tries < 3:
            nearby_devices = bluetooth.discover_devices(lookup_names = True, duration=5)
            tries += 1
            time.sleep (200.0 / 1000.0)
            print ('couldnt connect! trying again...')
        for bdaddr, name in nearby_devices:
            if bdaddr and name == DeviceConnector.TARGET_NAME:
                DeviceConnector.TARGET_ADDRESS = bdaddr
                DeviceConnector.TARGET_NAME = name
    except BluetoothError as e:
        print ('bluetooth is off')

def connect_bluetooth_addr(self):
    for i in range(1,5):
        time.sleep(1)
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            sock.connect((DeviceConnector.TARGET_ADDRESS, 1))
            sock.setblocking(False)
            DeviceConnector.SOCKET = sock
            return
        except BluetoothError as e:
            print('Could not connect to the device')
    return None
