from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sput(models.Model):
    """
    It is the model for a sput and labels the colum names in teh table.
    """

    headline = models.CharField(max_length=130)
    content = models.TextField()
    antenna = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='sputs')

    def __repr__(self):
        return self.headline