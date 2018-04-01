from django.db import models

class Status(models.Model):
    status = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    post = models.ForeignKey(Status, on_delete=models.CASCADE, null = True)
    nama = models.TextField()
    comment = models.TextField()
    comments_created_date = models.DateTimeField(auto_now_add=True)
