from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_nft, name='lista_nfts'),
path('login/', views.login, name="login"),
]