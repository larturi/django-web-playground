

from django.contrib import admin
from .models import Message, Thread


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created')


admin.site.register(Message, MessageAdmin)
admin.site.register(Thread)
