from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from news.models import News, Tag


class NewsCreateForm(forms.ModelForm):
    """Форма для создания новости."""
    tags = forms.CharField(label='Тег')

    def __init__(self, *args, **kwargs):
        super(NewsCreateForm, self).__init__(*args, **kwargs)

        for field_name in ['title', 'description', 'tags']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

        self.fields['description'].widget.attrs['rows'] = '5'

    def clean(self):
        cleaned_data = super(NewsCreateForm, self).clean()

        # Добавление тегов новости
        tags_objs = []
        tags_form = cleaned_data.get('tags')
        tags_list = list(tags_form.split(', '))
        for tag in tags_list:
            t, created = Tag.objects.get_or_create(tag=tag)
            tags_objs.append(t)

        cleaned_data['tags'] = tags_objs
        return cleaned_data

    class Meta:
        model = News
        fields = ('title', 'description', 'tags')


class LoginForm(AuthenticationForm):
    """Форма для авторизации."""

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'password')
