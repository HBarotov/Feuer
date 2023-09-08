from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Max 100 Characters"}),
    )

    class Meta:
        model = Comment
        fields = ("comment",)
