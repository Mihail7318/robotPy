import numpy as np
import cv2
import serial
import keyboard
import os
import time
import main
ser = serial.Serial("/dev/ttyUSB0", 19200)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,940) # set Width
cap.set(4,680) # set Height
a = False
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

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    #cv2.imshow('video',img)
    if faces == () and a == False:
        print("hold")
    else:
        p  = (w*h)/10
        print(p)
        if p < 5000:
            ser.write(b'w')
            time.sleep(0.05)
        if p > 7000:
            ser.write(b's')
            time.sleep(0.05)
        if x > 300:
            ser.write(b'a')
            time.sleep(0.05)
            a = True
        if x < 100:
            ser.write(b'd')
            time.sleep(0.05)
            a = True
        if keyboard.is_pressed("q"):
            ser.close()
            break

        #if p < 2500:
        #    #time.sleep(2)
        #    main.go(cap)
        #    break
        #    k = 27
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:  # press 'ESC' to quit
     #   break
      #  print(w)


#x = 0
cap.release()
#cv2.destroyAllWindows()