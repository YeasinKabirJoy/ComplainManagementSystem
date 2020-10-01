from django.shortcuts import render
from .ComplainForm import ComplainForm
from .CommentForm import CommentForm
from .VoteForm import VoteForm
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


@login_required
def voteForm(request):
    vote_form = VoteForm()
    msg = ''

    if request.method == 'POST':
        vote_form = VoteForm(request.POST)
        msg = 'Invalid input'

        if vote_form.is_valid():
            vote = vote_form.save(commit=False)

            try:
                vote.user = Verified_User.objects.get(user=request.user)
                if vote.user.status == 'Verified':
                    if vote.user.type=="Student":
                        vote.save()
                        msg = 'Insertion done!'
                        vote_form = VoteForm()
                    else:
                        msg = "You are not allowed to vote!"
                else:
                    vote_form = VoteForm()
                    msg = 'Sorry !! You are not verified yet!!'
            except Exception:
                 msg = "Verify your profile by giving necessary documents"

    context = {
        'vote_form': vote_form,
        'msg': msg
    }
    return render(request, 'Complain/VoteForm.html', context)