from django.shortcuts import get_object_or_404

from .models import Verified_User


def verifiedUser(request):
    Student=False
    Admin =False
    try:
        verified_user = get_object_or_404(Verified_User,user=request.user)
    except Exception:
        verified_user=False
        msg="Verify yourself"
    if verified_user != False:
        if verified_user.type =="Student":
            if verified_user.status=="Verified":
                Student=True
            else:
                msg="Wait for your verfication"
        if verified_user.type =="Admin":
            if verified_user.status == "Verified":
                Admin =True
            else:
                msg="Wait for your verfication"
    context = {
        'verified_user': verified_user,
        'student':Student,
        'admin':Admin,
        'verify':msg
    }
    return context