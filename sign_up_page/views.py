from sign_up_page.models import Account
from django.shortcuts import render, redirect

from django.contrib import messages

# Create your views here.
def signup(request):
    print(request.method)
    if request.method == 'POST':
        fullname=request.POST['fname_test']
        username=request.POST['uname_test']
        dob=request.POST['date_test']
        gender=request.POST['btn']
        email=request.POST['email_test']
        state=request.POST['state']
        city=request.POST['city']
        pincode=request.POST['pincode_test']
        password1=request.POST['pass_test1']
        password2=request.POST['pass_test2']
        if password1==password2:
            if Account.objects.filter(email=email).exists() and email!='':
                messages.info(request, 'Email already used. Use another email id.')
                return redirect('signup_page')
            elif Account.objects.filter(username=username).exists():
                messages.info(request, 'Username not available. Use another username.')
                return redirect('signup_page')
            else:
                user=Account.objects.create_user(fullname=fullname, username=username, dob=dob, gender=gender, email=email, state=state, city=city, pincode=pincode, password=password1)
                user.save()
                return redirect('login_page')
        else:
            messages.info(request, 'Make sure your passwords match.')
            return redirect('signup_page')
    else:
        return render(request,'signup_page.html')
def login(request):
    return render(request,'login_page.html')
def forg_pass(request):
    return render(request,'forg_pass_page.html')