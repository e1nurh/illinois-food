from django.contrib import admin
from .models import *

admin.site.register(Tag)
admin.site.register(Story)
admin.site.register(StoryImage)
admin.site.register(Category)
admin.site.register(Comment)

# Register your models here.
