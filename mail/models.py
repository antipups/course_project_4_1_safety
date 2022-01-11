from django.contrib.auth.models import User
from django.db import models


class KeysStorage(models.Model):
    from_email = models.CharField(max_length=32)
    to_email = models.CharField(max_length=32)
    privkey = models.TextField(max_length=4096)
    pubkey = models.TextField(max_length=4096)
    tripleDesKey = models.CharField(max_length=4096)


class MessagesSigns(models.Model):
    from_email = models.CharField(max_length=32)
    to_email = models.CharField(max_length=32)
    sign = models.CharField(max_length=4096)
