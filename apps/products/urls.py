from .views import (
    ProdictListView, 
    ProductDetailView, 
#    ProductCreateView,
)
from django.urls import path


urlpatterns = [
    path('product/', ProdictListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
#    path('product/create/', ProductCreateView.as_view()),
]

