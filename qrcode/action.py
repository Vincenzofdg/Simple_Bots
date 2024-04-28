from qrcode import QRCode, constants


def create(url, name):
     result = QRCode( 1, constants.ERROR_CORRECT_L, 500, 1)

     result.add_data(url)
     result.make(fit=True)

     img = result.make_image(fill_color="black", back_color="white")

     img.save(f"results/{name}.png")