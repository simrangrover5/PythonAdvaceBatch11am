from django import forms

class Login(forms.Form):  # inherited the Form class to inherit its features
    email = forms.EmailField(required=True, label="Enter Your Email")
    password = forms.CharField(widget=forms.PasswordInput, max_length=300, required=True, label="Enter Your Password")


# <input type="email" name="email">
# widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Email'})
