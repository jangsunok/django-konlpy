
from django.db import models


class Key(models.Model):
    label = models.CharField(max_length=100)
    priority = models.IntegerField()


class Chat(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    key = models.ForeignKey(Key)
    content = models.TextField()
    request = models.IntegerField()


class Log(models.Model):
    chat = models.ForeignKey(Chat)
    best_key = models.ForeignKey(Key)
    created_at = models.DateTimeField(auto_now_add=True)
