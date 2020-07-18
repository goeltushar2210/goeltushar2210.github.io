from django.db import models
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.urls import reverse

class Category(MPTTModel):
    STATUS = (
        ('T', 'T'),
        ('F','F'),
        
    )
    parent       = TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    title       = models.CharField(max_length=50)
    description  = models.TextField(blank=True,max_length=50)
    image        = models.ImageField(blank=True,upload_to='images/')
    status       = models.CharField(max_length=20,choices=STATUS )
    slug         = models.SlugField(null=False,unique=True)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now=True )

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})      

    def __str__(self):
        full_path = [self.title]
        k =  self.parent     
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])    


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False','False'),
    )    
    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),   
    )
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)    #many to one relation with Category
    title           = models.CharField(max_length=50)
    price           = models.FloatField(max_length=50,default=0.00)
    discount_price  = models.FloatField(max_length=50,default=0.00)
    Quantity          = models.FloatField(default=0.00)
    description     = RichTextUploadingField()
    image           = models.ImageField(upload_to='images/')
    variant         = models.CharField(max_length=10,choices=VARIANTS, default='None')
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    status          = models.CharField(max_length=10, choices=STATUS)  
    slug            = models.SlugField(null=False,unique=True)
    create_at       = models.DateTimeField(auto_now_add=True)
    update_at       = models.DateTimeField(auto_now=True )
    
    def __str__(self):
        return self.title
    

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description= 'Image'

    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})      


class Images(models.Model):
    product         = models.ForeignKey(Product,on_delete=models.CASCADE)         #many to one ration with Product
    titlec          = models.CharField(max_length=50,blank=True)
    image           = models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.titlec


