from django.db import models


from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class User(AbstractUser):
    objects = UserManager()
    nick = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    class Meta(AbstractUser.Meta):
        pass

    user_permissions = ["can_login"]

    def __str__(self):
        return self.username





    




    

    

