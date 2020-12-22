from django.db import models
from datetime import datetime
from users.models import Adduser
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(to=Adduser, on_delete=models.CASCADE)  # author will be the object of Adduser
    title = models.CharField(max_length=300)
    post = models.TextField(max_length=2000)
    date = models.DateTimeField(default=datetime.now())
    category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author}"
