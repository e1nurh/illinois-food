from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
from django.urls import reverse

class StoryImageInline(admin.TabularInline):
    model = StoryImage

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'description', 'author_link', 'length_title', 'is_published']
    list_filter = ['author', 'category']
    # list_per_page = 1
    list_display_links = ['description', ]
    # list_editable = ['title', 'author', 'is_published']
    search_fields = ['title', 'author__username']
    actions = ['make_published']
    # fields = ['title', 'description']
    fieldsets = (
        ('General info', {'fields': ('title', 'description')}),
        ('Additional info', {'fields': ('author', 'category'), 'classes': ['collapse in']})
    )
    readonly_fields = ['category']
    inlines = [StoryImageInline]
    
    def length_title(self, obj):
        return len(obj.title)
    
    def make_published(self, request, queryset):
        queryset.update(is_published=True)
    
    def author_link(self, obj):
        # return HTML link that will not be escaped
        
        return mark_safe(f"""<a href="{reverse('admin:%s_%s_change' % ('auth', 'user'), args=[obj.author.id])}">User {obj.author.username}</font></a>""")
        
        # return mark_safe(
        #     f'<a href="/admin/auth/user/{obj.author.id}/change/"><font color="red">Userdsfsdf {obj.author.username}</font></a>'
        # )

    make_published.short_description = "Make it visible"
    class Meta:
        model = Story

# admin.site.register(Tag)
# admin.site.register(Story, StoryAdmin)
admin.site.register(StoryImage)
# admin.site.register(Category)
# admin.site.register(Comment)

# Register your models here.
