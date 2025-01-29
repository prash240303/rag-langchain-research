from django.urls import path
from transcriber.views import TranscriberView

urlpatterns = [
    path('transcribe/', TranscriberView, name='transcribe'),
]
