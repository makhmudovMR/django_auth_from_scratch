from django.urls import path
from myauth.views import HomePage, LoginPage, LoginHandler

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login', LoginPage.as_view(), name='login'),
    path('loginhandler', LoginHandler.as_view(), name='login_handler')
]
