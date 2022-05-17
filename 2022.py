from djitellopy import tello
from time import sleep

M1 = tello.Tello()
M1.connect()
print(M1.get_battery())

M1.takeoff()

#  Starting Takeoff Point
M1.move_up(95)
M1.move_forward(400)
sleep(.5)
M1.move_forward(400)
sleep(1)

# Moving in to the flying zone
M1.rotate_counter_clockwise(90)
M1.move_forward(350)
sleep(1)

# Going to start
M1.Rotate_counter_clockwise(90)
M1.move_forward(350)
sleep(.5)
M1.move_forward(350)
sleep(1)

# Landing Zone for the drone
M1.rotate_counter_clockwise(90)
M1.move_forward(370)
sleep(1)

M1.Land()
