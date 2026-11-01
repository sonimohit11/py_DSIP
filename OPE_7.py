import cv2
import numpy as np
import matplotlib.pyplot as plt

# GRAY-LEVEL TRANSFORMATION FUNCTIONS

# 1. Power-law / Gamma Transformation
def gamma_transform(image, gamma):
   image = image.astype(np.float32) / 255.0
   result = np.power(image, gamma)
   result = np.uint8(result * 255)
   return result

# 2. Logarithmic Transformation
def log_transform(image):
   image = image.astype(np.float32)

  # Normalize log result to 0-255
  result = np.log1p(image)
  result = result / result.max() * 255

  return np.uint8(result)

# 3. Contrast Stretching
def contrast_stretch(image, low, high):
   image = image.astype(np.float32)

  result = (image - low) * 255.0 / (high - low)

  result = np.clip(result, 0, 255)

  return np.uint8(result)

# READ IMAGES IN GRAYSCALE

image1 = cv2.imread("1.png", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("2.png", cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread("11.1.png", cv2.IMREAD_GRAYSCALE)
image4 = cv2.imread("22.2.png", cv2.IMREAD_GRAYSCALE)
image5 = cv2.imread("111.1.png", cv2.IMREAD_GRAYSCALE)


# Dark version of Image 1
# Use Gamma Correction + Contrast Stretching

image3_gamma = gamma_transform(image3, 0.55)

image3_enhanced = contrast_stretch(
  image3_gamma,
  30,
  200
)

# IMAGE 4
# Extremely dark car image
# Use Gamma Correction + Contrast Stretching

image4_gamma = gamma_transform(image4, 0.40)

image4_enhanced = contrast_stretch(
  image4_gamma,
  20,
  230
)

# IMAGE 5
# Very dark CT image
# Use Log Transformation + Gamma Correction

image5_log = log_transform(image5)

image5_enhanced = gamma_transform(
  image5_log,
  0.70
)

# DISPLAY RESULTS

plt.figure(figsize=(12, 12))

# Image 1
plt.subplot(3, 2, 1)
plt.imshow(image1, cmap="gray")


plt.title("Image 1 - Original")
plt.axis("off")

# Image 3
plt.subplot(3, 2, 2)
plt.imshow(image3_enhanced, cmap="gray")
plt.title("Image 3 - Enhanced")
plt.axis("off")

# Image 2
plt.subplot(3, 2, 3)
plt.imshow(image2, cmap="gray")
plt.title("Image 2 - Original")
plt.axis("off")

# Image 4
plt.subplot(3, 2, 4)
plt.imshow(image4_enhanced, cmap="gray")
plt.title("Image 4 - Enhanced")
plt.axis("off")

# Image 5 original
plt.subplot(3, 2, 5)
plt.imshow(image5, cmap="gray")
plt.title("Image 5 - Original")
plt.axis("off")

# Image 5 enhanced
plt.subplot(3, 2, 6)
plt.imshow(image5_enhanced, cmap="gray")
plt.title("Image 5 - Enhanced")
plt.axis("off")

plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# SAVE ENHANCED IMAGES
# ---------------------------------------------------------

cv2.imwrite("image3_enhanced.png", image3_enhanced)
cv2.imwrite("image4_enhanced.png", image4_enhanced)


cv2.imwrite("image5_enhanced.png", image5_enhanced)

print("Enhanced images saved successfully!")
