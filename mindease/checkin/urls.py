from django.urls import path
from .views import daily_checkin, success, dashboard

urlpatterns = [
    path('', daily_checkin, name='checkin'),
    path('success/', success, name='success'),
    path('dashboard/', dashboard, name='dashboard'),
]
