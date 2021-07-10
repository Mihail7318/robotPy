from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop()