from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    date = models.DateField('Date')

    def __str__(self):
        return f"{self.title}, {self.description}, {self.date}"

class Book(models.Model):
    bookcover = models.ImageField(upload_to='media')
    bookfile = models.FileField(upload_to='media')
    booktitle = models.CharField(max_length=500)


		
