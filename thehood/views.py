from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse

from thehood.models import Business, NeighbourHood, Post, Profile
from .forms import ProfileUpdateForm,UserUpdateForm,NeighbourHoodForm,PostForm,BusinessForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime as dt
# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
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

def hoods(request):
    hoodss = NeighbourHood.objects.all()
    hoodss = hoodss[::-1]
    params = {
        'hoodss': hoodss,
    }
    return render(request, 'hoods.html', params)

def single_hood(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    params = {
        'hood': hood,
        'business': business,
        'posts': posts
    }
    return render(request, 'single.html', params)

def new_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'new.html', {'form': form})

def business(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.hood = hood
            biz.user = request.user.profile
            biz.save()
            return redirect('single-hood', hood.id)
    else:
         form = BusinessForm()
    return render(request, 'biz.html', {'hood':hood,'business':business,'form': form,})

def news(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    posts = Post.objects.filter(hood=hood)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
         form = PostForm()
    return render(request, 'news.html', {'hood':hood,'posts':posts,'form': form})

def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url='/accounts/login/')
def businesses(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    return render(request, 'business.html', {'business': business})

def post(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    post = Post.objects.filter(hood=hood)
    return render(request, 'post.html', {'post': post})

def search_results(request):
    if 'query' in request.POST and request.GET['query']: 
        search = request.GET.get('query')
        search_business= Business.search_by_title(search)
        messages= f'{search}'
        context = {"message":messages,"businesses":search_business}
        
        return render(request,'search.html',context)

    else:
        message="You haven't searched for any item"
        return render(request,'search.html',{"message":message}) 
