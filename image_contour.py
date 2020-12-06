
import cv2
import sys
import numpy as np
import random

#read input image
img = cv2.imread("testimage.jpg", cv2.IMREAD_GRAYSCALE)

#check if image exists
if img is None:
    print("Sorry, couldn't find an image")
    sys.exit()

#apply canny to the input image
canny = cv2.Canny(img, 50, 150, apertureSize=3)

#find contours
temp, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#output image to draw contours on
output = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

#draw contours
for i in range(0, len(contours)):
    cv2.drawContours(output, contours, i, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)


#create windows to display images
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("canny", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Image with Contours", cv2.WINDOW_AUTOSIZE)

#display images
cv2.imshow("Original Image", img)
cv2.imshow("canny", canny)
cv2.imshow("Image with Contours", output)

#press esc to exit the program
cv2.waitKey(0)

#close all the opened windows
cv2.destroyAllWindows()
