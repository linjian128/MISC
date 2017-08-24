import SimpleCV as scv

import time

cam = scv.Camera()

img = cam.getImage()

img.save("same.jpg")
