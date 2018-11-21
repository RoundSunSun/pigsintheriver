from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


#分类表
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#标签表
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#文章表
class Post(models.Model):
    #标题和正文
    title = models.CharField(max_length=70)
    body = models.TextField()

    #创建时间，末次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk' : self.pk})
