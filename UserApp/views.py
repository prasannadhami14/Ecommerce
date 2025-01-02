from django.shortcuts import render,redirect
from .forms import register_user_form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# register
def register_user(request):
    form=register_user_form()
    if request.method == 'POST':
        form=register_user_form(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,user +"!"+ " your account has been created successfully!")

            return redirect('userApp:login-user')
        else:
            messages.warning(request,"Invalid credentials !!!")
            print(messages)

    return render(request,'userApp/register.html',{'form':form})

# login
def login_user(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Sucessfully logged in !!')
            return redirect('productApp:product-page')
        else:
            messages.warning(request,'Invalid Credentials!!!')
    return render(request,'userApp/login.html')
# logout
def logout_user(request):
    logout(request)
    return redirect('productApp:product-page')
#forgot password
def forgot_password(request):
    pass
