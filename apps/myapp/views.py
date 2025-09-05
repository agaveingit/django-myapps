from django.shortcuts import render, HttpResponse
from .alat.konversi import Konverter
from .alat.kodeqr import GenerateQRCode

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
    file_type: str = None
    data: str = None
    qr_code = None
    qr = GenerateQRCode()
    if request.method =="POST":
        data: str = request.POST.get("data", "kosong") # Get data to create QR Code, "kosong" default
        file_type: str = request.POST.get("file_type", "png") # File type, "png" default
        if file_type == "png":
            qr_code = qr.qrcode_img(data)
        elif file_type == "svg":
            qr_code = qr.qrcode_svg(data)
    # else:
    #     data: str = "kosong"
    #     return "ERROR! Please try again"
    # I think I don't need this?

    return render(request, "myapp/qr_generator.html", {"qr_code": qr_code, "file_type": file_type})