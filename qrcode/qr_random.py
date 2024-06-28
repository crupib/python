import qrcode
import random

# Generate a random string
random_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(10))

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the random string to the QR code
qr.add_data(random_string)

# Make the QR code
qr.make(fit=True)
# Save the QR code as an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
