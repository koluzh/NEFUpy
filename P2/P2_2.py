import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import convolve2d as conv2

from skimage import color, data, restoration
import cv2

rng = np.random.default_rng()

astro = cv2.imread('kek.jpg')
astro = color.rgb2gray(astro)

psf = np.ones((5, 5)) / 25
astro = conv2(astro, psf, 'same')
astro += 0.1 * astro.std() * rng.standard_normal(astro.shape)

# Add Noise to Image
astro_noisy = astro.copy()
# Restore Image using Richardson-Lucy algorithm
deconvolved_RL, _ = restoration.unsupervised_wiener(astro_noisy, psf)

cv2.imwrite('kek_copy.jpg', deconvolved_RL)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 5))
plt.gray()

for a in (ax[0], ax[1], ax[2]):
       a.axis('off')

ax[0].imshow(astro)
ax[0].set_title('Original Data')

ax[1].imshow(deconvolved_RL, vmin=astro_noisy.min(), vmax=astro_noisy.max())
ax[1].set_title('Restoration using\nRichardson-Lucy')


fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)
plt.show()