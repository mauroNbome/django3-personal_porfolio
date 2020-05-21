from django.db import models
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today) # I saved the day with this.
    #date = models.DateField(default=now)

    def __str__(self):
        return self.title
