"""ComplainManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from Student import views as student_view
from Complain import views as complain_view
from Tag import views as tag_views
from InfoNContact import views as infocontac_views
from django.conf import settings
from django.conf.urls.static import static
from UserManagement import views as user_views
from Verified_User import views as verified_user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', complain_view.homepage, name='homepage'),
    path('allComplain/', complain_view.allComplain, name='allComplain'),
    path('allComplain/<int:complain_id>', complain_view.complain_details, name='complainDetails'),
    path('faq/', infocontac_views.showFAQ, name='faq'),
    path('info/', infocontac_views.showInfo, name='info'),
    path('user_verification_form/', verified_user_views.user_verification_form, name='user_verification_form'),
    path('my_profile/',verified_user_views.show_profile, name='my_profile'),
    path('complainForm/', complain_view.complainForm, name='complainForm'),
    path('commentForm/', complain_view.commentForm, name='commentForm'),
    path('tagForm/', tag_views.insertTag, name='tagForm'),
    path('infoForm/', infocontac_views.infoForm, name='infoForm'),
    path('faqForm/', infocontac_views.faqForm, name='faqForm'),
    path('registration/', user_views.registration, name='registration'),
    path('about/', infocontac_views.aboutUS, name='about'),
    path('accounts/', include('django.contrib.auth.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)