from django.shortcuts import render,redirect
from .forms import register_User_form
from django.contrib import messages
# register
def register_user(request):
    form=register_User_form()
    if request.method== 'POST':
        form=register_User_form(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,"Account created for "+ request.user)
            return redirect('userApp:login-user')
        else:
            messages.warning(request,"Invalid credentials !!!")
    return render(request,'userApp/register.html',{'form':form})

# login
def login_user(request):
    return render(request,'userApp/login.html')