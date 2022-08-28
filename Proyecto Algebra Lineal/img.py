import matplotlib.pyplot as plt

import numpy as np
from skimage import io

image=io.imread("cromoterapia.jpg")/255.0

anti_identidad = np.eye(image.shape[1])[::-1]


img_red = np.matmul(image[:,:,0],anti_identidad)
plt.imsave("img_red.png",img_red)
img_green = np.matmul(image[:,:,1],anti_identidad)
plt.imsave("img_green.png",img_green)
img_blue = np.matmul(image[:,:,2],anti_identidad)
plt.imsave("img_blue.png",img_blue)
print(img_red)
print(img_green)
print(img_blue)

reflex_img = np.zeros((image.shape[0],image.shape[1],image.shape[2]))
for c in range(image.shape[0]):
    for f in range(image.shape[1]):
        reflex_img[c,f,0] = img_red[c,f]
        reflex_img[c,f,1] = img_green[c,f]
        reflex_img[c,f,2] = img_blue[c,f]

plt.imsave("img_reverse.png",reflex_img)

