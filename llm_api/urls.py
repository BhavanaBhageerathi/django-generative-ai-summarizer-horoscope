from django.urls import path
from .views import horoscope, summarize

urlpatterns = [
    path('summarize/', summarize),
    path('horoscope/', horoscope)
     ]