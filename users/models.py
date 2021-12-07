from django.contrib.auth.models import User
from django.db import models


class Session(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    session = models.JSONField()