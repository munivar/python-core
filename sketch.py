import cv2

# Read an image from file
image = cv2.imread('nilkanth.png')

# Display the image
cv2.imshow('Original Image', image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the image window

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted = cv2.bitwise_not(gray_image)

# Smoothen Image
smoothen = cv2.GaussianBlur(inverted, (21,21), sigmaX=0, sigmaY=0)

# dodge image
def dodge(a, b):
    return cv2.divide(a, 255-b, scale=256)
final_image = dodge(gray_image, smoothen)

# Display the grayscale image
cv2.imshow('Final Image', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the grayscale image
cv2.imwrite('final.png', final_image)
