# Importing qrcode module
import qrcode as qr

# make() is used to create a QR Code
img = qr.make("https://www.youtube.com/")

# save() is used to save QR Code in form of image
img.save("qr_youtube.png")