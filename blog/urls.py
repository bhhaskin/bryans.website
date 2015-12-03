from django.conf.urls import url, include
from .views import Index, Detail


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
     url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w-]+)/$', Detail.as_view(), name='detail'),
]
