from django.contrib import admin
from .models import Subscriber, Contact

# class SubscriberAdmin(admin.ModelAdmin):
#     list_display = ('email', 'is_active', 'created_at')
#     fields = ('email', 'is_active', 'created_at')
#     list_editable = ('email', 'is_active',)


admin.site.register(Subscriber)
admin.site.register(Contact)

# Register your models here.
