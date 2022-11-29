from django.db import models


# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    create_date = models.DateField()


class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.postname
