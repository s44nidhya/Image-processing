import cv2
import numpy as np

#reading an image in greyscale
img = cv2.imread(r"C:\Users\s44nidhya\Docs\meet_my_electronic_pet_goofy.jpg", 0)
rows, cols = img.shape

# Define rotation matrix to rotate the image by 90 degrees
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)

# Apply the rotation
dst = cv2.warpAffine(img, M , (cols, rows))

# Display the original and rotated images
cv2.imshow('Original Image ', img)
cv2.imshow('Rotation_img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
