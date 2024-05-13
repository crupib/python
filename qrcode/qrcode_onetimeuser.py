import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('This is a one-time user QR code')
qr.make(fit=True)
qr.make_image()
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
