from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    link = models.CharField(max_length=120)
    workimg = models.ImageField(upload_to='img/', max_length=255)

    def __str__(self):
        return self.title + ' / ' + self.content