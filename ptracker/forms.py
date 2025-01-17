import datetime

from django import forms

from .models import Pregnancy

class PregnancyForm(forms.ModelForm):
    class Meta:
        model = Pregnancy
        fields = ['user_name', 'lmp_date']  # You can add 'baby_birth_date' if you want the user to input it manually

    # You can add custom validation or widgets if needed
    def clean_lmp_date(self):
        lmp_date = self.cleaned_data.get('lmp_date')
        if lmp_date > datetime.date.today():
            raise forms.ValidationError("LMP date cannot be in the future.")
        return lmp_date
