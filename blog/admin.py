from django.contrib import admin
from .models import Post

# Registers Post model with admin site
admin.site.register(Post)