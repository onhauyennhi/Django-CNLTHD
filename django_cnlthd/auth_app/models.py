from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def upload_to(instance, filename):
        return "images/user_image/{filename}".format(filename=filename)

    image = models.ImageField(
        upload_to=upload_to,
        max_length=200,
        blank=True,
        null=True,
        default="images/user_image/default.png",
    )
    is_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"User({self.username})"
