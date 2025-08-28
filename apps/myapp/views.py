from django.shortcuts import render, HttpResponse
from .alat.konversi import Konverter

# Create your views here.
def home(request):
    return render(request, "home.html")
    # return HttpResponse("hi")

def konversi(request):
    result = None
    error = None
    # Di sini ada unexpected behaviour, 
    # di mana result menunjukan none
    # menghasilkan result tidak tampil di browser
    # tapi pesan error muncul
    # TODO: Beresin ni error
    if request.method == "POST":
        angka = request.POST.get("angka")
        konversi_angka = Konverter()
        try:
            angka = int(angka)
            result = konversi_angka.konversi(angka)
        except (ValueError, TypeError):
            error = "Error! Harus masukan angka."
    print(result, error)

    return render(request, "konversi.html", {"result": result, "error": error})