import qrcode

url="https://example.com/menu"

img=qrcode.make(url)

img.save("menu_qr.png")

print("Qr Code created!")