from django.urls import path
from webApp import views

# Template URLS
app_name = 'webApp'

urlpatterns = [
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login')
]
