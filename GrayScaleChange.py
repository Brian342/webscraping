import cv2
import numpy as np

# Load the green apple image
image = cv2.imread('/Users/briankimanzi/Downloads/GreenApple.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the grayscale image
cv2.imwrite('gray_apple.jpg', gray_image)