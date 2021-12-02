from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserInformationUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		#fields = ('first_name', 'last_name', 'email', )
		fields = ('email', )


class ContactForm(forms.Form):
    Subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label="Your e-mail adress")
    #photo = forms.ImageField()
    receive_copy = forms.BooleanField(label="Receive a copy", required=False)
    
    
    def clean_message(self):

        message = self.cleaned_data['message']

        if "Pimentech is not good" in message:

            raise forms.ValidationError("Are you sure? Please check our website: pimentech.fr !")

        return message   
    
        
        
