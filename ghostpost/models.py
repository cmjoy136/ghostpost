from django.db import models

BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))

class Post(models.Model):
    boast_roast = models.BooleanField(choices=BOOL_CHOICES)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    content = models.CharField(max_length=280)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content