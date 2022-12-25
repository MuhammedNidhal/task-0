from django.contrib import admin
from t0.models import *

#showing the post details in the admin panel
class PostDetails(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'text',
    ]

admin.site.register(Post,PostDetails) #registering the post details to display in the admin panel