from django.urls import path
from .views import CartDetailView, CartItemView


urlpatterns = [
    path('cartitem/', CartDetailView.as_view()),
    path('cartitem/create/', CartItemView.as_view()),
    path('cartitem/<int:pk>/', CartDetailView.as_view()),
]