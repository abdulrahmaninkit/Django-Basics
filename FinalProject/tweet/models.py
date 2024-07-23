from django.db import models
from django.contrib.auth.models import User

class tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


#This is used to show in the admin pannel about the user that are present in the admin pannel
def __str__(self):
    return f'{self.user.username} - {self.text[:10]}'