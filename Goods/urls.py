from django.urls import path, include
from Goods import views
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
     path('lending/', views.lending_page, name='lending_page'),
]

