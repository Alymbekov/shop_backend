from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(title='Shop Backend')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.categorys.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    path('api/v1/', include('apps.products.urls')),
    path('api/v1/', include('apps.authentication.urls')),
    path('api/v1/documentation/', include_docs_urls(title='Shop Backend')),
    path('api/v1/schema/', schema_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
