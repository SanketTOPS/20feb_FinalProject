from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings
from django.contrib.auth import logout
import requests

# Create your views here.

def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def login(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        id=usersignup.objects.get(username=unm)
        print("UserID:",id.id)
        if user:
            print("Login Successfully!")
            request.session['user']=unm
            request.session['userid']=id.id

            #OTP SMS
            
            return redirect('/')
        else:
            print("Error!Login faild....")
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")

            #Email Sending Code
            global otp
            otp=random.randint(11111,99999)
            sub="Your One Time Password"
            msg=f"Dear User\n\nThanks for registration with us!\n\nFor account verification, your one time password is below.\n\nYour One time password:{otp}\n\nThanks & Regards!\n+91 9724799469 | www.tops-int.com"
            from_email=settings.EMAIL_HOST_USER
            #to_email=["patelbhumi2504@gmail.com","ayushpatel5440@gmail.com","heetgokani8@gmail.com","vinaychhatraliya19@gmail.com"]
            to_email=[request.POST['username']]
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
            return redirect('otpverify')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get('user')
    if request.method=='POST':
        newfeedback=feedbackForm(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your feedback has been submitted!")

            #OTP SEND
            url = "https://www.fast2sms.com/dev/voice"
            querystring = {"authorization":"KEY","variables_values":"5599","route":"otp","numbers":"9106438428,7228846917,6355826374"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)

            #Feedback Email Sending Code
            sub="Thank You!"
            msg=f"Dear User\n\nThanks for your valueable feedback!\n\nThanks & Regards!\n+91 9724799469 | www.tops-int.com"
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
        else:
            print(newfeedback.errors)
    return render(request,'contact.html',{'user':user})

def otpverify(request):
    global otp
    msg=""
    print("OTP:",otp)
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            return redirect("login")
        else:
            print("Invalid OTP...Please try again!")
            msg="Invalid OTP...Please try again!"
    return render(request,'otpverify.html',{'msg':msg})


def userlogout(request):
    logout(request)
    return redirect('/')

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cid=usersignup.objects.get(id=userid)
    if request.method=='POST':
        updateReq=signupForm(request.POST,instance=cid)
        if updateReq.is_valid():
            updateReq.save()
            print("Update successfully!")
            return redirect('/')
        else:
            print(updateReq.errors)
    return render(request,'profile.html',{'user':user,'cid':cid})