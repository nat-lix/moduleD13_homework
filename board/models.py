from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    tanks = 'TK'
    heals = 'HL'
    dd = 'DD'
    traders = 'TR'
    gildmasters = 'GM'
    questgivers = 'QG'
    blacksmiths = 'BS'
    leathermasters = 'LM'
    poisonmasters = 'PM'
    spellmasters = 'SM'
    CATEGORIES = [
        (tanks,'Танки'),
        (heals,'Хилы'),
        (dd,'ДД'),
        (traders,'Торговцы'),
        (gildmasters,'Гилдмастеры'),
        (questgivers,'Квестгиверы'),
        (blacksmiths,'Кузнецы'),
        (leathermasters,'Кожевники'),
        (poisonmasters,'Зельевары'),
        (spellmasters,'Мастера заклинаний'),
]
    name = models.CharField(max_length = 255, unique = True)
    subscribers = models.ManyToManyField(User, blank=True)
    def __str__(self):
                return f'{self.name}'

class CategorySubscribe(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    media = models.FileField(upload_to='media/', default='')

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return f'/posts/{self.id}'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Response(models.Model):
    responsePost = models.ForeignKey(Post, on_delete=models.CASCADE)
    responseUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    responseReply = models.ForeignKey(Response, related_name='response_reply', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    replied_to_user = models.ForeignKey(Response, related_name='replies', on_delete=models.CASCADE)