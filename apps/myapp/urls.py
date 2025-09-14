from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("konversi/", views.konversi, name="konversi"),
    path("qrgen/", views.qr_gen, name="qrgen"),
]