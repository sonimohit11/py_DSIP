import cv2
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------

image = cv2.imread(r"D:\College\SEM 5\DSIP\PY\OPEN CV\f1.jpg")
plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.title("Input Image")
plt.axis('off')
plt.show()

# ----------------------------------------------------------------

gray_image = cv2.imread(r"D:\College\SEM 5\DSIP\PY\OPEN CV\f1.jpg",
cv2.IMREAD_GRAYSCALE)

plt.Figure(figsize=(6, 6))
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# ----------------------------------------------------------------

negat_image = 255 - gray_image

plt.figure(figsize=(6,6))
plt.imshow(negat_image,cmap="gray")
plt.title("input Image")
plt.axis('off')
plt.show()

# ----------------------------------------------------------------

#appply log transformation
c = 80
log_image = c * np.log(1 + gray_image.astype(np.float32))
log_image = np.array(log_image, dtype=np.uint8)

plt.figure(figsize=(6,6))
plt.imshow(log_image, cmap='gray')
plt.title("input Image")
plt.axis('off')
plt.show()
