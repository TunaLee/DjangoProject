from django.urls import path
from . import views

# url 주소
urlpatterns = [
    path('list/',views.board_list),
    path('write/',views.board_write)
]
