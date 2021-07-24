from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from .models import CustomUser
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            login(request, user)
        else:
            if CustomUser.objects.filter(username = request.POST['username']).exists():
                messages.info(request, '비밀번호가 틀렸습니다.')
                return redirect('urllogin')
            else:
                messages.info(request, '존재하지 않는 계정입니다.')
                return redirect('urllogin')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'lf':form})

def logout_view(request):
    logout(request)
    return redirect('urlhome')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        else:
            if CustomUser.objects.filter(username = request.POST['username']).exists():
                messages.info(request, '중복된 아이디가 있습니다.')
                return redirect('urlsignup')
            
            elif request.POST['password1'] != request.POST['password2']:
                messages.info(request, '비밀번호와 비밀번호 확인이 일치하지 않습니다.')
                return redirect('urlsignup')

            elif len(request.POST['password1']) < 8:
                messages.info(request, '비밀번호는 8자리 이상으로 작성해주세요.')
                return redirect('urlsignup')

            elif request.POST['password1'].isdigit():
                messages.info(request, '비밀번호는 숫자로만 이루어질 수 없습니다')
                return redirect('urlsignup')

            elif request.POST['username'] in request.POST['password1']:
                messages.info(request, '비밀번호에 아이디가 포함될 수 없습니다')
                return redirect('urlsignup')

            else:
                messages.info(request, '알 수 없는 에러입니다. 관리자 문의')
                return redirect('urlsignup')
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'sf':form})