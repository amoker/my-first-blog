from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    # 哪个模型会被用来创建这个表单
    class Meta:
        model = Post
        fields = ('title', 'text',)
