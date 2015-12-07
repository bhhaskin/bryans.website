from django.views.generic import ArchiveIndexView, DateDetailView, ListView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import BlogPost, BlogCategory, BlogTag

class Index(ArchiveIndexView):
    template_name = "blog/index.html"
    paginate_by = 5
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

class CategoryListView(ListView):
    template_name = "blog/category.html"
    paginate_by = 5
    context_object_name = "objects"
    def get_queryset(self):
        if self.kwargs['slug'] == "uncategorized":
            self.queryset = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public').filter(categories=None)
            return super(ListView, self).get_queryset()
        else:
            category = get_object_or_404(BlogCategory, slug=self.kwargs['slug'])
            self.queryset = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public').filter(categories__in=[category])
            return super(ListView, self).get_queryset()
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        if self.kwargs['slug'] != "uncategorized":
            context['category'] = get_object_or_404(BlogCategory, slug=self.kwargs['slug'])
        return context

class TagListView(ListView):
    template_name = "blog/tag.html"
    paginate_by = 5
    context_object_name = "objects"
    def get_queryset(self):
        tag = get_object_or_404(BlogTag, slug=self.kwargs['slug'])
        self.queryset = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public').filter(tags__in=[tag])
        return super(ListView, self).get_queryset()
    def get_context_data(self, **kwargs):
         context = super(TagListView, self).get_context_data(**kwargs)
         context['tag'] = get_object_or_404(BlogTag, slug=self.kwargs['slug'])
         return context

class YearArchive(YearArchiveView):
    template_name = "blog/year.html"
    paginate_by = 5
    date_field = 'published'
    queryset = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public')
    context_object_name = "objects"
    def get_context_data(self, **kwargs):
         context = super(YearArchive, self).get_context_data(**kwargs)
         context['year'] = self.kwargs['year']
         return context

class MonthArchive(MonthArchiveView):
    template_name = "blog/month.html"
    paginate_by = 5
    date_field = 'published'
    queryset = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public')
    context_object_name = "objects"
    month_format = '%m'
    def get_context_data(self, **kwargs):
         context = super(MonthArchive, self).get_context_data(**kwargs)
         context['month'] = self.kwargs['month']
         return context

class DayArchive(DayArchiveView):
    template_name = "blog/day.html"
    paginate_by = 5
    date_field = 'published'
    queryset = BlogPost.objects.filter(status__exact='Published').filter(status__exact='Published').filter(visibility__exact='Public')
    context_object_name = "objects"
    month_format = '%m'
    day_format = '%d'
    def get_context_data(self, **kwargs):
         context = super(DayArchive, self).get_context_data(**kwargs)
         context['day'] = self.kwargs['day']
         return context
