import numpy as np
import cv2
import serial
import keyboard
import time
import main
import PID
import uart
#ser = serial.Serial("COM5", 19200)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

targetT = 200
P = 0.5
I = 0.5
D = 0.05

pid = PID.PID(P, I, D)
pid.SetPoint = targetT
pid.setSampleTime(0.05)



def readConfig():
    global targetT, P, I, D
    pid.SetPoint = float(targetT)
    targetT = pid.SetPoint
    pid.setKp(P)
    pid.setKi(I)
    pid.setKd(D)


cap = cv2.VideoCapture(0)
cap.set(3, 940)  # set Width
cap.set(4, 680)  # set Height
a = False
i = 0
errp = 0
count = 0
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    #cv2.imshow('video', img)
    # = cv2.waitKey(30) & 0xff
    #if k == 27:  # press 'ESC' to quit
    #    break
    if faces == () and a == False:
        print("hold")
        data = [0, 0]
    else:
        data = [0, x, w]
        uart.serialWrite(data)
        print(x)
        if 100 < x < 230:
            count = count + 1
        if count > 5:
            main.go(cap)
            break
x = 0
cap.release()
#cv2.destroyAllWindows()
