from django.db import models

# Create your models here.
class Adduser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    username = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        ordering = ['fname']

    def __str__(self):
        return f"{self.email}"

# create table adduser(fname varchar(100))
# customizing admin panel 