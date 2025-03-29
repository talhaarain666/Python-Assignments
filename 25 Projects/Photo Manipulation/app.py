import cv2
import numpy as np

def adjust_brightness(image, value):
    return cv2.convertScaleAbs(image, alpha=1, beta=value)

def adjust_contrast(image, value):
    return cv2.convertScaleAbs(image, alpha=value, beta=0)

def apply_blur(image, ksize):
    return cv2.GaussianBlur(image, (ksize, ksize), 0)

def apply_kernel(image, kernel):
    return cv2.filter2D(image, -1, kernel)

def combine_images(image1, image2, alpha=0.5):
    return cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)

# Load images
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

# Resize images to match dimensions
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Apply manipulations
bright_image = adjust_brightness(image1, 50)
contrast_image = adjust_contrast(image1, 1.5)
blurred_image = apply_blur(image1, 5)
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # Sharpening kernel
filtered_image = apply_kernel(image1, kernel)
combined_image = combine_images(image1, image2, 0.7)

# Save images in the same folder
cv2.imwrite("brightened.jpg", bright_image)
cv2.imwrite("contrasted.jpg", contrast_image)
cv2.imwrite("blurred.jpg", blurred_image)
cv2.imwrite("filtered.jpg", filtered_image)
cv2.imwrite("combined.jpg", combined_image)

# Display images
cv2.imshow("Brightened", bright_image)
cv2.imshow("Contrasted", contrast_image)
cv2.imshow("Blurred", blurred_image)
cv2.imshow("Filtered", filtered_image)
cv2.imshow("Combined", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
