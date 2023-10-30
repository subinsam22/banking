from django.urls import path
from . import views
app_name='bankapp'
urlpatterns = [
    path('',views.test,name='home'),
    path('get_items/<int:district_id>/', views.get_items, name='get_items'),
    path('add/',views.add_application,name='add'),
    path('details/',views.details_application,name='details'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('confirm/',views.confirmation,name='confirm'),
    ]