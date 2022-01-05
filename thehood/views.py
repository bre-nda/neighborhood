from django.shortcuts import render, redirect
from django.http  import HttpResponse

from thehood.models import Profile
from .forms import ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        
    context = {
        'u_form' : u_form,
        'p_form' : p_form,

    }
    return render(request,'profile.html',context)

