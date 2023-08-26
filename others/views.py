from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def get_rectangle_area(request, width, height):
    answer = width * height
    # return HttpResponse(f"Плошадь прямоугольника размером {width}x{height} = {answer}")
    return render(request, "others/rectangle.html")


def get_square_area(request, width):
    # return HttpResponse(f"Площадь квадрата размером {width}x{width}= {width ** 2}")
    return render(request, "others/square.html")


def get_circle_area(request, radius):
    pi = 3.14
    # return HttpResponse(f"Площадь круга радиуса {radius} равна {(radius ** 2) * pi}")
    return render(request, "others/circle.html")


def inf_about_post_name(request, name_post):
    return HttpResponse(f"Информация о посте {name_post}")


def inf_about_post_number(request, number_post):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")
