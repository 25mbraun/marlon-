from djitellopy import tello
from time import sleep

dr = tello.Tello()
dr.connect()
print(dr.get_battery())

dr.takeoff()

# Takeoff Point
dr.move_up(95)
dr.move_forward(500)
sleep(.5)
dr.move_forward(100)
sleep(1)

# Moving in to the flying zone
dr.rotate_counter_clockwise(90)
dr.move_forward(350)
sleep(1)

# Going to start
dr.Rotate_counter_clockwise(90)
dr.move_forward(500)
sleep(.5)
dr.move_forward(100)
sleep(1)

# Landing Zone for the drone
dr.rotate_counter_clockwise(90)
dr.move_forward(350)
sleep(1)

dr.Land()
