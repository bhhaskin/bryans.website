from django.views.generic import ArchiveIndexView
from .models import Drop

class Index(ArchiveIndexView):
    template_name = "stream/index.html"
    date_field = 'created'
    model = Drop
    context_object_name = "objects"
    allow_empty = True
