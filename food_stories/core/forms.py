from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):
    # name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Your name'
    #         }),)

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message'
            }),
        }
        error_messages = {
            'name': {
                'max_length': ("Error: maximum length limit is 255 characters"),
                
            },
        }

    def clean_email(self):
        value = self.cleaned_data['email'] 
        if not value.endswith('gmail.com'):
            raise forms.ValidationError('mail unvani gmail olmalidir')
        return value

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.lower()

    # def clean(self):
    #     result = super().clean()
    #     print(self.cleaned_data)
    #     value = self.cleaned_data['email'] 
    #     if not value.endswith('gmail.com'):
    #         raise forms.ValidationError('mail unvani gmail olmalidir')
    #     return result

