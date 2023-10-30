from django.urls import path
from . import views
app_name='authen'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('logout/',views.logout,name='logout'),
    ]