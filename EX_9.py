import cv2
     import numpy as np
     from tkinter import Tk, filedialog

     # Open image selection window
     root = Tk()
     root.withdraw()

     image_path = filedialog.askopenfilename(
       title="Select an image",
       filetypes=[
           ("Image files", "*.jpg *.jpeg *.png *.bmp")
       ]
     )

     root.destroy()

     # Load image
     image = cv2.imread(image_path)

     if image is None:
         print("Error: Image not found!")
     else:
         print("Image loaded successfully!")
         print("Image size:", image.shape)
     smoothed_image = cv2.blur(image, (5, 5))
     kernel = np.array([
         [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
     ])
     sharpened_image = cv2.filter2D(image, -1, kernel)

     cv2.imshow("Original Image", image)
     cv2.imshow("Smoothed Image", smoothed_image)
     cv2.imshow("Sharpened Image", sharpened_image)

     cv2.imwrite("smoothed_image.jpg", smoothed_image)
     cv2.imwrite("sharpened_image.jpg", sharpened_image)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     print("Images processed and saved successfully!")

# ----------------------------------------------------------------

import cv2
     import numpy as np
     from tkinter import Tk, filedialog

     # Select input image
     root = Tk()
     root.withdraw()

     image_path = filedialog.askopenfilename(
       title="Select an Image",
       filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
     )

     root.destroy()

     # Load image
     image = cv2.imread(image_path)

     if image is None:
         print("Error: Image not found!")
         exit()

     # Apply Gaussian smoothing, as in the PDF
     smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

     # Create sharpening kernel
     sharpening_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
     ], dtype=np.float32)

     # Apply sharpening filter
     sharpened_image = cv2.filter2D(
       smoothed_image, -1, sharpening_kernel
     )

     # Display images
     cv2.imshow("Original Image", image)
     cv2.imshow("Smoothed Image", smoothed_image)
     cv2.imshow("Sharpened Image", sharpened_image)

     # Save output images
     cv2.imwrite("averaging_smoothed.jpg", smoothed_image)
     cv2.imwrite("sharpened_image.jpg", sharpened_image)
     # Wait and close windows
     cv2.waitKey(0)
     cv2.destroyAllWindows()

     print("Images processed and saved successfully!")
