from django.shortcuts import render, HttpResponse
from .konversi import konverter

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
            result = konverter(angka)
        except (ValueError, TypeError):
            error = "Error! Harus masukan angka."
    print(result, error)

    return render(request, "konversi.html", {"result": result, "error": error})