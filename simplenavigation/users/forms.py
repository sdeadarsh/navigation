from django import forms

class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email', \
                    widget=forms.EmailInput(
                        attrs={
                        'placeholder': 'your.email@example.com',
                        'required': 'required'
                        }
                    )
    )
    password = forms.CharField(label='Password', \
                    widget=forms.PasswordInput(
                        attrs={
                        'placeholder': '**********',
                        'required': 'required'
                        }
                    )
    )
