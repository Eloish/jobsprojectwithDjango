from django.contrib import admin

# Register your models here.

from .models import conversationMessage

admin.site.register(conversationMessage)