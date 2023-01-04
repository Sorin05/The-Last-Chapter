from django import forms
from .models import BlogPost, Comment
from .widgets import CustomClearableFileInput


class BlogPostForm(forms.ModelForm):
    """
    Class defining the form
    """
    class Meta:
        model = BlogPost
        fields = (
            'title', 'content', 'image_url', 'image',
        )
        exclude = ['owner', 'created_at']

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )


class CommentForm(forms.ModelForm):
    """
    comments form
    """
    class Meta:
        model = Comment
        fields = (
            'comment_body',
        )

    def __init__(self, *args, **kwargs):
        """
        Initialize method for the form

        """
        super().__init__(*args, **kwargs)
        self.fields['comment_body'].label = 'Post your comment:'
