from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views

urlpatterns = patterns('',
    url(r'^', include('core.urls')),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<url>.*/)$', views.flatpage),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
