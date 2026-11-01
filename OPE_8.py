import cv2

import numpy as np

import matplotlib.pyplot as plt

def generate_histrogram(image):

  histrogram = cv2.calcHist(image,[0], None, [256],[0, 256])

  return histrogram

input_path=r"D:\College\SEM 5\DSIP\PY\image.jpg"

input_image = cv2.imread(input_path)

gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

gray_image

input_hist = generate_histrogram(gray_image)

intensity = np.arange(256)

input_hist = np.ravel(input_hist)

input_hist

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)

plt.imshow(gray_image , cmap="gray")

plt.title("input image")

plt.axis("off")

plt.subplot(1,2,2)

plt.bar(intensity, input_hist)

plt.title("input image histogram")

plt.xlabel("intensity")

plt.ylabel("frequency / number if pixal")

plt.show()
