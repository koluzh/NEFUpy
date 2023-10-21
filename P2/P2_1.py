import numpy as np
import cv2

MAXITER = 70

WIDTH = 320
HEIGHT = 270

SCALE = 4

WIDTH_S = SCALE * WIDTH
HEIGHT_S = SCALE * HEIGHT
X1, Y1 = 0.45, 0.2
d = 0.1
X1 -= d/2
Y1 -= d/2
X2 = X1 + d/2
Y2 = Y1 + d/2

x = np.linspace(X1, X2, WIDTH_S)
y = np.linspace(Y1, Y2, HEIGHT_S)

img = np.zeros((WIDTH_S, HEIGHT_S, 3))


def interp(img, x1, y1, x2, y2):
    q11 = img[x1][y1] / SCALE ** 2
    q12 = img[x1][y2] / SCALE ** 2
    q22 = img[x2][y2] / SCALE ** 2
    q21 = img[x2][y1] / SCALE ** 2
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            # print(x, y)
            if x in [x1, x2] and y in [y1, y2]:
                continue
            img[x][y] = q11 * (x2 - x) * (y2 - y) + \
                q21 * (x - x1) * (y2 - y) + \
                q12 * (x2 - x) * (y - y1) + \
                q22 * (x - x1) * (y - y1)


if __name__ == '__main__':
    for i_t in range(WIDTH):
        for j_t in range(HEIGHT):
            i = i_t * SCALE
            j = j_t * SCALE
            C = complex(x[i], y[j])
            Z = complex(0.5, 0.5)
            it = 0
            while True:
                Z = (Z ** 2) + C
                print(i, HEIGHT_S - 1 - j)
                if (np.abs(Z) > 2):
                    img[i][j] = it
                    break
                if (it == MAXITER):
                    img[i][j] = it
                    break
                it += 1

    for i_t in range(WIDTH):
        for j_t in range(HEIGHT):
            if i_t == 0 or j_t == 0:
                continue
            i = i_t * SCALE
            j = j_t * SCALE
            interp(img, i - SCALE, j - SCALE, i, j)

    img = np.clip(img, 0, MAXITER)
    img = np.interp(img, (0, MAXITER), (0, 179)).astype(np.uint8)
    img = np.resize(img, (WIDTH_S, HEIGHT_S, 3))
    for i in range(WIDTH_S):
        for j in range(HEIGHT_S):
            img[i][j][1] = 255
            img[i][j][2] = 255

    for i in range(WIDTH_S):
        np.flip(img[i])

    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)


    cv2.imwrite('img.jpg', img)
