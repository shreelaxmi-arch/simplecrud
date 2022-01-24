from django import forms
#import model class from models.py
#from app_name.models import model_name
from flower.models import Flower

class FlowerForm(forms.ModelForm):
    class Meta:
        model=Flower
        fields="__all__"

