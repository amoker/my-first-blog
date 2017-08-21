from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    # 哪个模型会被用来创建这个表单
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
