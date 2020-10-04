from django.shortcuts import get_object_or_404

from .models import Verified_User


def verifiedUser(request):
    try:
        verified_user = get_object_or_404(Verified_User,user=request.user)
    except Exception:
        verified_user=''
    context = {
        'verified_user': verified_user
    }
    return context