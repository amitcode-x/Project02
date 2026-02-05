from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=100, null=True)
    date = models.DateField()
