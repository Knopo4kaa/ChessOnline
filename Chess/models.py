from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class Game(models.Model):
    WHITE='W'
    BLACK='B'
    DRAW='D'
    WINNER_COLORS = (
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (DRAW, 'Draw'),

    )
    players = models.ManyToManyField(settings.AUTH_USER_MODEL)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    winner_color=models.TextField(max_length=1,choices=WINNER_COLORS,default=WHITE)



class User(AbstractUser):
    avatar = models.ImageField(blank=True,upload_to='avatars')
    rating=models.IntegerField(default=1200)
    games=models.ManyToManyField(Game,blank=True)
    followers=models.ManyToManyField('self',blank=True)
    following=models.ManyToManyField('self',blank=True)



class Step(models.Model):
    number=models.IntegerField()
    step=models.CharField(max_length=20)
    duration=models.DurationField()
    game=models.ForeignKey(Game)




class Article(models.Model):
    text=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime=models.DateTimeField()
    game=models.ManyToManyField(Game)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime = models.DateTimeField()
    game = models.ManyToManyField(Game)
    article=models.ForeignKey(Article)





# Create your models here.













