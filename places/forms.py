from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label='Назва місця',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Наприклад: Парк Кіото'
        })
    )
    description = forms.CharField(
        required=False,
        label='Опис',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Чому тобі тут подобається?'
        })
    )
    place_type = forms.CharField(
        max_length=50,
        required=False,
        label='Тип місця',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'парк / кафе / музей / ринок...'
        })
    )
    location = forms.CharField(
        max_length=150,
        required=False,
        label='Локація',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Адреса або район'
        })
    )
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        required=True,
        label='Особистий рейтинг (1–5)',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
            'max': 5
        })
    )