from django.contrib import admin

from .models import Drop, DropAttachment, DropLink

admin.site.register(Drop)
admin.site.register(DropAttachment)
admin.site.register(DropLink)
