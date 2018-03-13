import bluetooth,subprocess
print "looking for nearby devices..."
nearby_devices = bluetooth.discover_devices(lookup_names = True, flush_cache = True, duration = 20)
print "found %d devices" % len(nearby_devices)
#subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)
port1=0
ad1="E1:E1:1W:12"
for addr, name in nearby_devices:
    print " %s - %s" % (addr, name)
if(len(nearby_devices)>0):
	for services in bluetooth.find_service(address = addr):
		print (addr)	
		print " Name: %s" % (services["name"])
	        print " Description: %s" % (services["description"])
    		print " Protocol: %s" % (services["protocol"])
    		print " Provider: %s" % (services["provider"])
    		print " Port: %s" % (services["port"])
    		print " Service id: %s" % (services["service-id"])
    		print ""
    		print ""
	print("\n enter the address ")
	ad1=raw_input()
	print("\n enter the port ")
	port1=input()
	try:
		s=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		s.connect((ad1,port1))
		s.send("t1.py")
		print("send !!!")
	except 	bluetooth.btcommon.BluetoothError as err:
		print("Error!!!")		
		pass
