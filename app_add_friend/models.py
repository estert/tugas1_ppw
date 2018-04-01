from django.db import models

class Message(models.Model):
        name = models.CharField(max_length=27)
        url = models.CharField(max_length=200)
        created_date = models.DateTimeField(auto_now_add=True)