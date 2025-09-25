from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

class Poll(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='polls')
    question = models.CharField(max_length=100)

class Choice(models.Model):
    poll = models.ForeignKey(Poll,
                             on_delete=models.CASCADE,
                             related_name='choices')
    choice_text = models.CharField(max_length=100,
                                   verbose_name='Варианты ответа')