from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        text = forms.CharField(required=True)
        group = forms.CharField(required=False)
        fields = ('text', 'group')