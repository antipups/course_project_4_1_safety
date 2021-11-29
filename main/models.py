from django.contrib.auth.models import User
from django.db import models


class Messages(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,)
    whom = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,)
    message_content = models.BinaryField()


class Session(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    session = models.JSONField()


class Mails(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    mail_title = models.CharField(max_length=16)
    login = models.BinaryField()
    password = models.BinaryField()
