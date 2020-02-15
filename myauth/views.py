from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from myauth.models import MyUser, AuthSession
import time

# Create your views here.


class HomePage(View):

    def post(self, request):
        pass

    def get(self, request):
        context = {
            'username': None,
            'name':None
        }
        
        if request.myUserId:
            user = MyUser.objects.get(id=request.myUserId)
            context = {
                'username': user.username,
                'name': user.name,
            }
        return render(
            request,
            'myauth/profile.html',
            context
        )


class LoginPage(View):
    def get(self, request):
        return render(request, 'myauth/login.html')

    def post(self, request):
        pass


class LoginHandler(View):
    def get(self, request):
        pass

    def post(self, request):
        print(request.POST)
        login = request.POST.get('login')
        password = request.POST.get('password')

        user = MyUser.objects.get(username=login)
        print(user)
        if user.password == password:
            myHash = user.username + 'blblathisishash' + str(user.id) + str(time.time())
            AuthSession.objects.create(hash=myHash, myuserId=user.id)

        response = HttpResponse('response')
        response.set_cookie('myhash', myHash)
        return response
