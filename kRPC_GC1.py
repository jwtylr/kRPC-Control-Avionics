import math
import time
import krpc
import numpy as np
import launch_controller as lc

# Connect and get static references
conn = krpc.connect()
vessel = conn.space_center.active_vessel
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
