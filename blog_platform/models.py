from django.db import models
from django.contrib.auth.models import User

# Create Model
class PostData(models.Model):
    #image = models.ImageField(upload_to="")
    title_name = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_name


