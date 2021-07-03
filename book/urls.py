from django.urls import path
from .views import showslot

urlpatterns = [
    path('', showslot),
]
