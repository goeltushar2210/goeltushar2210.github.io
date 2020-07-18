from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser , BaseUserManager
)
from django.utils.safestring import mark_safe

class UserManager(BaseUserManager):
    def create_user(self, email,first_name=None,last_name=None,password=None, is_active=True, is_staff=False, is_admin=False): # Any required field add into this
        if not email:
            raise ValueError("Users must have an Email Address")
        if not password:
            raise ValueError("Users must have a Password")  
              
        user_obj = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name = last_name,
        )    
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj


    def create_staffuser(self, email, first_name=None,last_name=None,password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email,first_name=None,last_name=None, password=None):
         user = self.create_user(
             email,
             first_name=first_name,
             last_name=last_name,
             password=password,
             is_staff=True,
             is_admin=True
         )
         return user    

class User(AbstractBaseUser):
    email     = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)    
    active    = models.BooleanField(default=True)  # can login
    staff     = models.BooleanField(default=False) # staff user non super
    admin     = models.BooleanField(default=False) # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'  #Username
    REQUIRED_FIELDS = []              #add full name to user form

    obejcts = UserManager()

    

    def __str__(self):
        return self.email
    
    def get_first_name(self):
        if self.first_name:
            return self.first_name
        return self.email

    def get_last_name(self):
        return self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True    

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True,upload_to='images/users/')
    

    def __str__(self):
        return self.user.first_name


    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name 
        
    