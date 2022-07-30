import qrcode

data = input("Enter the Data.\n---> ")
border = input("\nEnter the Border Thick. Recommended = 1 (0-100)\n---> ")
f_color_hex = input("\nEnter the Fill Color as hex code. (Black = 000000)\n---> ")
b_color_hex = input("\nEnter the Back Color as hex code. (White = FFFFFF)\n---> ")

f_color = tuple(int(f_color_hex[i:i+2], 16) for i in (0, 2, 4))
b_color = tuple(int(b_color_hex[i:i+2], 16) for i in (0, 2, 4))

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=border)

qr.add_data(data)

qrimg = qr.make_image(fill_color=(f_color[0], f_color[1], f_color[2]), back_color=(b_color[0], b_color[1], b_color[2]))

qrimg.save("QR.png")

print("\nQR Code Image Saved as QR.png.")