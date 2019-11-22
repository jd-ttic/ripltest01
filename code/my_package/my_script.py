import os
import numpy as np
message = "Hello from {}!".format(os.environ['VEHICLE_NAME'])
print(message)
adding = "1 + 1 is {}".format(np.add(1.0,1.0))
print(adding)

