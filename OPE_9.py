import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load Image 1
image = cv2.imread("img1.png")

if image is None:
    print("Image not found: img1.png")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Smoothing
gaussian = cv2.GaussianBlur(gray, (5, 5), 0)

# Median Smoothing
median = cv2.medianBlur(gray, 5)

# Sharpening Filter
sharpening_kernel = np.array([
   [0, -1, 0],
   [-1, 5, -1],
   [0, -1, 0]
])

sharpened = cv2.filter2D(gray, -1, sharpening_kernel)

# Unsharp Masking
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
unsharp = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)
plt.figure(figsize=(15, 8))
plt.subplot(2, 3, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")
plt.subplot(2, 3, 2)
plt.imshow(gaussian, cmap="gray")


plt.title("Gaussian Smoothing")
plt.axis("off")
plt.subplot(2, 3, 3)
plt.imshow(median, cmap="gray")
plt.title("Median Smoothing")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(sharpened, cmap="gray")
plt.title("Sharpening")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(unsharp, cmap="gray")
plt.title("Unsharp Masking")
plt.axis("off")

plt.suptitle("Image 1 - Smoothing and Sharpening")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("img2.png")
if image is None:
    print("Image not found: img2.png")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
median = cv2.medianBlur(gray, 5)
sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharpened = cv2.filter2D(
    gray, -1, sharpening_kernel
)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
unsharp = cv2.addWeighted(
    gray, 1.5, blurred, -0.5, 0
)
plt.figure(figsize=(15, 8))
plt.subplot(2, 3, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(gaussian, cmap="gray")
plt.title("Gaussian Smoothing")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(median, cmap="gray")
plt.title("Median Smoothing")
plt.axis("off")

plt.subplot(2, 3, 4)


plt.imshow(sharpened, cmap="gray")
plt.title("Sharpening")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(unsharp, cmap="gray")
plt.title("Unsharp Masking")
plt.axis("off")

plt.suptitle("Image 2 - Smoothing and Sharpening")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("img3.png")
if image is None:
    print("Image not found: img3.png")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
# Median Smoothing
median = cv2.medianBlur(gray, 5)
sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharpened = cv2.filter2D(
    gray, -1, sharpening_kernel
)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

unsharp = cv2.addWeighted(
  gray, 1.5, blurred, -0.5, 0
)
plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(gaussian, cmap="gray")
plt.title("Gaussian Smoothing")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(median, cmap="gray")
plt.title("Median Smoothing")


plt.axis("off")
plt.subplot(2, 3, 4)
plt.imshow(sharpened, cmap="gray")
plt.title("Sharpening")
plt.axis("off")
plt.subplot(2, 3, 5)
plt.imshow(unsharp, cmap="gray")
plt.title("Unsharp Masking")
plt.axis("off")
plt.suptitle("Image 3 - Smoothing and Sharpening")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("img4.png")
   print("Image not found: img4.png")
   exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
median = cv2.medianBlur(gray, 5)
sharpening_kernel = np.array([
   [0, -1, 0],
   [-1, 5, -1],
   [0, -1, 0]
])
sharpened = cv2.filter2D(
   gray, -1, sharpening_kernel
)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
unsharp = cv2.addWeighted(
   gray, 1.5, blurred, -0.5, 0
)
plt.figure(figsize=(15, 8))
plt.subplot(2, 3, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(gaussian, cmap="gray")
plt.title("Gaussian Smoothing")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(median, cmap="gray")
plt.title("Median Smoothing")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(sharpened, cmap="gray")


plt.title("Sharpening")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(unsharp, cmap="gray")
plt.title("Unsharp Masking")
plt.axis("off")

plt.suptitle("Image 4 - Smoothing and Sharpening")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load Image 5
image = cv2.imread("img5.png")

if image is None:
    print("Image not found: img5.png")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Smoothing
gaussian = cv2.GaussianBlur(gray, (5, 5), 0)

# Median Smoothing
median = cv2.medianBlur(gray, 5)

# Sharpening Filter
sharpening_kernel = np.array([
   [0, -1, 0],
   [-1, 5, -1],
   [0, -1, 0]
])

sharpened = cv2.filter2D(
  gray, -1, sharpening_kernel
)

# Unsharp Masking
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

unsharp = cv2.addWeighted(
  gray, 1.5, blurred, -0.5, 0
)


# Display Results
plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(gaussian, cmap="gray")
plt.title("Gaussian Smoothing")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(median, cmap="gray")
plt.title("Median Smoothing")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(sharpened, cmap="gray")
plt.title("Sharpening")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(unsharp, cmap="gray")
plt.title("Unsharp Masking")
plt.axis("off")

plt.suptitle("Image 5 - Smoothing and Sharpening")
plt.tight_layout()
plt.show()


# ----------------------------------------------------------------

import cv2
import matplotlib.pyplot as plt

# Load Image 1 in grayscale
image = cv2.imread("img1.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found: img1.png")
    exit()

# Apply Median Filters
median3 = cv2.medianBlur(image, 3)
median5 = cv2.medianBlur(image, 5)
median7 = cv2.medianBlur(image, 7)

# Display Results


plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(median3, cmap="gray")
plt.title("Median Filter (3x3)")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(median5, cmap="gray")
plt.title("Median Filter (5x5)")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(median7, cmap="gray")
plt.title("Median Filter (7x7)")
plt.axis("off")

plt.tight_layout()
plt.show()
