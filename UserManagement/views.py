from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registration(request):
    form = UserCreationForm()
    msg =""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        msg="Invalid Input"
        if form.is_valid():
            form.save()
            msg="Registration Successful!"
            return redirect('login')
    context = {
        "message":msg,
        'form': form,
    }
    return render(request, 'UserManagement/registration.html', context)

