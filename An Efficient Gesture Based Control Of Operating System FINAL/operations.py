import cv2
import numpy as np
import trackmodule as tm
import time
import autopy
import pyautogui
import time
from inputimeout import inputimeout
import threading

Movment = []
Right_click = []
left_click = []
double_click = []


width, height = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
detector = tm.handDetector(maxHands=1)
wscreen,hscreen = autopy.screen.size()


# def gesture():
#     threading.Timer(10.0, gesture).start()
#     return detector.fingersUp()

print("please give a gesture to do mouse movment")
o = str(input("Enter Y to scan your hand : "))
if o == 'Y' or o == 'y':
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)

        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            if len(Movment) != 100:
                Movment.append(detector.fingersUp())
                print(Movment)
                if len(Movment) == 100:
                    Movment = Movment[-1]
                    break

        cv2.imshow("Images", img)
        cv2.waitKey(1)
    print(Movment)

else:
    print("please scan your gesture to enable mouse movment")

print("please give a gesture to do right click operation")
o = str(input("Enter Y to scan your hand : "))
if o == 'Y' or o == 'y':
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)

        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            if len(Right_click) != 100:
                Right_click.append(detector.fingersUp())
                print(Right_click)
                if len(Right_click) == 100:
                    Right_click = Right_click[-1]
                    break

        cv2.imshow("Images", img)
        cv2.waitKey(1)
    print(Right_click)

else:
    print("please scan your gesture to enable right click operation")

print("please give a gesture to do left click operation")
r = str(input("Enter Y to scan your hand : "))
if r == 'Y' or r == 'y':
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)

        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            if len(left_click) != 100:
                left_click.append(detector.fingersUp())
                print(left_click)
                if len(left_click) == 100:
                    left_click = left_click[-1]
                    break

        cv2.imshow("Images", img)
        cv2.waitKey(1)
    print(left_click)

else:
    print("please scan your gesture to enable left click operation")

print("please give a gesture to do double click operation")
i = str(input("Enter Y to scan your hand : "))
if i == 'Y' or i == 'y':
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)

        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            if len(double_click) != 100:
                double_click.append(detector.fingersUp())
                print(double_click)
                if len(double_click) == 100:
                    double_click = double_click[-1]
                    break

    cv2.imshow("Images", img)
    cv2.waitKey(1)
    print(double_click)

else:
    print("please scan your gesture to enable double click operation")


c = []
c.append(Movment)
c.append(Right_click)
c.append(left_click)
c.append(double_click)

print("the input gestures are : ")
print(c)

smoothening = 7
px,py = 0,0
cx,cy = 0,0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # mouse movment
        b = c[0]
        if detector.fingersUp() == b:
            o1 = np.interp(x1, (0,width), (0,wscreen))
            o2 = np.interp(y1, (0,height), (0,hscreen))
            cx = px + (o1 - px) / smoothening
            cy = py + (o2 - py) / smoothening
            autopy.mouse.move(wscreen-cx,cy)
            px, py = cx, cy
        # right click
        if detector.fingersUp() == c[1]:
            o1 = np.interp(x1, (0,width), (0,wscreen))
            o2 = np.interp(y1, (0,height), (0,hscreen))
            cx = px + (o1 - px) / smoothening
            cy = py + (o2 - py) / smoothening
            pyautogui.click(wscreen-cx,cy,button='right')
        # left click
        if detector.fingersUp() == c[2]:
            o1 = np.interp(x1, (0,width), (0,wscreen))
            o2 = np.interp(y1, (0,height), (0,hscreen))
            cx = px + (o1 - px) / smoothening
            cy = py + (o2 - py) / smoothening
            pyautogui.click(cx,cy)
        # double click
        if detector.fingersUp() == c[3]:
            o1 = np.interp(x1, (0,width), (0,wscreen))
            o2 = np.interp(y1, (0,height), (0,hscreen))
            cx = px + (o1 - px) / smoothening
            cy = py + (o2 - py) / smoothening
            pyautogui.click(cx,cy,clicks=2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
