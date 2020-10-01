from django.shortcuts import render
from .tagForms import TagForm
from .complainTagForms import ComplainTagForm
from Verified_User.models import Verified_User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def insertTag(request):
    tag_form = TagForm()
    message = ""

    if request.method == "POST":
        tag_form = TagForm(request.POST)
        message = "Invalid Input!"

        if tag_form.is_valid():
            tag = tag_form.save(commit=False)

            try:
                user = Verified_User.objects.get(user=request.user)
                if user.status=="Verified":
                    if user.type=="Admin":
                        tag.save()
                        message ="Insertion done!"
                        tag_form=TagForm()
                    else:
                        message ="You are not allowed to add a tag!"
                else:
                    tag_form=TagForm()
                    message = "Sorry! You are not verified yet!"
            except Exception:
                message = "Verify your profile by giving necessary documents."

    context={
        'tag_form': tag_form,
        'message': message
    }
    return render(request, 'Tag/tagForm.html', context)




@login_required
def insertComplainTag(request):
    complainTag_form = ComplainTagForm()
    message = ""

    if request.method == "POST":
        complainTag_form = ComplainTagForm(request.POST)
        message = "Invalid input. Please try again!"

        if complainTag_form.is_valid():
            complain = complainTag_form.save(commit=False)

            try:
                user = Verified_User.objects.get(user=request.user)
                if user.status == "Verified":
                    if user.type == "Student":
                        complain.save()
                        message = "Insertion done!"
                        complainTag_form = ComplainTagForm()
                    else:
                        message = "You are not allowed to add information!"

                else:
                    complainTag_form = ComplainTagForm()
                    message = "Sorry! You are not verified yet."
            except Exception:
                message = "Verify your profile by giving necessary documents!"

    context ={
        'complainTagForm': complainTag_form,
        'message': message
    }
    return render(request, 'Tag/complainTagForm.html', context)
