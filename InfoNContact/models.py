from django.db import models

class Info(models.Model):

    email=models.EmailField(max_length=200)
    phone_no=models.IntegerField( unique= True)


    def __str__(self):
        return str(self.id)

class FAQ(models.Model):

    question=models.TextField()
    answer=models.TextField()

    def __str__(self):
        return str(self.id)


