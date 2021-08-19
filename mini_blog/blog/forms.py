from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CommentForm(forms.Form):
    comment_text=forms.CharField(max_length=1000,label='Description',help_text='Enter comment about blog here')

    def clean_comment_text(self):
        data=self.cleaned_data['comment_text']

        if data == '' or data==' ':
            raise ValidationError(_('Strange Comment'))
            
        return data