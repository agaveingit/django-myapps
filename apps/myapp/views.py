from django.shortcuts import render, HttpResponse
from .konversi import teks_dari_angka

# Create your views here.
def home(request):
    return render(request, "home.html")
    # return HttpResponse("hi")

def konversi(request):
    result = None
    error = None

    if request.method == "POST":
        angka = request.POST.get("angka")
        try:
            angka = int(angka)
            result = teks_dari_angka(angka)
        except (ValueError, TypeError):
            error = "Error! Harus masukan angka."

    return render(request, "konversi.html", {"result": result, "error": error})