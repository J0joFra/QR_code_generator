import pyqrcode

qr =  pyqrcode.create(r"https://www.youtube.com/@jofrancalanci") #link
qr.svg('QR_code.svg', scale=10, background="white", module_color="black")
