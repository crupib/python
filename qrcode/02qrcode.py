import qrcode

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the data to the QR code
qr.add_data("This is a one-time-use QR code.")

# Make the QR code
qr.make(fit=True)

# Save the QR code as an image
qr.make_image(fill_color="black", back_color="white").save("qrcode.png")
