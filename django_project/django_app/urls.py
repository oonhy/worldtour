from django.urls import path
from .views import index

urlpatterns=[
    path('', index, name="index"), #쉼표 빼면 오류발생
]