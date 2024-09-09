from django.contrib import admin
from .models import Tag, Note, Profile

# Register your models here.
admin.site.register(Tag)
admin.site.register(Note)
admin.site.register(Profile)
