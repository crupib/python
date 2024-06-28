import qrcode_generator

# Create a QR code object
qr = qrcode_generator.QRCode(
    data="This is a one-time-use QR code.",
    version=1,
    error_correction=qrcode_generator.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    one_time_use=True,
)

# Save the QR code to a file
qr.save("qrcode.png")
