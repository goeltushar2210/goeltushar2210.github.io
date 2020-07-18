from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, get_user_model,logout
from django.http import HttpResponse
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView
from django.contrib import messages
from accounts.models import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.models import *




from .forms import *

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/shop:home/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        next = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=email, password=password)
        if user is not None:
            login(request, user)
            
            if is_safe_url(redirect_path, request.get_host()):
                
                return redirect(redirect_path)
            else: 
                             
                return redirect("/")
        messages.warning(request,"Login Error !! Username or Password is incorrect")          
        return super(LoginView, self).form_invalid(form) 
        
                         


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url= '/login/'


def Logout(request): 
                                                         #logout
        logout(request)
        return redirect('/')



@login_required(login_url='/login') # Check login
def profile(request):
    #category = Category.objects.all()
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {#'category': category,
               'profile':profile}
    return render(request,'accounts/profile.html',context)
   
    
            
           