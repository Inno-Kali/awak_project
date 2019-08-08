from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:200]

    def pub_date_nice(self):
        return self.pub_date.strftime('%b %e %Y')
