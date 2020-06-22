# blogging/forms.py

from django.forms import ModelForm
from myapp.models import Comment


class MyCommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['title', 'text', 'notes']
