import cv2

image = cv2.imread('example.jpg')

resized_image = cv2.resize(image,(800,500))
cv2.imshow("Image 1",resized_image)
key = cv2.waitKey(0)
resized_image1 = cv2.resize(image,(600,400))
cv2.imshow("Image 2",resized_image1)
key = cv2.waitKey(0)
resized_image2 = cv2.resize(image,(400,300))
cv2.imshow("Image 3",resized_image2)
key = cv2.waitKey(0)


cv2.destroyAllWindows()