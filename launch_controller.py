def launch(vessel):
    import time
    import krpc

    # Launch
    vessel.control.throttle = 1.0
    for i in range(3):
        time.sleep(1)
        print(3-i)
    vessel.control.activate_next_stage()

    # Nominal launch
    return 1