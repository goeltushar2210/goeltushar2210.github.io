from django.contrib import admin
from .models import *


#Register your models here.

class User_MessageAdmin(admin.ModelAdmin):                # manage category at database
    list_display = ['name','subject','update_at','status']    
    readonly_fields  = ('name','subject','email','message','ip',)
    list_filter =['status']

# admin.site.register(Products_Men)
# admin.site.register(Products_Women)
admin.site.register(Order)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(User_Message,User_MessageAdmin)




