import qrcode

# Define UPI QR Code Format
upi_data = "upi://pay?pa=devkewalramani1234@okaxis&pn=Dev KewalRamani&mc=0000&tid=TXN789456&tr=ORDER1234&mam=2.0&tn=&am=2.00&cu=INR"

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(upi_data)
qr.make(fit=True)

# Generate QR Code Image
img = qr.make_image(fill="black", back_color="white")

# Save and Show QR Code
img.save("upi_qr.png")
img.show()
