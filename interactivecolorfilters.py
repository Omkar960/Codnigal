import cv2 

import numpy as np

def apply_colorfilter(image,filter_type):
    
    filtered_image = image.copy()

    if filter_type == "red_tint":

        filtered_image[:,:,1] = 0

        filtered_image[:,:,0] = 0

    elif filter_type == "blue_tint":

        filtered_image[:,:,1] = 0

        filtered_image[:,:,2] = 0
    elif filter_type == "green_tint":

        filtered_image[:,:,0] = 0

        filtered_image[:,:,2] = 0

    elif filter_type == "increase_red":

        filtered_image[:,:,2] = cv2.add(filtered_image[:,:,2],50)

    elif filter_type == "decrease_green":

        filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,1],50)

    elif filter_type == "increase_green":

        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,1],50)

    elif filter_type == "decrease_blue":

        filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,0],50)

    elif filter_type == "increase_blue":

        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,0],50)

    elif filter_type == "decrease_red":

        filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,2],50)

    elif filter_type == "increase_red":

        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,2],50)

    elif filter_type == "increase_red_increase_blue":

        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,2],50)
        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,0],50)

    elif filter_type == "increase_blue_increase_green":

        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,1],50)
        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,0],50)

    elif filter_type == "increase_red_increase_green":

        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,2],50)
        filtered_image[:,:,0] = cv2.add(filtered_image[:,:,1],50)
    



    
    return filtered_image

image_path = 'example-2.jpg'

image = cv2.imread(image_path)

if image is None:
    print("Error: image is not found")

else:
    filter_type = "original"

    print("Press the following keys to apply filters: ")

    print("1 - Red Tint")

    print("2 - Blue Tint")

    print("3 - Green Tint")

    print("4 - Increase Red Intensity")

    print("5 - Increase Blue Intensity")

    print("6 - Decrease Green Intensity")

    print("7 - Increase Green Intensity")

    print("8 - Decrease Red Intensity")

    print("9 - Decrease Blue Intensity")

    print("r - Red and Blue intensity(increase)")

    print("b - Blue and Green Intensity(increase)")

    print("g - Red and Green intensity(increase)")




    print("q - Quit")

    while True:

        filtered_image = apply_colorfilter(image,filter_type)

        resized_image = cv2.resize(filtered_image,(600,500), interpolation= cv2.INTER_AREA)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('1'):
            filter_type = "red_tint"


        elif key == ord('2'):
            filter_type = "blue_tint"

        elif key == ord('3'):
            filter_type = "green_tint"
        
        elif key == ord('5'):
            filter_type = "increase_blue"
        
        elif key == ord('7'):
            filter_type = "increase_green"

        elif key == ord('6'):
            filter_type = "decrease_green"

        elif key == ord('8'):
            filter_type = "decrease_red"

        elif key == ord('4'):
            filter_type = "increase_red"

        elif key == ord('9'):
            filter_type = "decrease_blue"

        elif key == ord('r'):
            filter_type = "increase_red_increase_blue"

        elif key == ord('b'):
            filter_type = "increase_blue_increase_green"

        elif key == ord('g'):
            filter_type = "increase_red_increase_green"

        

        elif key == ord('q'):
            print("Exiting...")
            break

        else:
            print("Invalid key! Please use: 'r','g','b','ib','dr','ir','ig','dg','bg','rb','db','q'.")

cv2.destroyAllWindows


    
 



