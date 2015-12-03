from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from post.models import Post

class BlogPost(Post):
    slug = models.SlugField(unique_for_date="published")

    def get_publishedDate(self):
        return timezone.localtime(self.published, timezone.get_default_timezone())
    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.get_publishedDate().year, self.get_publishedDate().month, self.get_publishedDate().day, self.slug])
