from django.contrib import admin
from .models import Post, Comment
# 在http://127.0.0.1:8000/admin/提供对以下模型的管理

admin.site.register(Post)
admin.site.register(Comment)
