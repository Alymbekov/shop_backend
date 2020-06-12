from django.urls import path
from .views import UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
# ]

