import cv2
import numpy as np
filename = 'meet_my_electronic_pet_goofy.jpg'
img = cv2.imread(r"C:\Users\GAMING-3\Documents\meet_my_electronic_pet_goofy.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
img[dst > 0.01 *dst.max()] = (0, 0, 225)
cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
 cv2.destroyAllWindows()