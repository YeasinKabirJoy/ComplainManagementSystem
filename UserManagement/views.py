from django.shortcuts import render
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
            form = UserCreationForm()
    context = {
        "message":msg,
        'form': form,
    }
    return render(request, 'UserManagement/registration.html', context)

