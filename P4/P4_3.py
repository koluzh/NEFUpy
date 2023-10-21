import cv2
import numpy as np
import random


img = cv2.imread('plane.jpeg', 0)
n, m = img.shape[0], img.shape[1]

target = (5/100) * n * m
sigma = 15
k = 0

while k < target:
    x = random.randint(0, n - 1)
    y = random.randint(0, m - 1)
    d = random.randint(0, 1)
    img[x][y] = img[x][y] + np.random.normal(0, 10, 1)
    img[x][y] = max(img[x][y], 0)
    img[x][y] = min(img[x][y], 255)
    k += 1

cv2.imwrite("plane_WN.jpeg", img)