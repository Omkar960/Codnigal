import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('example.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale image",gray_image)

key  =cv2.waitKey(0)

cv2.destroyAllWindows()

cropped_image = image[100:400,200:600]
cv2.imshow("Cropped image", cropped_image)
key  =cv2.waitKey(0)
cv2.destroyAllWindows()
(h,w) = image.shape[:2]
center = (w // 2 , h// 2)

matrix = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image,matrix,(w,h))
cv2.imshow("Rotated image",rotated)
key  =cv2.waitKey(0)
cv2.destroyAllWindows()

brighter = cv2.add(image,np.array([50]))
cv2.imshow("Brighter image",brighter)
key  =cv2.waitKey(0)
cv2.destroyAllWindows()