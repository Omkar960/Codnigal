import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image"""

    plt.figure(figsize=(8,8))
    if len(image.shape) == 2:
        plt.imshow(image,cmap= "grey")

    else:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis("off")
    plt.show()

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found")

        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    print("Select an option: ")
    print("1. Sobel Edge Detection ")
    print("2. Canny Edge Detection  ")
    print("3. Laplaican Edge Detection ")
    print("4. Gaussian Smoothing ")
    print("5. Median Filtering ")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6)")

        if choice == "1":
            sobelx = cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize = 3)

            sobely = cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize = 3)

            combined_sobel1 = cv2.bitwise_or(sobelx.astype(np.uint8),sobely.astype(np.uint8))

            display_image("Sobel Image Dectection", combined_sobel1)
        elif choice == "2":
            print("Adjust threshold for Canny(default: 100 and 200)")
            threshold1 = int(input("Enter lower threshold for Canny"))
            threshold2 = int(input("Enter higher threshold for Canny"))

            result = cv2.Canny(gray_image,threshold1,threshold2)
            display_image("Canny Edge detection",result)

        elif choice == "3":
            result = cv2.Laplacian(gray_image,cv2.CV_64F)
            display_image("Laplacian Edge Detection",np.abs(result).astype(np.uint8))
        elif choice == "4":
            print("Adjust Kernel Size for Gaussian blur(must be odd, default:5)")
            ksize = int(input("Enter Kernel size for Gaussian smoothing (odd number)"))
            result = cv2.GaussianBlur(image,(ksize,ksize),0)
            display_image("Gaussian Smoothed Image",result)
        elif choice == "5":
            print("Adjust Kernel Size for Median filtering(must be odd, default:5)")
            ksize = int(input("Enter Kernel size for Median filtering (odd number)"))
            result = cv2.medianBlur(image,ksize)
            display_image("Median Filtered Image",result)
        elif choice == "6":
            print("Existing...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6")

interactive_edge_detection("example-2.jpg")

    
