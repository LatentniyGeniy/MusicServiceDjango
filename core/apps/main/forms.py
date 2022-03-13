from .models import Album

from django.forms import ModelForm, TextInput, DateInput


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ["title", "release_date", "release_type", "picture_link"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название альбома',
            }),
            "release_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату выхода',
            }),
            "release_type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тип релиза',
            }),
            "picture_link": TextInput(attrs={
                'class': 'form-control',
            }),
        }
