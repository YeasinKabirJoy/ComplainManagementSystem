from django.shortcuts import render, get_object_or_404
from .ComplainForm import ComplainForm
from .CommentForm import CommentForm
from .models import Complain

from Verified_User.models import Verified_User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def complainForm(request):
    complain_form = ComplainForm()
    msg = ''

    if request.method == 'POST':
        complain_form = ComplainForm(request.POST, request.FILES)
        msg = 'Invalid input'

        if complain_form.is_valid():
            complain = complain_form.save(commit=False)

            try:
                complain.user = Verified_User.objects.get(user=request.user)
                if complain.user.status == 'Verified':
                    if complain.user.type=="Student":
                        complain.save()
                        msg = 'Insertion done!'
                        complain_form = ComplainForm()
                    else:
                        msg = "You are not allowed to complain!"
                else:
                    complain_form = ComplainForm()
                    msg = 'Sorry !! You are not verified yet!!'
            except Exception:
                 msg = "Verify your profile by giving necessary documents"

    context = {
        'complain_form': complain_form,
        'msg': msg
    }
    return render(request, 'Complain/ComplainForm.html', context)


@login_required
def commentForm(request):
    comment_form = CommentForm()
    msg = ''

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        msg = 'Invalid input'

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            try:
                comment.user = Verified_User.objects.get(user=request.user)
                if comment.user.status == 'Verified':
                    comment.save()
                    msg = 'Insertion done!'
                    comment_form = CommentForm()
                else:
                    comment_form = CommentForm()
                    msg = 'Sorry !! You are not verified yet!!'
            except Exception:
                msg = "Verify your profile by giving necessary documents"

    context = {
        'comment_form': comment_form,
        'msg': msg
    }
    return render(request, 'Complain/CommentForm.html', context)



def allComplain(request):

    complain = Complain.objects.all()



    context = {
        'complain':complain
    }

    return render(request, 'Complain/allComplain.html', context)

def complain_details(request, complain_id):
    complain = get_object_or_404(Complain, id=complain_id)

    comment_form = CommentForm()
    msg = ''

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        msg = 'Invalid input'

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            try:
                comment.user = Verified_User.objects.get(user=request.user)
                if comment.user.status == 'Verified':
                    if comment.comment!="":
                        comment.save()
                        complain.comment.add(comment)
                        complain.save()
                        msg = 'Insertion done!'
                        comment_form = CommentForm()
                else:
                    comment_form = CommentForm()
                    msg = 'Sorry !! You are not verified yet!!'
            except Exception:
                msg = "Verify your profile by giving necessary documents"

    vote = request.POST.get("vote")

    if complain.votes.exists(request.user.id):
        pass
    else:
        if vote == "upvote":
            complain.votes.up(request.user.id)

        elif vote == "downvote":
            complain.votes.down(request.user.id)
        else:
            pass

    context = {
        'complain': complain,
        'vote': vote,
        'comment_form': comment_form,
        'msg': msg

    }

    return render(request, 'Complain/complainDetails.html', context)



def homepage(request):

    return render(request, 'Complain/home.html')







