from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="horoscope_index"),
    path('type', views.get_info_about_types),
    path('type/<elem>', views.get_info_about_types_and_elements, name="types_name"),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name="horoscope_name"),

]