from django.shortcuts import render, HttpResponse
from .alat.konversi import Konverter
from .alat.loading_gimmick import Loading

# Create your views here.
def home(request):
    return render(request, "myapp/home.html")

def konversi(request):
    if request.method == "POST":
        angka = request.POST.get("angka")
        konversi_angka = Konverter()
        try:
            angka: int = int(angka)
            result: str = konversi_angka.konversi(angka)    
            error: str = None
        except (ValueError, TypeError):
            result: str = None
            error = "Error! Harus masukan angka."

    return render(request, "myapp/konversi.html", {"result": result, "error": error}) 

def qr_generator(request):
    pass