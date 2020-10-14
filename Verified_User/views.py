from django.shortcuts import render, get_object_or_404
from .models import Verified_User
from .User_Verification_Form import User_Verification_Form
from django.contrib.auth.decorators import login_required
from Complain.models import Complain

# Create your views here.


@login_required
def user_verification_form(request):
    try:
        user_verification= User_Verification_Form()
        msg =" "

        if request.method == 'POST':
            user_verification= User_Verification_Form(request.POST, request.FILES)
            msg = 'Invalid input'

            if user_verification.is_valid():
                user_form = user_verification.save(commit=False)
                user_form.user = request.user
                user_form.save()
                msg = 'Insertion done!'
                user_verification= User_Verification_Form()

        context = {
            'user_verification_form': user_verification,
            'msg': msg
        }
        return render(request, 'Verified_User/user_verification_form.html', context)

    except Exception:
        user_verification = User_Verification_Form()
        context = {
             'user_verification_form': user_verification,
             'msg': 'You have already applied for verification.',
        }
        return render(request, 'Verified_User/user_verification_form.html', context)



@login_required
def show_profile(request):
    try:
        userC = Verified_User.objects.get(user=request.user)
        if userC.type == "Student":
            complain = Complain.objects.filter(user=userC)
        else:
            complain = ""

    except Exception:
        complain = ""

    try:
        profile = Verified_User.objects.get(user=request.user)
    except Verified_User.DoesNotExist:
        profile = 'Please complete your profile'

    context = {
        "profile": profile,
        "complain": complain
    }

    return render(request, 'Verified_User/profile.html', context)







