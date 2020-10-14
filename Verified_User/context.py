from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Verified_User

def verifiedUser(request):
    Student=False
    Admin =False
    msg=""
    try:
        verified_user = get_object_or_404(Verified_User,user=request.user)
    except Exception:
        verified_user=False
        msg = "Verify Yourself"
    if verified_user != False:
        if verified_user.type =="Student":
            if verified_user.status=="Verified":
                Student=True
            else:
                msg="Wait for your Verification"
        if verified_user.type == "Admin":
            if verified_user.status == "Verified":
                Admin =True
            else:
                msg="Wait for your Verification!"
    context = {
        'verified_user': verified_user,
        'student':Student,
        'admin':Admin,
        'verify':msg
    }
    return context