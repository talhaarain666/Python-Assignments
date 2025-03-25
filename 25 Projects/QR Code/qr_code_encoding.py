import qrcode

data = "https://www.streamlit.io/"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")

# img = qrcode.make(data)

img.save("D:/Gov House (Python Q3)/Python-Assignments/25 Projects/QR Code/myqrcode1.png")