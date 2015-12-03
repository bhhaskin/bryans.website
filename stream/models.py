from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Drop(models.Model):
    attachment = models.OneToOneField("DropAttachment", null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField('content', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    class Meta:
        ordering = ['-created']

class DropAttachment(models.Model):
    limit = models.Q(app_label = 'blog', model = 'BlogPost') | models.Q(app_label = 'stream', model = 'DropLink')
    content_type = models.ForeignKey(ContentType, limit_choices_to = limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class DropLink(models.Model):
    text = models.CharField('title', max_length=200)
    link = models.URLField()

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
    def __unicode__(self):
        return self.text
