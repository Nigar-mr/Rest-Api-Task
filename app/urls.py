from django.urls import path
from .views import Stock, Product, Sale

urlpatterns = [
    path('category/', Stock.as_view()),
    path('products/<int:id>/', Product.as_view()),
    path('products/', Product.as_view()),
    path('sale/<str:name>/', Sale.as_view())
]
