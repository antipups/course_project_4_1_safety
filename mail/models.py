from django.contrib.auth.models import User
from django.db import models


class Messages(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,
                             related_name='from_user')
    whom = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,
                             related_name='to_user')
    message_content = models.BinaryField()


class Mails(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    mail_title = models.CharField(max_length=16)
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=512)
