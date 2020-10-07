from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .registrationForm import CreateUserForm

# Create your views here.
def registration(request):
    form = CreateUserForm()
    msg =""

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        msg="Invalid Input"
        if form.is_valid():
            form.save()
            msg="Registration Successful!"
            form = CreateUserForm()
            return redirect('login')
    context = {
        "message":msg,
        'form': form,
    }
    return render(request, 'UserManagement/registration.html', context)

