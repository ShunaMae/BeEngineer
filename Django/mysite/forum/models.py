from django.db import models
# Create your models here.

class Topic(models.Model):
    name = models.CharField("topic name", max_length = 200)

    def __str__(self):
        return self.name

class Message(models.Model):
    def __str__(self):
        return self.content
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    content = models.CharField("message", max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)