from django.views.generic import TemplateView
from blog.models import BlogPost
from stream.models import Drop
class Index(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
         context = super(Index, self).get_context_data(**kwargs)
         context['posts'] = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public')[:2]
         context['stream'] = Drop.objects.all()[:2]
         return context
