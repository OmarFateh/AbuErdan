from django import forms

from .models import Weather


class AddWeatherForm(forms.ModelForm):
    """
    Add weather record model form.
    """
    temp = forms.FloatField(
        label='Temperature', 
        widget=forms.NumberInput(attrs={
            'class':'form-control', 
            'name':'temperature', 
            'placeholder':"Temperature (from 19 to 28)",
            'step': 0.25,
            'min': 19,
            'max': 28,
            'required': True,
        })
    )
    humidity = forms.FloatField(
        label='Humidity', 
        widget=forms.NumberInput(attrs={
            'class':'form-control', 
            'name':'humidity', 
            'placeholder':"Humidity (from 35 to 65)",
            'step': 0.25,
            'min': 35,
            'max': 65,
            'required': True,
        })
    )

    class Meta:
        model  = Weather
        fields = ['temp', 'humidity']