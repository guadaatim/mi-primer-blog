from django.urls import path
from . import views


# asociamos una vista llamada post list a la url raiz
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
