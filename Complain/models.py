from django.db import models
from Verified_User.models import Verified_User
from Tag.models import Tag


# Create your models here.

class Comment(models.Model):

    comment = models.TextField()

    def __str__(self):
        return str(self.complain.id)


class Vote(models.Model):

    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)



    def __str__(self):
        return str(self.id)

class Complain(models.Model):
    image = models.ImageField(upload_to='complain/image/', blank=True,null=True)
    status = models.CharField(max_length=100, choices=(('Approved', 'Approved'), ('Not Approved', 'Not Approved'), ('Not Approved', 'Pending')), default='Approved')
    description = models.TextField()
    type = models.CharField(max_length=100, choices=(('General', 'General'), ('Departmental', 'Departmental'), ('Both', 'Both')), default='General')
    tag = models.ManyToManyField(Tag,blank=True)


    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    user = models.ForeignKey(Verified_User, on_delete=models.CASCADE)





    def __str__(self):
        return str(self.id)







