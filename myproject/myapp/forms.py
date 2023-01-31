from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control'}
        self.fields['college'].widget.attrs = {'class': 'form-control'}
        self.fields['roll_number'].widget.attrs = {'class': 'form-control'}
        self.fields['comment'].widget.attrs = {'class': 'form-control'}