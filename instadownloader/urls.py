from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('instagramadmin/', admin.site.urls),
    path('api-v1/', include('backend.urls')),
    path('', include('frontend.urls')),
]
