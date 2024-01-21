from django.urls import path
from .views import *
# urls.py
urlpatterns = [
    path("getdata",getdata,name='getdata'),
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
