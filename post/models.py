from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField('title', max_length=200)
    content = models.TextField('content', blank=True)
    excerpt = models.TextField('excerpt', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User)
    VISIBILITY_CHOICES = (
        ('Public', 'Public'),
        ('Password protected', 'Password protected'),
        ('Private', 'Private'),
    )
    visibility = models.CharField(max_length=18,
                                      choices=VISIBILITY_CHOICES,
                                      default='Public')
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Pending Review', 'Pending Review'),
        ('Draft', 'Draft'),
    )
    status = models.CharField(max_length=14,
                                      choices=STATUS_CHOICES,
                                      default='Draft')
    class Meta:

        abstract = True
        ordering = ['-published']

    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=70, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='categoryParent')
    class Meta:
        abstract = True
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __unicode__(self):
        return self.category

class Tag(models.Model):
    tag = models.CharField(max_length=70, unique=True)
    class Meta:
        abstract = True
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['tag']
    def __unicode__(self):
        return self.tag
