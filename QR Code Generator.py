import qrcode

data = input("Enter the Data.\n---> ")
border = input("\nEnter the Border Thick. Recommended = 1 (0-100)\n---> ")
f_color = input("\nEnter the Fill Color Name. Recommended = Black\n---> ")
b_color = input("\nEnter the Back Color Name. Recommended = White\n---> ")

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=border)

qr.add_data(data)

qrimg = qr.make_image(fill_color=f_color, back_color=b_color)

qrimg.save("QR.png")

print("\nQR Code Image Saved as QR.png.")