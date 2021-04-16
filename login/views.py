from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse
# Create your views here.
from .models import *
def login(request):
    return render(request,'login.html')

def cklogin(request):
    print(request.method)
    if request.method=='POST':
        uid=request.POST.get('uid').lower()
        pwd=request.POST.get('pwd')
        if uid[2:]=='vh':
            data=Student.objects.filter(uid=uid).values('uid','password')
            if(len(data!=0)):
                data=data[0]
                if(data['uid']==uid and data['pwd'] == pwd):
                    return HttpResponse("loggedin")
                else:
                    return redirect(login,{'script':"<script>alert(\"wrong username or password\")</script>"})
            else: 
                return redirect(login,{'script':"<script>alert(\"wrong username or password\")</script>"})
        elif uid[3:]=='hts':
            data=Faculty.objects.filter(uid=uid).values('uid','password')
            if(len(data!=0)):
                data=data[0]
                if(data['uid']==uid and data['pwd'] == pwd):
                    return HttpResponse("loggedin")
                else:
                    return redirect(login,{'script':"<script>alert(\"wrong username or password\")</script>"})
            else: 
                return redirect(login,{'script':"<script>alert(\"wrong username or password\")</script>"})
        else:
            return redirect(login)
    return HttpResponse("not post method find why") 