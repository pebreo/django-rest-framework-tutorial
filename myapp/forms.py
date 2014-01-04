from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing

#import floppyforms as forms
#from .models import Thing


#class ThingForm(forms.ModelForm):
#    class Meta:
#        model = Thing
