import math
import time
import krpc
import numpy as np
import launch_controller as lc

# Connect and get static references
conn = krpc.connect()
vessel = conn.space_center.active_vessel
<<<<<<< HEAD:kRPC_CG1.py
body = vessel.orbit.body
refframe = body.non_rotating_reference_frame

# Get streams
altitude = conn.add_stream(getattr, vessel.flight(refframe), 'mean_altitude')
velocity = conn.add_stream(getattr, vessel.flight(refframe), 'velocity')




if __name__ == "__main__":

    # Launch
    #lc.launch(vessel)    


    while True:
        time.sleep(0.1)
        if vessel.flight().mean_altitude > 10000:
            break

    print("CG1 complete")
=======
>>>>>>> 595927f4a53aff017bc43f9bc79ae39e09441e0f:kRPC_GC1.py
