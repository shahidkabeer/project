import bluetooth
print "looking for nearby devices..."
nearby_devices = bluetooth.discover_devices(lookup_names = True, flush_cache = True, duration = 20)
print "found %d devices" % len(nearby_devices)

print " Name: %s" % (services["name"])
print " Description: %s" % (services["description"])
print " Protocol: %s" % (services["protocol"])
print " Provider: %s" % (services["provider"])
print " Port: %s" % (services["port"])
print " Service id: %s" % (services["service-id"])

