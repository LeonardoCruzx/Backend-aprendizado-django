from django.db import models


from django.contrib.auth.models import AbstractUser
from .manager import UserManager

from cloudinary.models import CloudinaryField

from django.contrib.auth import authenticate

# Create your models here.
class User(AbstractUser):
    objects = UserManager()
    username = None

    last_login = models.DateTimeField(
        verbose_name="ultimo login",
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
    profile_picture = CloudinaryField(
        "profile_pictures/profile_picture",
        default="profile_pictures/default_profile_picture",
        null=True
    )

    user_permissions = ["can_login"]

    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.nick


    @staticmethod
    def autenticar_se(request):
        email = request.data.get("email")
        password = request.data.get("password")
        if email == None:
            return {"erro":"porfavor insira um email"}
        if password == None:
            return {"erro":"porfavor insira uma senha"}
        user = authenticate(email=email,password=password)
        if not user:
            return {'erro': 'Credencias invalidas (sem token)'}
        return user
        
