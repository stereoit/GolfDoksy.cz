from django import forms
import re

phone_regex = re.compile('^[\+0-9 ]+$')

class EmailInput(forms.TextInput):
    input_type = 'email'

class TelInput(forms.TextInput):
    input_type = 'tel'

class ContactForm(forms.Form):

    sender = forms.EmailField(
        widget=EmailInput(attrs={'class':'form-textfield'}),
        max_length=255,
        required=True
    )
    phone = forms.CharField(
        widget=TelInput(attrs={'class':'form-textfield'}),
        max_length=40,
        required=False
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-textarea','rows':'6','cols':'6'}),
        required=True,
        min_length=3
    )
    cc_myself = forms.BooleanField(required=False, initial=True)

    def clean(self):
        phone = self.cleaned_data.get('phone')
        if phone and phone_regex.match(phone) is None:
            self._errors['phone'] = self.error_class([self.phone_error_invalid])
        return self.cleaned_data
