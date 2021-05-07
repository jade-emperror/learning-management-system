from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse
# Create your views here.
from .models import *
def login(request):
    return render(request,'login.html')

def cklogin(request):
    if request.method == 'POST':
        uid=request.POST.get('uid').lower()
        pwd=request.POST.get('pwd')
        if uid[:2]=='vh':
            data=Student.objects.filter(uid=uid).values('uid','password')
            if(len(data)!=0):
                data=data[0]
                if(data['uid']==uid and data['password'] == pwd):
                    request.session['islogin']=True
                    request.session['role']='student'
                    request.session['uid']=uid
                    #return redirect("/dashboard/")
                    return redirect("/dashboard/")
                else:
                    return render(request,'login.html',{'script':"Invalid Username or password"})
                    #return redirect('',{'script':"Invalid Username or password"})
            else:
                return render(request,'login.html',{'script':"Invalid Username or password"}) 
                #return redirect(login#,{'script':"<span class="error">Invalid Username or password</span>"})
        elif uid[:3]=='hts':
            data=Faculty.objects.filter(uid=uid).values('uid','password')
            if(len(data)!=0):
                data=data[0]
                if(data['uid']==uid and data['password'] == pwd):
                    request.session['islogin']=True
                    request.session['role']='faculty'
                    request.session['uid']=uid
                    return redirect("/dashboard/")
                else:
                    return render(request,'login.html',{'script':"Invalid Username or password"})
                    #return redirect(login#,{'script':"<span class="error">Invalid Username or password</span>"})
            else: 
                return render(request,'login.html',{'script':"Invalid Username or password"})
                #return redirect(login#,{'script':"<span class="error">Invalid Username or password</span>"})
        else:
            return render(request,'login.html',{'script':"Invalid Username or password"})
            #return redirect(login)
    else:
        return HttpResponse("fucked up for sure")