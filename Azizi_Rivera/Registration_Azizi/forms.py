from django import forms
from Registration_Azizi.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta():
        model=Registration
        fields=('First_Name','Last_Name','Email_Address','Mobile_Number','Intereset')

        widgets={
        'First_Name':forms.TextInput(attrs={'class':'w3-input w3-border'}),
        'Last_Name':forms.TextInput(attrs={'class':'w3-input w3-border'}),
        'Email_Address':forms.TextInput(attrs={'class':'w3-input w3-border'}),
        'Mobile_Number':forms.TextInput(attrs={'class':'w3-input w3-border','placeholder':'Please Start with + and the Country Code Example : +971'}),
        # 'Intereset':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        'Intereset':forms.Textarea(attrs={'class':'w3-input w3-border','placeholder':'Please Share your Intereset Here ..'}),
        }
