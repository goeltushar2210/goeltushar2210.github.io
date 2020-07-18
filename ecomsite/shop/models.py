from django.db import models
from django.core.validators import RegexValidator
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import  RichTextUploadingField
from django import forms
from django.forms import ModelForm,BaseModelForm
from django.contrib.auth.models import User
from accounts.models import User


# Create your models here.

# class Products_Men(models.Model):
#     title           = models.CharField(max_length=50)
#     price           = models.CharField(max_length=50)
#     discount_price  = models.CharField(max_length=50)
#     category        = models.CharField(max_length=50)
#     description     = models.TextField()
#     image           = models.ImageField(upload_to='men')
#     featured        = models.BooleanField(default=False)
#     active          = models.BooleanField(default=True)
   


# class Products_Women(models.Model):
#     title           = models.CharField(max_length=50)
#     price           = models.CharField(max_length=50)
#     discount_price  = models.CharField(max_length=50)
#     category        = models.CharField(max_length=50)
#     description     = models.TextField()
#     image           = models.ImageField(upload_to='women')
#     featured        = models.BooleanField(default=False)
#     active          = models.BooleanField(default=True)




class Order(models.Model):
    items        = models.CharField(max_length=500)
    name         = models.CharField(max_length=50)
    email        = models.CharField(max_length=50)
    phone_regex  = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone        = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    address      = models.CharField(max_length=500)
    city         = models.CharField(max_length=50)
    state        = models.CharField(max_length=50)
    zipcode      = models.CharField(max_length=10)
    total        = models.CharField(max_length=50)
   

    



class About(models.Model):
    name    = models.CharField(blank=True,max_length=255)

    aboutus  = RichTextUploadingField()
    def __str__ (self):
        return self.name
   

class Contact(models.Model):
    name    = models.CharField(blank=True,max_length=255)
    
    contactus  = RichTextUploadingField()
    def __str__ (self):
        return self.name
    
class User_Message(models.Model):
    STATUS = (
        ('New','New'),
        ('Read', 'Read'),
        ('Closed','Closed'),
    )
    name      = models.CharField(blank=True,max_length=100)
    email     = models.CharField(blank=True,max_length=100)
    subject   = models.CharField(blank=True,max_length=100)
    message  = models.TextField(blank=True,max_length=255)
    status    = models.CharField(max_length=100,choices=STATUS,default=True)
    ip        = models.CharField(blank=True,max_length=50)
    note      = models.CharField(blank=True,max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name

class User_Form(ModelForm):
    
    class Meta:
        model = User_Message
        fields =['name','email','subject','message']
        widgets ={
            'name'  : forms.TextInput(attrs={'classs': 'input','placeholder':'Name & Surname'}),
            'subject'  : forms.TextInput(attrs={'classs': 'input','placeholder':'Subject'}),
            'email'  : forms.TextInput(attrs={'classs': 'input','placeholder':'Email Address'}),
            'message'  : forms.Textarea(attrs={'classs': 'input','placeholder':'Your Message','rows':'5'}),

        }
       

        

   
