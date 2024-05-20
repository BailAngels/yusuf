from django import forms

from apps.posts.models import Post
from apps.tags.models import Tag


class PostCreateForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget = forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ['title','description','image','tag']


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','description','image']    