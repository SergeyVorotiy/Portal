from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


article = 'A'
news = 'N'
TYPES = [
    (news, 'Новость'),
    (article, 'Статья')
]
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    position = models.CharField(max_length=1, choices=TYPES)
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', through='PostCategory')
    heading = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.text[:124]}..."


class PostCategory(models.Model):
    post = models.ForeignKey('Category', on_delete=models.CASCADE)
    category = models.ForeignKey('Post', on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()