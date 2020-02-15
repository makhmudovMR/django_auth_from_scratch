from django.contrib import admin
from myauth.models import AuthSession, MyUser

# Register your models here.

admin.site.register(AuthSession)
admin.site.register(MyUser)