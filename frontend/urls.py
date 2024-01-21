from django.urls import path
from .views import *
# urls.py
urlpatterns = [
    path("",home,name='home'),
    path('show_image/<path:image_url>/', show_image, name='show_image'),
    path('download_image/<str:image_url>/', download_image, name='download_image'),
    # path("test",test,name='test'),
    # path("about",about,name='about'),
    # path("disclaimer",disclaimer,name='disclaimer'),
    # path("contact",contact,name='contact'),
    # path("services",services,name='services'),
    # path("terms",terms,name='terms'),
    # path("disclaimer",disclaimer,name='disclaimer'),
    # path("privacypolicy",privacypolicy,name='privacypolicy'),
    # path("refundpolicy",refundpolicy,name='refundpolicy'),
]
