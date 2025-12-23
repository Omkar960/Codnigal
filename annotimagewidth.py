import cv2
import matplotlib.pyplot as plt

image = cv2.imread('example1.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, channels = image.shape
print(f"Image width: {width}")

cv2.putText(image_rgb, f"Width: {width}", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 3)


cv2.arrowedLine(image_rgb, (0, height//2), (width-1, height//2), (255, 255, 255), 2, tipLength=0.05)

cv2.arrowedLine(image_rgb, (width-1, height//2), (0, height//2), (255, 255, 255), 2, tipLength=0.05)



plt.imshow(image_rgb)
plt.title("Image Width")
plt.show()
