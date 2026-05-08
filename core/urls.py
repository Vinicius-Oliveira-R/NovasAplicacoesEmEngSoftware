from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),
]
