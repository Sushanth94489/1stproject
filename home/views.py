from django.shortcuts import render
from django.contrib.auth.hashers import check_password, make_password
from .models import User


def index(request):
    return render(request, "home/index.html")
def reg(request):
    if request.method != "POST":
        return render(request,"home/index.html")
    first_name=request.POST.get('first_name','').strip()
    last_name=request.POST.get('last_name','').strip()
    username=request.POST.get('username','').strip()
    email=request.POST.get('email','').strip()
    phone_no=request.POST.get('phno','').strip()
    password=request.POST.get('pass','').strip()
    confirm_password=request.POST.get('cpass','').strip()
    if not first_name or not last_name or not username or not email or not phone_no or not password:
        return render(request,"home/index.html",{"error":"Please Enter Fields"})
    if password != confirm_password:
        return render(request,"home/index.html",{"error":"Password Mismatch"})
    user=User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        phone_no=phone_no,
        password=make_password(password),
    )
    user.save()
    return render(request,"home/login.html")
def log(request):
    if request.method != "POST":
        return render(request,"home/login.html")
    username=request.POST.get('username1','')
    password=request.POST.get('password1','')
    if not username or not password:
        return render(request,"home/login.html",{"error":"Please Enter Fields"})
    user=User.objects.filter(username=username).first()
    if not user:
        return render(request,"home/login.html",{"error":"incorrect username or password"})
    if check_password(password, user.password):
        return render(request, "home/home.html")
    return render(request,"home/login.html",{"error":"incorrect username or password"})
def home(request):
    return render(request,"home/home.html")