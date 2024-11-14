import cv2
import numpy as np

img = cv2.imread(r"C:\Users\s44nidhya\Docs\meet_my_electronic_pet_goofy.jpg",0)

rows, cols = img.shape

M = np.float32([[1,0,100], [0,1,50]])

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
