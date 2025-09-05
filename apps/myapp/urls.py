from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("konversi/", views.konversi, name="konversi"),
    path("qr_generator/", views.qr_generator, name="qr_generator"),
    # path("qr_download/", views.qr_download, name="qr_download"),
]