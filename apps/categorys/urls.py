from django.urls import path
from .views import (
    CategoryListView,
)

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    # path('category/create/', CategoryCreateView.as_view()),
]
