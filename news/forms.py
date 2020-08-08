from django import forms
from django.forms.widgets import (
    Textarea,
    TextInput,
)

from news.models import News, Comment


class NewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-sm'}),
            'text': Textarea(attrs={'class': 'form-control form-control-sm'})
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if data.lower().find('php') != -1:
            raise forms.ValidationError('В тексте запрещено упоминать PHP!')
        return data

    def clean_title(self):
        data = self.cleaned_data['title']
        if data.lower().find('php') != -1:
            raise forms.ValidationError('В заголовке запрещено упоминать PHP!')
        return data


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': Textarea(attrs={'class': 'form-control form-control-sm'})
        }
