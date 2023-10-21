import cv2
import numpy as np
import random

f_1 = 'plane.jpeg'
f_2 = 'plane_WN.jpeg'


def get_mse(pre, aft):
    img1 = cv2.imread(pre, 0)
    n, m = img1.shape[0], img1.shape[1]
    img2 = cv2.imread(aft, 0)
    res = 0
    for i in range(n):
        for j in range(m):
            res += (img1[i][j] - img2[i][j]) ** 2

    res /= n * m
    return res


mse = get_mse(f_1, f_2)
psnr = 20 * np.log10(255 / np.sqrt(mse))

print('mse: ', mse)
print('psnr: ', psnr)




