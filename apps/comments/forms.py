from django import forms 

from apps.comments.models import Comment


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'post', 'parent']


class CommentUpdateForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ['text']