from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django import forms
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView
from product.models import *
import json



# Create your views here.

# def men(request):
#     product_objects = Products_Men.objects.all()

#     # Paginator Code

#     paginator = Paginator(product_objects,9)
#     page = request.GET.get('page')
#     product_objects = paginator.get_page(page)

#     return render(request,'shop/men.html',{'product_objects':product_objects})
    
# def women(request):
#     product_objects = Products_Women.objects.all()

#     # Paginator Code

#     paginator = Paginator(product_objects,9)
#     page = request.GET.get('page')
#     product_objects = paginator.get_page(page)

#     return render(request,'shop/women.html',{'product_objects':product_objects})




    
#     # Detail view code

# def detail(request,id):
#     product_object = Products_Men.objects.get(id=id)

#     return render(request,'shop/detail.html',{'product_object':product_object})

    


            #check out view



def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,phone=phone,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save() 

    return render(request,'shop/checkout.html')


def home(request):
    
    category       = Category.objects.all()           
    product_latest = Product.objects.all().order_by('-id')[:4]       #last 4   products
    product_picked = Product.objects.all().order_by('?')[:4]         #Random 4 products
    page = "home"
    context = {'category':category,'product_latest':product_latest,'product_picked':product_picked}    
    return render(request,'shop/home.html',context)
    
 


def category_products(request,id,slug):
    category       = Category.objects.all()    
    products       = Product.objects.filter(category_id=id)
    paginator = Paginator(products,9)
    page = request.GET.get('page')
    products = paginator.get_page(page)     
    context = {'products':products,'category':category}
    return render(request,'shop/category_products.html',context)





def aboutus(request):
    about = About.objects.get()
    return render(request,'shop/aboutus.html',{'about':about})

def contactus(request):
    if request.method == 'POST':
        form =User_Form(request.POST)
        if form.is_valid():
            data = User_Message()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Your mesaage has been sent to Awfy Team. Thankyou for Intrest ")
            return HttpResponseRedirect('/contactus')
    

    contact =Contact.objects.get()
    form = User_Form
    context ={'contact':contact,'form':form}   
    return render(request,'shop/contactus.html',context)


                                 # Product detail

def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {'product': product,'category': category,'images': images}               
    return render(request,'shop/product_detail.html',context)           
            
