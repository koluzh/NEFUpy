import cv2
import numpy as np
import random


img = cv2.imread('plane.jpeg', 0)
n, m = img.shape[0], img.shape[1]

target = 0.1 * n * m
k = 0

while k < target:
    x = random.randint(0, n - 1)
    y = random.randint(0, m - 1)
    d = random.randint(0, 1)
    img[x][y] = 255 * (1 - d)
    k += 1

cv2.imwrite("plane_SP.jpeg", img)