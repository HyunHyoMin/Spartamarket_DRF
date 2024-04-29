from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    birth = models.DateField()
    REQUIRED_FIELDS = ['email', 'name', 'nickname', 'birth']

    first_name = None
    last_name = None