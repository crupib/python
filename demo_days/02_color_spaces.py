#!/usr/local/bin/python3
# Need function that reads pixel hue value
import matplotlib.pyplot as plt
import cv2
import numpy
import pyautogui

img = cv2.imread("color_test.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Plot the image
fig, axs = plt.subplots(1, 3, figsize=(15, 15))
names = ["BGR", "RGB", "HSV"]
imgs = [img, img, hsv]
i = 0
for elem in imgs:
    axs[i].title.set_text(names[i])
    axs[i].imshow(elem)
    axs[i].grid(False)
    i += 1
plt.show()
