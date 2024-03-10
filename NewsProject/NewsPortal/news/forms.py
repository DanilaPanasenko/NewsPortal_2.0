from django import forms
from .models import Post, Author, User
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):


   class Meta:
       model = Post
       fields = [
           'author',
           'headline',
           'text',
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
