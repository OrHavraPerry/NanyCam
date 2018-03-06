import cv2
import datetime as td
import time
import os

# Change Path if u need
path = 'Capture'
if not os.path.exists(path):
    os.mkdir(path)

# Open Cams
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

# Check if cams ok
if not (cap1.isOpened() and cap2.isOpened()):
    print('Error: Openning Cams')
    print('cam1: ', cap1.isOpened())
    print('cam2: ', cap2.isOpened())

# saves data and show it
while cap1.isOpened() and cap2.isOpened():
    # delay
    time.sleep(2)

    # get time
    dt = str(td.datetime.now()).replace(" ","_").replace(":","-").split(".")[0]

    # capture
    _, image1 = cap1.read()
    _, image2 = cap2.read()

    # Show images
    cv2.imshow('Cam1', image1)
    cv2.imshow('Cam2', image2)

    # resize
    im1 = cv2.resize(image1, (100, 100))
    im2 = cv2.resize(image2, (100, 100))

    # exit if key is q
    if cv2.waitKey(1) == ord('q'):
        cap1.release()
        cap2.release()
        cv2.destroyAllWindows()
        break

    cv2.imwrite('{}\\Cam1_{}.png'.format(path,dt), im1)
    cv2.imwrite('{}\\Cam2_{}.png'.format(path,dt), im2)
