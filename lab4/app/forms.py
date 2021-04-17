"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from.models import Comment
from.models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class RatingForm(forms.Form):
    userName = forms.CharField(label = "Ваше имя", min_length = 5, max_length = 50, required = True)
    userMail = forms.EmailField(label = "Ваш e-mail", min_length = 5, max_length = 20, required = True)
    age = forms.ChoiceField(label = "Вам есть 18 лет?", choices = [('1','Да'), ('2','Нет')], widget = forms.RadioSelect)
    what_like = forms.ChoiceField(label= "Что именно вам понравилось на сайте?", choices = (('1','Внешний вид'),('2','Стабильная работа'),('3','Интересный контент')))
    notice = forms.BooleanField(label = 'Получать новости сайта на e-mail?',)
    MoreInf = forms.CharField(label = 'Опишите подробнее, что имненно вам понравилось?', widget = forms.Textarea(attrs={'rows':4, 'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}
