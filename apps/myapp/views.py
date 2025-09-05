from django.shortcuts import render, HttpResponse
from .alat.konversi import Konverter
from .alat.kodeqr import generate_qrcode

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
    data: str = None
    qr_code = None
    if request.method == "POST":
        data: str = request.POST.get("data", "kosong")
        qr_code = generate_qrcode(data)
    else:
        data: str = "kosong"

    return render(request, "myapp/qr_generator.html", {"qr_code": qr_code})