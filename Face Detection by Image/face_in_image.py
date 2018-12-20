# -*- coding: utf-8 -*-
"""GitHub_Face in Image.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SgfYCVBdVCUDToszT3L4jak9vTw2QEsI
"""

#Installing modules we need. And doing it only once.
import pkgutil; 
if not pkgutil.find_loader("missingno"):
  !pip install missingno -q

#importing modules we need 
import os.path
from pathlib import Path
from matplotlib import pyplot as plt

def get_file(url):
  fname = url.split('/')[-1]
  if not Path(fname).exists():
    print("Getting ", fname)
    !wget {url} -q

get_file("https://www.dropbox.com/s/retmd6htwsnnomq/test1.jpg?dl=0")
get_file("https://www.dropbox.com/s/mq7julne4cudghx/haarcascade_frontalface_default.xml")
get_file("https://www.dropbox.com/s/vfupjlbhtd9qjnf/test2.jpg?dl=0")
get_file("https://www.dropbox.com/s/rpuk1odtg5hycjy/messi.png")
get_file("https://www.dropbox.com/s/n59r5nd02dan1a0/messi2.png")

import cv2
import numpy as np

def imshow(image):
  plt.grid(False)
  if len(image.shape) == 3:
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  else:
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))

image = cv2.imread("test1.jpg?dl=0")
print("height: {} pixels".format(image.shape[0]))
print("width: {} pixels".format(image.shape[1]))
print("channels: {}".format(image.shape[2]))
image.shape

imshow(image)

gr_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imshow(gr_image)

def detect_face(image, scaleFactor = 1.2, minNeighbors = 5, minSize = (30, 30)):
  get_file("https://www.dropbox.com/s/mq7julne4cudghx/haarcascade_frontalface_default.xml")
  faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
  gr_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  rects = faceCascade.detectMultiScale(gr_image,
               scaleFactor = scaleFactor,
               minNeighbors = minNeighbors, minSize = minSize,
               flags = cv2.CASCADE_SCALE_IMAGE)
  for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
  return image

image = cv2.imread("test1.jpg?dl=0")
fc_image = detect_face(image,scaleFactor = 1.1, minNeighbors = 5,
                      minSize = (30, 30))

imshow(fc_image)

image = cv2.imread("test2.jpg?dl=0")
imshow(image)

image = cv2.imread("test2.jpg?dl=0")
fc_image = detect_face(image,scaleFactor = 1.1, minNeighbors = 5,
                      minSize = (30, 30))

imshow(fc_image)

image = cv2.imread("messi2.png")
fc_image = detect_face(image,scaleFactor = 1.1, minNeighbors = 5,
                      minSize = (30, 30))

imshow(fc_image)

image = cv2.imread("messi2.png")
fc_image = detect_face(image,scaleFactor = 1.2, minNeighbors = 5,
                      minSize = (30, 30))

imshow(fc_image)
