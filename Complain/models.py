from django.db import models
from Verified_User.models import Verified_User



# Create your models here.
class Complain(models.Model):
    image = models.ImageField(upload_to='complain/image/', blank=True,null=True)
    status = models.CharField(max_length=100, choices=(('Approved', 'Approved'), ('Not Approved', 'Not Approved'), ('Not Approved', 'Pending')), default='Approved')
    description = models.TextField()
    type = models.CharField(max_length=100, choices=(('General', 'General'), ('Departmental', 'Departmental'), ('Both', 'Both')), default='General')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    user = models.ForeignKey(Verified_User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    user = models.ForeignKey(Verified_User, on_delete=models.CASCADE, default=1)

    description = models.TextField()

    def __str__(self):
        return 'comment for complain' + str(self.complain.id)


class Vote(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    user = models.ForeignKey(Verified_User, on_delete=models.CASCADE, default=1)
    vote = models.CharField(max_length=50, choices=(('Upvote', 'Upvote'), ('Downvote', 'Downvote')), default=None)

    class Meta:
        unique_together = ('complain', 'user')

    def __str__(self):
        return str(self.user)+' voted in complain '+ str(self.complain.id)




