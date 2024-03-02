from django.urls import path
from .views import HomePageView, AboutPageView, OrderPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('order/', OrderPageView.as_view(), name="order"),
]