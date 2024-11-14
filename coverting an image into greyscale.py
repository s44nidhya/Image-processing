import cv2 as cv;
#importing the image
img = cv.imread(r"C:\Users\s44nidhya\Docs\meet_my_electronic_pet_goofy.jpg")

cv.waitKey(0)
#code for the convertion of BGR image into greyscale
grey_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#using imshow to show the image after covertion 
cv.imshow('greyscale', grey_image)

cv.waitKey(0)
