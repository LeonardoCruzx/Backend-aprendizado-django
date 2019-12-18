from django.db import models


from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.
class User(AbstractUser):
    objects = UserManager()
    username = None
    last_login = models.DateTimeField(
        auto_now=True,
        null=True
    )
    email = models.EmailField(
        null=False,
        unique=True,
    )
    nick = models.CharField(
        max_length=30,
        null=True,
        unique=True
    )

    user_permissions = ["can_login"]

    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.nick





    




    

    

