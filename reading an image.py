import cv2 as cv;
#note that we are taking the global image path in the follwing code you can use local image path aswell
img = cv.imread(r"C:\Users\GAMING-3\Documents\meet_my_electronic_pet_goofy.jpg")

cv.imshow('image', img)

cv.waitKey(0)

cv.destroyAllWindows()