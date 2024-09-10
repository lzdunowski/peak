from django.urls import path

from . import views

app_name = "nbpApiIntegration"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:currency_id>/", views.detail, name="detail"),
]
