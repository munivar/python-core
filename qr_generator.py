# install all the libraries needed
# create a function that collect text and convert it to qrcode
# save the qr as image
# run the function

# Importing library
import qrcode


def genarateQR(text):
    # Creating an instance of QRCode class
    qr = qrcode.QRCode(version=1, box_size=10, border=1)  # type: ignore
    # Adding data to the instance 'qr'
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    # save image in directory
    img.save('demoqr.png')


# getting data from user
data = input("Enter data that you want store in QR: ")
# running function
genarateQR(data)
