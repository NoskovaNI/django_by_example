# The forms framework makes it
# simple to define the fields of your form, specify how they have to be displayed, and
# indicate how they have to validate input data

from django import forms
from .models import Comment


# just form
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


# modelForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
