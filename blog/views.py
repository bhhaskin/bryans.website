from django.views.generic import ArchiveIndexView, DateDetailView
from django.http import Http404
from .models import BlogPost

class Index(ArchiveIndexView):
    template_name = "blog/index.html"
    date_field = 'published'
    queryset = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public')
    context_object_name = "objects"

class Detail(DateDetailView):
    template_name = "blog/detail.html"
    context_object_name = 'object'
    model = BlogPost
    date_field = 'published'
    month_format = '%m'
    day_format = '%d'

    def render_to_response(self, context, **response_kwargs):
        if self.object.status != 'Published' and self.request.user.is_staff is False:
            raise Http404
        return super(DateDetailView, self).render_to_response(context, **response_kwargs)
