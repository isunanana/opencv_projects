
import cv2
import sys
import numpy as np

#Read image
img = cv2.imread("testimage.jpg")

#Check if image exists
if img is None:
    print("Sorry, couldn't find an image")
    sys.exit()

#create a copy of input image to work on so that at the end of program we can compare input and output image
image = np.copy(img)

#convert color image to gray scale image
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#resizing down the image 0.3 times
resizedDownImage = cv2.resize(image, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)

#resizing up the image 1.5 times
resizedUpImage = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

#crop the input image
croppedImage = image[0:700, 500:1000]

#Draw a line over image
lineImage = image.copy()
cv2.line(lineImage, (750, 300), (500,1000), (0, 0, 255), thickness=4, lineType=cv2.LINE_AA)

#Draw a cirle over image
circleImage = image.copy()
cv2.circle(circleImage, (750, 300), 250, (0, 0, 255), thickness=4, lineType=cv2.LINE_AA)

#Draw an ellipse over image
ellipseImage = image.copy()
cv2.ellipse(ellipseImage, (750, 300), (200, 250), 45, 0, 360, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA)
cv2.ellipse(ellipseImage, (750, 300), (200, 250), 135, 0, 360, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA)

#Draw a rectangle over image
rectangleImage = image.copy()
cv2.rectangle(rectangleImage, (750, 300), (1000, 600), (0, 0, 255), thickness=4, lineType=cv2.LINE_AA)

#Draw text over image
textImage = image.copy()
cv2.putText(textImage, "This is a text script on this image", (750, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


#create windows to display images
cv2.namedWindow("input image", cv2.WINDOW_NORMAL)
cv2.namedWindow("gray image", cv2.WINDOW_NORMAL)
cv2.namedWindow("resized up", cv2.WINDOW_NORMAL)
cv2.namedWindow("resized down", cv2.WINDOW_NORMAL)
cv2.namedWindow("line image", cv2.WINDOW_NORMAL)
cv2.namedWindow("circle image", cv2.WINDOW_NORMAL)
cv2.namedWindow("rectangle image", cv2.WINDOW_NORMAL)
cv2.namedWindow("ellipse image", cv2.WINDOW_NORMAL)
cv2.namedWindow("text image", cv2.WINDOW_NORMAL)

#display images
cv2.imshow("input image", img)
cv2.imshow("gray image", grayImage)
cv2.imshow("resized up", resizedUpImage)
cv2.imshow("resized down", resizedDownImage)
cv2.imshow("line image", lineImage)
cv2.imshow("circle image", circleImage)
cv2.imshow("rectangle image", rectangleImage)
cv2.imshow("ellipse image", ellipseImage)
cv2.imshow("text image", textImage)

#save images to disk
cv2.imwrite("gray_putin.jpg", grayImage)
cv2.imwrite("resized_up.jpg", resizedUpImage)
cv2.imwrite("resized_down.jpg", resizedDownImage)
cv2.imwrite("crop_image.jpg", croppedImage)
cv2.imwrite("line_image.jpg", lineImage)
cv2.imwrite("circle_image.jpg", circleImage)
cv2.imwrite("ellipse_image.jpg", ellipseImage)
cv2.imwrite("rectangle_image.jpg", rectangleImage)
cv2.imwrite("text_image.jpg", textImage)

#this will pause the program until you press any key from keyboard
cv2.waitKey(0)

#destroy all windows opened
cv2.destroyAllWindows()
