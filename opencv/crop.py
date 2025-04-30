import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread("bill.jpeg")

# Check if image was successfully loaded
if img is None:
    raise FileNotFoundError("Could not load image 'my.jpg'")

# Define crop dimensions
y1, y2 = 50, 250
x1, x2 = 120, 330

# Crop the image
cropped_img = img[y1:y2, x1:x2]

# Convert BGR to RGB for matplotlib display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cropped_img_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)

# Display the images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Cropped Image")
plt.imshow(cropped_img_rgb)
plt.axis("off")

plt.show()
