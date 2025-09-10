import qrcode
import io
import base64
from qrcode.image.svg import SvgImage

class GenerateQRCode:
    def __init__(self):
        pass

    def qrcode_img(self, data: str) -> str:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        # img.save(filename)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return img_base64

    def qrcode_svg(self, data: str) -> str:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
        qr.add_data(data)
        qr.make(fit=True)
        svg = qr.make_image(image_factory=SvgImage)
        # img.save(filename)

        buffer = io.BytesIO()
        svg.save(buffer)
        svg_data = buffer.getvalue().decode()

        return svg_data