from .views import (
    ProductListView,
    ProductDetailView, 
    ProductCreateView,
    ProductUpdateView
)
from django.urls import path


urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/<int:pk>/update/', ProductUpdateView.as_view()),
]

