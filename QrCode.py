import qrcode as dk
img = dk.make("https://github.com/Darshil999")

img.save("GitHub.png")

import qrcode as dk
from PIL import Image
qr=dk.QRCode(version=1, error_correction=dk.constants.ERROR_CORRECT_H, box_size=10,border=5)

qr.add_data("https://github.com/Darshil999")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="red")
img.save("GitHub@.png")



