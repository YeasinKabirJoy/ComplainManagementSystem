from django.db import models
from django.contrib.auth.forms import User

# Create your models here.
class Verified_User(models.Model):
    email = models.EmailField(unique=True)
    image_of_id = models.ImageField(upload_to='verified_user/image_of_id/')
    status = models.CharField(max_length=100, choices=(('Verified', 'Verified'), ('Not Verified', 'Not Verified')), default='Not Verified')
    type = models.CharField(max_length=100, choices=(('Student', 'Student'), ('Admin', 'Admin')), default='Student')

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.status == 'Verified' and self.type == 'Student':
            try:
                Verified_Email.objects.get(email=self.email)
                self.status = "Not Verified"
            except Exception:
                ve = Verified_Email(email=self.email)
                ve.save()
                self.email = self.user.username + "@uapStudent.com"
                self.image_of_id = 'meme1.png'

        elif self.status == 'Verified' and self.type == 'Admin':
            try:
                Verified_Email.objects.get(email=self.email)
                self.status = 'Not Verified'
            except Exception:
                self.email = self.user.username + "@uapAdmin.com"
                ve = Verified_Email(email=self.email)
                ve.save()

        super(Verified_User, self).save(*args, **kwargs)


class Verified_Email(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
