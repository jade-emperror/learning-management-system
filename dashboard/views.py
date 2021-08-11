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
            #uid=request.session['uid']
            #profile=Student.objects.filter()
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
            title=request.POST.get('title')
            if(len(syllabusfeed.objects.filter(subcode_id=subcode,unit_no=unit))==0 ):
                syllabusfeed.objects.create(subcode_id=subcode,key=key,unit_no=unit,title=title)
                return HttpResponse("<a href=\"\\dashboard\\syllabusfeed\">go back</a>")
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
def enrollsubject(request):
    if not checklogin(request):
        return redirect("/login/")
    else: 
        if request.method == 'POST':
            dept=request.POST.get('dept')
            sem=request.POST.get('sem')
            subcode1=request.POST.get('subcode1').upper()
            subcode2=request.POST.get('subcode2').upper()
            subcode3=request.POST.get('subcode3').upper()
            subcode4=request.POST.get('subcode4').upper()
            subcode5=request.POST.get('subcode5').upper()
            subcode6=request.POST.get('subcode6').upper()
            uids=Student.objects.filter(dept=dept,semester=sem).values('uid')
            print(uids)
            if(sem=='1'):
                for i in uids:
                    enrolledsub.objects.create(uid=i['uid'],sub1=subcode1,sub2=subcode2,sub3=subcode3,sub4=subcode4,sub5=subcode5,sub6=subcode6).save()
            else:
                for i in uids:
                    enrolledsub.objects.filter(uid=i['uid']).update(sub1=subcode1,sub2=subcode2,sub3=subcode3,sub4=subcode4,sub5=subcode5,sub6=subcode6)
            return redirect('/dashboard')
        else:
            return render(request,'subjectenrollment.html')
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
            data=g.getWeb(q)
            print(data.keys())
            return render(request,'searchresult.html',data)
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
        return render(request,'profile.html',{'data':data[0]})

def course(request):
    if not checklogin(request):
        return redirect("/login/")
    uid=request.session['uid']
    courses=enrolledsub.objects.filter(uid=uid).values('sub1','sub2','sub3','sub4','sub5','sub6')
    data={}
    for name,code in courses[0].items():
        title=subjects.objects.filter(subcode=code).values('subject')
        data[name] ={'subcode' : code,'title' : title[0]['subject'] }

    print(data)
    return render(request,'course.html',{'data':data})

def rendercourse(request,subcode,subject):
    if not checklogin(request):
        return redirect("/login/")
    data={}
    if request.method == 'POST':
        unit=request.POST.get('unit_no')
        keyraw = syllabusfeed.objects.filter(subcode=subcode,unit_no=unit).values('key','title')

        data['subjectdetails']={'subcode':subcode,'title':subject,'unitname':keyraw[0]['title']}
        keys= g.getKeys(keyraw[0]['key'])
        col={}
        for i in keys:
            print(g.getWeb(i)['weblinks'][0]['link'])
            col[i]=g.getWeb(i)['weblinks'][0]['link']
        data['keys_tags']=col
        data['unit']=unit
        print (data)
        #data={'unit':1,'subjectdetails': {'subcode': 'MA8151', 'title': 'engineertin MAths 1', 'unitname': 'Differential Calculus'}, 'keys_tags': {'Representation of functions': 'https://www.youtube.com/watch?v=ACZDnF8-9Ks', 'Limit of a function': 'https://en.wikipedia.org/wiki/Limit_of_a_function', 'Continuity': 'https://www.continuity.net/', 'Derivatives': 'https://www.investopedia.com/terms/d/derivative.asp', 'Differentiation rules': 'https://www.mathsisfun.com/calculus/derivatives-rules.html', 'Maxima and Minima of functions of one variable.': 'https://en.wikipedia.org/wiki/Maxima_and_minima'}}
        return render(request,'coursedetails.html',data)
    else:
        unit=1
        keyraw = syllabusfeed.objects.filter(subcode=subcode,unit_no=unit).values('key','title')

        data['subjectdetails']={'subcode':subcode,'title':subject,'unitname':keyraw[0]['title']}
        keys= g.getKeys(keyraw[0]['key'])
        
        col={}
        for i in keys:
            print(g.getWeb(i)['weblinks'][0]['link'])
            col[i]=g.getWeb(i)['weblinks'][0]['link']
        data['keys_tags']=col
        data['unit']=unit
        #data={'subjectdetails': {'subcode': 'MA8151', 'title': 'engineertin MAths 1', 'unitname': 'Differential Calculus'}, 'keys_tags': {'Representation of functions': 'https://www.youtube.com/watch?v=ACZDnF8-9Ks', 'Limit of a function': 'https://en.wikipedia.org/wiki/Limit_of_a_function', 'Continuity': 'https://www.continuity.net/', 'Derivatives': 'https://www.investopedia.com/terms/d/derivative.asp', 'Differentiation rules': 'https://www.mathsisfun.com/calculus/derivatives-rules.html', 'Maxima and Minima of functions of one variable.': 'https://en.wikipedia.org/wiki/Maxima_and_minima'}}
        return render(request,'coursedetails.html',data)

def coursedetails(request,subcode):
    if not checklogin(request):
        return redirect("/login/")
    subject=subjects.objects.filter(subcode=subcode).values('subject')[0]['subject']
    return rendercourse(request,subcode,subject)    