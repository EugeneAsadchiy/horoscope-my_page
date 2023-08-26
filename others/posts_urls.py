
from django.urls import path, include
from . import views
urlpatterns = [
    path('<int:number_post>/', views.inf_about_post_number),
    path('<str:name_post>/', views.inf_about_post_name),

    # path('leo/', views.leo),
    # path('aries/', views.aries),
    # path('taurus/', views.taurus),
]