# Import necessary libraries
import numpy as np
import cv2


# Function to read an image from a file
def read_image(file_path):
    return cv2.imread(file_path)


# Function to resize an image
def resize_image(image, width, height):
    return cv2.resize(image, (width, height))


# Function to filter an image based on color range
def filter_color(image, lower_range, upper_range):
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Create a mask using the specified color range
    mask = cv2.inRange(hsv_image, lower_range, upper_range)
    # Apply the mask to the original image
    return cv2.bitwise_and(image, image, mask=mask)


# Function to ask the user for color choice and filter the image accordingly
def ask_for_color():
    while True:
        print("Pick the color below:")
        print("1 = Red")
        print("2 = Green")
        print("3 = Yellow")
        print("4 = Blue")

        # Get user input
        user_input = input("Enter your input: ")
        user_input = int(user_input)

        # Filter the image based on the chosen color
        if user_input == 1:
            filtered_image = filter_color(resized_image, np.array([-10, 100, 100]), np.array([10, 255, 255]))
            show_images(resized_image, filtered_image)
        elif user_input == 2:
            filtered_image = filter_color(resized_image, np.array([40, 40, 40], dtype=np.uint8),
                                          np.array([70, 240, 250], dtype=np.uint8))
            show_images(resized_image, filtered_image)
        elif user_input == 3:
            filtered_image = filter_color(resized_image, np.array([20, 100, 100], dtype=np.uint8),
                                          np.array([40, 255, 255], dtype=np.uint8))
            show_images(resized_image, filtered_image)
        elif user_input == 4:
            filtered_image = filter_color(resized_image, np.array([50, 100, 100], dtype=np.uint8),
                                          np.array([130, 255, 255], dtype=np.uint8))
            show_images(resized_image, filtered_image)
        else:
            break


# Function to display the original and filtered images
def show_images(original_image, filtered_image):
    cv2.imshow('Original', original_image)
    cv2.imshow('Filtered', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Main code
# Read the image from a file
image = read_image("im3.png")
# Resize the image to a specified width and height
resized_image = resize_image(image, 400, 400)
# Ask the user for color choice and filter the image accordingly
ask_for_color()
