from django.shortcuts import render, redirect
from account.forms import UserForm
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import QueryDict
import json

def login_view(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        user_password = data.get('password')
        user = authenticate(request, username = user_id, password = user_password)


        if user is not None:
            login(request, user)
            return redirect('rueng_home')
        
def logout_view(request):
    logout(request)
    return redirect('rueng_home')
        
def signup(request):

    if request.method == 'GET':
        return render(request, 'account/signup.html')
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        request.POST = QueryDict('', mutable=True)
        request.POST.update(data)

        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    
    print(form)
    return render(request, 'account/login.html' ,{'form': form})
