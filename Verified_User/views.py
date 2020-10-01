from django.shortcuts import render
from .models import Verified_User
from Complain.models import Complain, Comment, Vote
from Tag.models import Tag, ComplainTag
from InfoNContact.models import FAQ, Info
from .User_Verification_Form import User_Verification_Form
from django.contrib.auth.decorators import login_required

# Create your views here.


def showTables(request):

    # studentTable = Student.objects.all()
    verified_userTable = Verified_User.objects.all()
    complainTable = Complain.objects.all()
    commentTable = Comment.objects.all()
    voteTable = Vote.objects.all()
    tagTable = Tag.objects.all()
    complainTag = ComplainTag.objects.all()
    faqTable = FAQ.objects.all()
    infoTable = Info.objects.all()



    context = {
        # 'studentTable': studentTable,
        'verified_userTable': verified_userTable,
        'complainTable': complainTable,
        'commentTable': commentTable,
        'votTable': voteTable,
        'tagTable': tagTable,
        'complainTag': complainTag,
        'faqTable': faqTable,
        'infoTable': infoTable,
    }

    return render(request, 'showTables.html', context)

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
        profile = Verified_User.objects.get(user=request.user)
    except Verified_User.DoesNotExist:
        profile = 'Please complete your profile'

    context = {
        "profile": profile
    }

    return render(request, 'Verified_User/profile.html', context)









