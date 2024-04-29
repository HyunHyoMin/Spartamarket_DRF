from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:productId>/', views.ProductList.as_view()),
]
