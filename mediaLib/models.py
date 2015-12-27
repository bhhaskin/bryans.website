from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .utils import get_file_path

class MediaObj(models.Model):
    limit = models.Q(app_label = 'mediaLib', model = 'MediaImage')
    content_type = models.ForeignKey(ContentType, limit_choices_to = limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    class Meta:
        ordering = ['-created']

class MediaImage(models.Model):
    image = models.ImageField(upload_to = get_file_path,
                                blank = True,
                                null = True )
    # title
    # caption
    # altText
    # description
