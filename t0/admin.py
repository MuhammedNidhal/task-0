from django.contrib import admin
from t0.models import *
class PostDetails(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'text',
    ]

admin.site.register(Post,PostDetails)