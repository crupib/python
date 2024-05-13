import qrcode
import uuid

# Generate a unique ID for the QR code
qr_id = uuid.uuid4()

# Create a QR code object
qr_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

# Add the unique ID to the QR code
qr_code.add_data(qr_id)

# Make the QR code image
qr_code.make(fit=True)

# Save the QR code image
img = qr_code.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
