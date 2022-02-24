# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#  drone wifi name = 6EA

from djitellopy import Tello
from time import sleep

Julisian = Tello()
Julisian.connect()
print(Julisian.get_battery(), "%")

input("Ready? ")

Julisian.takeoff()
Julisian.move_up(120)
Julisian.rotate_clockwise(360)
Julisian.flip("f")
sleep(1)
Julisian.flip("b")
sleep(1)
Julisian.land()


