import os
message = "Hello from !".format(os.environ['VEHICLE_Name'])
print(message)
