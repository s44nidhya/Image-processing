import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\s44nidhya\Docs\meet_my_electronic_pet_goofy.jpg")
rows, cols, ch = img.shape

pts1 = np.float32([[56,65], [368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0], [0,300], [300,300]])

M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img, M, (300,300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

