import qrcode

def generate_qrcode(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

teks = "coba"
namafile = "test.png"
generate_qrcode(teks, namafile)
if generate_qrcode:
    print(f"done")