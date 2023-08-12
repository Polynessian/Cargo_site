from typing import Any, Mapping, Optional, Type, Union
from django.forms.utils import ErrorList
from .models import Review, Photo
from django import forms 
from django.forms import ModelForm, TextInput, Textarea

from captcha.fields import CaptchaField
from captcha.widgets import ReCaptchaV3 
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from snowpenguin.django.recaptcha3.widgets import ReCaptchaHiddenInput

class ReviewsForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    captcha = ReCaptchaField()
    class Meta:
        model = Review
        
        fields = ['title', 'way', 'content', 'captcha']
        widgets = {
            'title': TextInput(attrs={
                'name': 'title_name',
                'type': 'text',
                'id': 'name_button',
                'placeholder': 'Ваше имя/ Your name'
                }),       
            'way': TextInput(attrs={
                'name': 'test_way',
                'type': 'text',
                'id': 'r_button',
                'placeholder': 'Рейс / Flight'
                }),
            'content': Textarea(attrs={
                'rows':4,
                'cols':15,
                'name': 'test_content',
                'id': 'message',
                'placeholder': 'Как все прошло?/ How did the deal go?'
                }),
            
            }


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
    
    
class PhotoForm(forms.FileField):
    
    class Meta:
        model = Photo
        fields = ['photo']
        widgets = {'photo': MultipleFileInput(attrs={                                     
                'name': 'file',
                'type': 'file',
                'id': 'file',
                'class': 'field input__file'
                })}
       
    def __init__(self, *args, **kwargs):  
        kwargs.setdefault('widget', MultipleFileInput())
        super(PhotoForm, self).__init__(*args, **kwargs)
        
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

   
class FileFieldForm(forms.Form):   
        
    photos = PhotoForm()