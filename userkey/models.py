from django.db import models
from django.contrib.auth.models import User

class UserKey(models.Model):
    user = models.OneToOneField(User)
    public_key = models.TextField(null = True, blank = True)
    private_key = models.TextField(null = True, blank = True)
