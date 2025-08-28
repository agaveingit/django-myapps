from django.shortcuts import render, HttpResponse
from .alat.konversi import Konverter

# Create your views here.
def home(request):
    return render(request, "home.html")

def konversi(request):
    result = None
    error = None
    if request.method == "POST":
        angka = request.POST.get("angka")
        konversi_angka = Konverter()
        try:
            angka = int(angka)
            result = konversi_angka.konversi(angka)
        except (ValueError, TypeError):
            error = "Error! Harus masukan angka."

    return render(request, "konversi.html", {"result": result, "error": error})