from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 인증&권한:AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST": # 저장
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        
    else : # 입력할 수 있는 폼
        form = CustomUserCreationForm()
    return render(request,"accounts/form.html",{"form":form})
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("posts:list")
    else :
        form = AuthenticationForm()
    
    return render(request,"accounts/form.html", {"form":form})

def logout(request):
    auth_logout(request)
    return redirect("posts:list")
    
    
def user_page(request, id):
    User = get_user_model()
    user_info = User.objects.get(id=id)
    return render(request, 'accounts/user_page.html',{'user_info':user_info})
    
@login_required
def follow(request, id):
    User = get_user_model()
    me = request.user
    you = User.objects.get(id=id)
    if me != you:
        if you in me.followings.all():
            #취소 버튼
            me.followings.remove(you)
            
        else:
            #추가버튼
            me.followings.add(you)
    
    return redirect('accounts:user_page', id)
    
    
@login_required
def edit_profile(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    me = request.user
    if me == user:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance = user)
            if form.is_valid():
                form.save()
                return redirect('accounts:user_page', id)
        else:
            form = CustomUserChangeForm(instance = user)
        return render(request, 'accounts/form.html', {'form':form})
    else:
        return redirect('posts:list')
        
    


