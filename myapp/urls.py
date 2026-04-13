from django.urls import path
from . import views
app_name = 'myapp'

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:id>/', views.details, name ='details'),
        path('friends/', views.friends, name='friends'),
        path('add/', views.create_item, name='create_item'),
    ]