import cv2
import numpy as np


img = cv2.imread('plane.jpeg', 0)
n, m = img.shape[0], img.shape[1]
mean = 0
maxi = 0
mini = 1000

for i in range(n):
    for j in range(m):
        mean += img[i][j]
        maxi = max(maxi, img[i][j])
        mini = min(mini, img[i][j])
mean /= (n * m)

sigma = 0

for i in range(n):
    for j in range(m):
        sigma += (img[i][j] - mean) ** 2

sigma /= (n * m)

sigma = np.sqrt(sigma)

print(sigma)
print(maxi)
print(mini)
