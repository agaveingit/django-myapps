from django.shortcuts import render, HttpResponse
from .utils.KonverterAngka import Konverter
from .utils.QRGenerator import GenerateQRCode, QRCodeDataError
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

    return render(request, "myapp/konversi.html", {
        "result": result, 
        "error": error
})

def _create_png_response(qr_generator, data):
    img = qr_generator.download_qrcode_img(data)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    response = HttpResponse(buffer.getvalue(), content_type="image/png")
    response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
    return response

def _create_svg_response(qr_generator, data):
    svg_data = qr_generator.qrcode_svg(data)
    response = HttpResponse(svg_data, content_type="image/svg+xml")
    response['Content-Disposition'] = 'attachment; filename="qrcode.svg"'
    return response

def qr_gen(request):
    context = {
        "qr_code": None,
        "file_type": "png",
        "data": None,
        "action": None,
        "error": None,
        "png_selected": "selected", # Default selection
        "svg_selected": "",
    }

    if request.method == "POST":
        qr = GenerateQRCode()
        data = request.POST.get("data")
        file_type = request.POST.get("file_type", "png")
        action = request.POST.get("action")

        context.update({"data": data, "file_type": file_type, "action": action})
        
        # Update selection based on POST data
        context["png_selected"] = "selected" if file_type == "png" else ""
        context["svg_selected"] = "selected" if file_type == "svg" else ""

        try:
            if action == "preview":
                context["qr_code"] = qr.qrcode_img(data)
            elif action == "download":
                if file_type == "png":
                    return _create_png_response(qr, data)
                elif file_type == "svg":
                    return _create_svg_response(qr, data)
        except QRCodeDataError as e:
            context["error"] = str(e)

    return render(request, "myapp/qrgen.html", context)