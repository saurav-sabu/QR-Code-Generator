# Importing module
import qrcode as qr

# QRCode() is used to change the functionality of qr code
qr_new = qr.QRCode(version=1,
error_correction=qr.ERROR_CORRECT_H,
box_size=14,
border=4,)

# Embed the link using add_data()
qr_new.add_data("https://www.youtube.com/watch?v=OCr5uCPHGE0")

# make() is used to create a QR Code
qr_new.make(fit=True)

# Changing the color of the Qr Code
img = qr_new.make_image(fill_color="blue",back_color="red")

# save() is used to save QR Code in form of image
img.save("updated_qr.png")
