from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Memo(models.Model):
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    text = models.TextField()