from django.db import models

# Create your models here.
class Blog(models.Model):
    aurthor = models.CharField(max_length=200)
    title = models.CharField(max_length= 200)
    desc = models.TextField()
    image = models.ImageField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    def __str__(self):
        return self.name