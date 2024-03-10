from django import forms
from .models import Post, Author, User
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):


   class Meta:
       model = Post
       fields = [
           'author',
           #'type',
           #'datetime_in', django.core.exceptions.FieldError: 'datetime_in' cannot be specified for Post model form as it is a non-editable field
           'headline',
           'text',
           #'rating',
           'category',
       ]

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       if text is not None and len(text) < 20:
           raise ValidationError({
               "text": "Описание не может быть менее 20 символов."
           })

       headline = cleaned_data.get("headline")
       if headline == text:
           raise ValidationError(
               {
                   "text": "текст новости не должен совпадать с заголовком"
               }
           )

       return cleaned_data
