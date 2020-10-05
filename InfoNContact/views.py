from django.shortcuts import render
from .infoForm import InfoForm
from .faqForm import FaqForm
from .models import FAQ,Info
from Verified_User.models import Verified_User
from django.contrib.auth.decorators import login_required

@login_required
def infoForm(request):
    info_form = InfoForm()
    msg = ''

    if request.method == 'POST':
        info_form = InfoForm(request.POST)
        msg = 'Invalid input'
        if info_form.is_valid():
            info = info_form.save(commit=False)

            try:
                user = Verified_User.objects.get(user=request.user)
                if user.status == 'Verified':
                    if user.type == "Admin":
                        info.save()
                        msg = 'Insertion done!'
                        info_form = InfoForm()
                    else:
                        msg = "You are not allowed to add information!"
                else:
                    info_form = InfoForm()
                    msg = 'Sorry !! You are not verified yet!!'
            except Exception:
                msg = "Verify your profile by giving necessary documents."

    context = {
        'info_form': info_form,
        'msg': msg
    }
    return render(request, 'InfoNContact/infoForm.html', context)


@login_required
def faqForm(request):
    faq_form = FaqForm()
    msg = ''

    if request.method == 'POST':
        faq_form = FaqForm(request.POST)
        msg = 'Invalid input'
        if faq_form.is_valid():
            faq = faq_form.save(commit=False)

            try:
                user = Verified_User.objects.get(user=request.user)
                if user.status == 'Verified':
                    if user.type == "Admin":
                        faq.save()
                        msg = 'Insertion done!'
                        faq_form = FaqForm()
                    else:
                        msg = "You are not allowed to add FAQ!"
                else:
                    faq_form = FaqForm()
                    msg = 'Sorry !! You are not verified yet!!'
            except Exception:
                msg = "Verify your profile by giving necessary documents."

    context = {
        'faq_form': faq_form,
        'msg': msg
    }
    return render(request, 'InfoNContact/faqForm.html', context)


def showFAQ(request):
    faq=FAQ.objects.all()
    context={
        'faq':faq
    }

    return render(request,'InfoNContact/FAQ.html',context)

def showInfo(request):
    info=Info.objects.all()
    context={
        'info':info
    }

    return render(request,'InfoNContact/info.html',context)
