from django.urls import path
from .views import FirstApiView

urlpatterns = [
    path('', FirstApiView.as_view()),
]