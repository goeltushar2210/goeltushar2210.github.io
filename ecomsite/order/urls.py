from django.urls import path,include
from  order import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
]    