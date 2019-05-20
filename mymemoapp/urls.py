from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name = 'detail'),
    path('delete/<int:id>', views.delete, name = 'delete'),
]