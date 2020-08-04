from django.urls import path
from . import views

# url 주소
urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
]
