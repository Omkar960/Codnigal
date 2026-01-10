import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('example1.jpg')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image",gray_image)
cv2.imwrite("gray_image.jpg",gray_image)
cv2.waitKey(0)
cropped_image = image[100:300]
cv2.imshow("Image",cropped_image)
cv2.imwrite("cropped_image.jpg",cropped_image)
cv2.waitKey(0)
(h,w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center,45,1.0)
rotated_image = cv2.warpAffine(image,M,(w,h))
cv2.imshow("Image",rotated_image)
cv2.imwrite("rotated_image.jpg",rotated_image)
cv2.waitKey(0)
value_matrix = np.ones(image.shape,dtype="uint8")*50
bright_image= cv2.add(image,value_matrix)
cv2.imshow("Image",bright_image)
cv2.imwrite("brightened_image.jpg",bright_image)
cv2.waitKey(0)
cv2.destroyAllWindows()