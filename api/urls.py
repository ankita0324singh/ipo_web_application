from django.urls import path
from .views import IndexView, IPOInfoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ipo_info', IPOInfoView.as_view(), name='ipo_info'),
]