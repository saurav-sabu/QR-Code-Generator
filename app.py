import streamlit as st 
import qrcode as qr
from PIL import Image

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

st.title("QR Code Generator")


vers = st.number_input("Choose The Version",1,40)
box_s = st.number_input("Specify Box Size",1)
bord = st.number_input("Specify Size Of Border",1)

data = st.text_input("Embed Data In The QR Code")
    

fill = st.color_picker("Pick The Face Color",value="#000000")
back = st.color_picker("Pick The Background Color",value="#FFFFFF")

qr_new = qr.QRCode(version=vers,
error_correction=qr.ERROR_CORRECT_H,
box_size=box_s,
border=bord,)

# Embed the link using add_data()
qr_new.add_data(data)

# make() is used to create a QR Code
qr_new.make(fit=True)

# Changing the color of the Qr Code

img = qr_new.make_image(fill_color=fill,back_color=back)

# save() is used to save QR Code in form of image
img.save("img.png")

with open("img.png","rb") as file:
    btn = st.download_button("Download",data=file,file_name="qrcode.png",mime="image/png")




