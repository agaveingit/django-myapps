from django.shortcuts import render, HttpResponse
from .alat.konversi import Konverter
from .alat.kodeqr import GenerateQRCode
import io
import base64

# Create your views here.
def home(request):
    return render(request, "myapp/home.html")

def konversi(request):
    result: str = None
    error: str = None
    if request.method == "POST":
        angka = request.POST.get("angka")
        konversi_angka = Konverter()
        try:
            angka: int = int(angka)
            result: str = konversi_angka.konversi(angka)
        except (ValueError, TypeError):
            error: str = "Error! Harus masukan angka."

    return render(request, "myapp/konversi.html", {"result": result, "error": error})

def qr_generator(request):
    qr = GenerateQRCode()
    qr_code = None
    data: str = None
    file_type: str = None
    action: str = None
    if request.method =="POST":
        data: str = request.POST.get("data", "kosong") # Get data to create QR Code, "kosong" default
        file_type: str = request.POST.get("file_type", "png") # File type, "png" default
        action: str = request.POST.get("action")
        if action == "preview":
            if file_type == "png":
                qr_code = qr.qrcode_img(data)
            elif file_type == "svg":
                qr_code = qr.qrcode_svg(data)
        elif action == "download":
            if file_type == "png":
                img_base64 = qr.qrcode_img(data)
                img_bytes = base64.b64decode(img_base64)
                response = HttpResponse(img_bytes, content_type="image/png")
                response["Content-Disposition"] = 'attachment; filename="qr_code.png"'
                return response            
            elif file_type == "svg":
                svg_data = qr.qrcode_svg(data)
                response = HttpResponse(svg_data, content_type="image/svg+xml")
                response["Content-Disposition"] = 'attachment; filename="qr_code.svg"'
                return response

    return render(request, "myapp/qr_generator.html", {
        "qr_code": qr_code,
        "file_type": file_type,
        "data": data,
        "action": action,
    })