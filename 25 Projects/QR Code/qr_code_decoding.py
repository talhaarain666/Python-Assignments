from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("D:/Gov House (Python Q3)/Python-Assignments/25 Projects/QR Code/myqrcode.png")

result = decode(img)

print(result)