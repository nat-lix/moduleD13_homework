from django.forms import ModelForm, Textarea, Select, TextInput
from .models import *
from django import forms
from django.core.exceptions import ValidationError

class PostForm(ModelForm):
    media = forms.FileField(label='Здесь вы можете прикрепить медиа и файлы', required=False)
                            
    class Meta:
        model = Post
        fields = ['title', 'text', 'postCategory', 'media']
        widgets = {
                    'title': Textarea(attrs={'class': 'title_class'}),
                    'text': Textarea(attrs={'class': 'text_class'}),
        }

        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'postCategory': 'Категория',
        }

class PostResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={'class': 'text_class'}),
        }

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['text', ]
        widgets = {
            'text': TextInput(attrs={'class': 'text_class'}),
        }