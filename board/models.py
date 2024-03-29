from asyncore import write
from django.db import models
from acc.models import User
from django.utils import timezone
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    content = models.TextField(blank=True)
    likey = models.ManyToManyField(User, blank=True, related_name="likey")
    pubdate = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.subject

    def summary(self):
        if len(self.content) > 100:
            return f"{self.content[:100]} ..."
        return self.content

class Reply(models.Model):
    b = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.b}_{self.replyer}"

