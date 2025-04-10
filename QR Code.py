import qrcode

# Ask the user for input
data = input("Enter the text or link you want to convert into a QR Code: ")

# Generate the QR code
qr = qrcode.make(data)

# Save the QR code image to Desktop
qr.save("C:/Users/HP/Desktop/my_qr_code.png")

print("✅ QR Code generated and saved to your Desktop!")
