from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from sample_web_application import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from web_app.forms import ReviewForm
from web_app.models import Review


# Create your views here.
@login_required
def home_view(request):
    return render(request,'web_app/home.html')

@login_required
def menu_view(request):
    return render(request,'web_app/menu.html')

@login_required
def about_us_view(request):
    return render(request,'web_app/about_us.html')

@login_required
def contact_info_view(request):
    return render(request,'web_app/contact_info.html')

def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request,"Your password and confirm password didn't match....!")

        if User.objects.filter(username=username):
            messages.error(request,'Your username already existed...!')
            return redirect('/signup')

        if User.objects.filter(email=email):
            messages.error(request,'Your email Id already existed...!')
            return redirect('/signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request,'Your account has been created successfully.')

        #Welcome Email

        subject = "Welcome to RED BUCKET Resturent World...!"
        message = "Hello " + myuser.username + "!!  \n" + "Welcome to RED BUCKET!! \nThank you for creating an account in our website. \nYour account have been created successfully. \n\nThanking you \n  RED BUCKET"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect('/signin')

    return render(request,'web_app/signup.html')

def signin_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(request,username=username, password=pass1)

        if user is not None:
            login(request,user)
            return render(request,'web_app/home.html')
        else:
            messages.error(request,'Bad credential.')
            return redirect('/signin')

    return render(request,'web_app/signin.html')

def review_view(request):
    form=ReviewForm()
    if request.method == 'POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for given your valuable review.')
    return render(request,'web_app/review.html',{'form':form})

def view_review(request):
    review=Review.objects.all()
    return render(request,'web_app/view_review.html',{'r':review})