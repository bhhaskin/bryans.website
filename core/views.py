from django.views.generic import TemplateView
from blog.models import BlogPost
class Index(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
         context = super(Index, self).get_context_data(**kwargs)
         context['posts'] = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public')[:1]
         return context
