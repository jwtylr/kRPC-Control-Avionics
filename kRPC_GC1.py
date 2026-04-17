import math
import time
import krpc

conn = krpc.connect()
vessel = conn.space_center.active_vessel
