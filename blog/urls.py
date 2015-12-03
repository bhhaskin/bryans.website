from django.conf.urls import url, include
from .views import Index, Detail, CategoryListView, TagListView, YearArchive, MonthArchive, DayArchive


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryListView.as_view(), name='category'),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagListView.as_view(), name='tag'),
    url(r'^(?P<year>\d{4})/$', YearArchive.as_view(), name='yearArchive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$', MonthArchive.as_view(), name='monthArchive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$', DayArchive.as_view(), name='dayArchive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w-]+)/$', Detail.as_view(), name='detail'),
]
