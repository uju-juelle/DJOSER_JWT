from django.urls import path
from .views import *


urlpatterns = [
    path("", apihomepage.as_view(), name="home"),
    path("<uuid:id>/", detailpage.as_view(), name="detail")
]