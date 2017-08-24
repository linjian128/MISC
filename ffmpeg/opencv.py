import cv2
import SimpleCV as scv

import time

cam = scv.Camera()

img = cam.getImage()

cv2.imshow("Image", img)  
