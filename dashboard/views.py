from login.models import Faculty, Student
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from google.auth.transport import Request
from dashboard.models import *
import api.gparser as g
# Create your views here.
def checklogin(request):
    if(request.session.get('islogin')is not None):
        return True
    else:
        return False
def index(request):
    if checklogin(request):
        if(request.session.get('role')=='student'):
            return render(request,'dashboard-student.html')
        else:
            return render(request,'dashboard-faculty.html')
    else:
        return redirect("/login/")
def SyllabusFeed(request):
    if not checklogin(request):
        return redirect("/login/")
    else:    
        if request.method == 'POST':
            subcode=request.POST.get('subcode').upper()
            key=request.POST.get('key')
            unit=request.POST.get('unit_no')
            if(len(syllabusfeed.objects.filter(subcode_id=subcode,unit_no=unit))==0 ):
                syllabusfeed.objects.create(subcode_id=subcode,key=key,unit_no=unit)
                return HttpResponse("<a href=\"\\dashboard\\\">go back</a>")
            else:
                return HttpResponse("already entered")
        else:
            return render(request,'syllabusfeed.html')
def SubjectFeed(request):
    if not checklogin(request):
        return redirect("/login/")
    else: 
        if request.method == 'POST':
            subcode=request.POST.get('subcode').upper()
            subject=request.POST.get('subject')
            dept=request.POST.get('dept')
            sem=request.POST.get('sem')
            if(len(subjects.objects.filter(subcode=subcode))==0 ):
                subjects.objects.create(subcode=subcode,subject=subject,dept=dept,sem=sem)
                return HttpResponse("<a href=\"\\dashboard\\\">go back</a>")
            else:
                return HttpResponse("already entered")
        else:
            return render(request,'subjectfeed.html')

def clearses(request):
    del request.session['islogin']
    del request.session['role']
    del request.session['uid']
    return redirect('/dashboard/')

def search(request):
    if not checklogin(request):
        return redirect('/login/')
    else:
        if(request.method=='POST'):
            q=request.POST.get('searchq')
            data=g.getData(q)
            return render('searchresult.html',data)
        else:
            return redirect('/dashboard/')

def profile(request):
    if not checklogin(request):
        return redirect("/login/")
    uid=request.session['uid']
    if(uid[:2]=='vh'):
        data=Student.objects.filter(uid=uid).values('uid','gender','phno','email')
        return render(request,'profile.html',{'data':data[0]})
    else:
        data=Faculty.objects.filter(uid=uid).values('uid','gender','phno','email')
        print(data[0])
        return render(request,'profile.html',data[0])