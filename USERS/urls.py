# USERS/urls.py

from django.urls import path
from . import views
app_name = 'USER'  # Namespace for the app
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('enduser_dash/', views.enduser_dash, name='enduser_dash'),
    path('login/', views.customer_login, name='customer_login'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('event_booking/', views.event_booking, name='event_booking'),
    
    path('payment/<int:event_id>/', views.payment_page, name='payment_page'),
    
]
