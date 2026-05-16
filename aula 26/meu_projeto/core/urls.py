from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path('criar/', views.criar),

    path('editar/<int:id>/', views.editar),

    path('deletar/<int:id>/', views.deletar),

]