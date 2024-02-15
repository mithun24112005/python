import qrcode


def generate_qrcode(text, save):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # img.save("ironman.png") #will be saved in this name
    img.save(save)


url = input("enter the url: ")
save = input("enter the name it has to be saved: ")
save = save + ".png"
generate_qrcode(url, save)
