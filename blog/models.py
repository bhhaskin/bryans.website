from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from post.models import Post, Category, Tag

class BlogPost(Post):
    slug = models.SlugField(unique_for_date="published")
    categories = models.ManyToManyField("BlogCategory", null=True, blank=True)
    tags = models.ManyToManyField("BlogTag", null=True, blank=True)

    def get_publishedDate(self):
        return timezone.localtime(self.published, timezone.get_default_timezone())
    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.get_publishedDate().year, self.get_publishedDate().month, self.get_publishedDate().day, self.slug])

class BlogCategory(Category):
    slug = models.SlugField(null=True, unique=True)
    def get_absolute_url(self):
        return reverse('blog:category', args=[self.slug])


class BlogTag(Tag):
    slug = models.SlugField(null=True, unique=True)
    def get_absolute_url(self):
        return reverse('blog:tag', args=[self.slug])
