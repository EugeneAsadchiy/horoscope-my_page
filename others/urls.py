
from django.urls import path, include
from . import views
urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area),
    path('square/<int:width>/', views.get_square_area),
    path('circle/<int:radius>/', views.get_circle_area),
    path('posts/', include("others.posts_urls"))

    # path('leo/', views.leo),
    # path('aries/', views.aries),
    # path('taurus/', views.taurus),
]