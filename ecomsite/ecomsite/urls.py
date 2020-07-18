"""ecomsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  shop import views
from  order import views as OrderViews
from accounts import views as accountsviews
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth.views  import LogoutView
from django.views.generic import TemplateView

from accounts.views import  RegisterView,LoginView,Logout







urlpatterns = [
    path('',views.home, name='/'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contactus/',views.contactus, name='contactus'),
    path('shopcart/',OrderViews.shopcart, name='shopcart'), 
    path('profile/',accountsviews.profile, name='profile'), 

 
    path('admin/', admin.site.urls),
    path('order/',include('order.urls')),
    path('accounts/',include('accounts.urls')),
    # path('men/',views.men,name='men'),
    # path('women/',views.women,name='women'),
    # path('<int:id>/',views.detail, name='detail'),
    # path('checkout/',views.checkout, name='checkout'),

    path('category/<int:id>/<slug:slug>',views.category_products,name='category_products'),
    path('product/<int:id>/<slug:slug>',views.product_detail,name='product_detail'),    
    

  
    
    
    url (r'^register/$',RegisterView.as_view(),name='register'),
    url (r'^login/$',LoginView.as_view(),name='login'),
    url (r'^logout/$',Logout,name='logout'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
   
    
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

