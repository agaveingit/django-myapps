from django.shortcuts import render, HttpResponse
from utils.KonverterAngka import Konverter
from utils.QRGenerator import GenerateQRCode
import io

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
            result: str = konversi_angka.konverter(angka)
        except (ValueError, TypeError):
            error: str = "Error! Harus masukan angka."

    return render(request, "myapp/konversi.html", {"result": result, "error": error})

def qr_gen(request):
    qr = GenerateQRCode()
    qr_code = None
    data: str = None
    file_type: str = None
    action: str = None
    if request.method =="POST":
        """
        qrgen.html input name='data' give 'string' or empty default is empty
        qrgen.html select name='file_type' give 'png' or 'svg' default is 'png'
        """
        data: str = request.POST.get("data", "kosong")
        file_type: str = request.POST.get("file_type", "png")
        action: str = request.POST.get("action")
        if action == "preview":
            if file_type == "png":
                qr_code = qr.qrcode_img(data)
            elif file_type == "svg":
                qr_code = qr.qrcode_svg(data)
        elif action == "download":
            if file_type == "png":
                img = qr.download_qrcode_img(data) 
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                response = HttpResponse(buffer.getvalue(), content_type="image/png")
                response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
                return response
            elif file_type == "svg":
                svg_data = qr.qrcode_svg(data)
                response = HttpResponse(svg_data, content_type="image/svg+xml")
                response['Content-Disposition'] = 'attachment; filename="qrcode.svg"'
                return response
    return render(request, "myapp/qrgen.html", {
        "qr_code": qr_code,
        "file_type": file_type,
        "data": data,
        "action": action,
})

"""
Now I Know, so here is the reason about unexpected behaviour, note for myself tommorow
When you pass a data, and you clik the preview. The input would be cleared and when you try 
to download you don't get your current qrcode instead the default value 'kosong'.

So my strategy? Try to preserve the input so when you download you get what you want.

What about SVG? It works now its not just blank my friend instead it return literal strings 😂😫.
"""