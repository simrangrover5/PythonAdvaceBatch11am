from django import forms

class Login(forms.Form):  # inherited the Form class to inherit its features
    email = forms.EmailField(required=True, label="Enter Your Email")
    password = forms.CharField(widget=forms.PasswordInput, max_length=300, required=True, label="Enter Your Password")

class Signup(forms.Form):
    fname = forms.CharField(required=True, max_length=100, label="First Name")
    lname = forms.CharField(required=True, max_length=100, label="Last Name")
    email = forms.EmailField(required=True, max_length=200)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    con_password = forms.CharField(required=True, widget=forms.PasswordInput, label="Confirm Password")
    image = forms.ImageField()

class GetEmail(forms.Form):
    email = forms.EmailField(required=True, max_length=200)

class Getotp(forms.Form):
    otp = forms.CharField(max_length=10)

class Newpass(forms.Form):
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    con_password = forms.CharField(required=True, widget=forms.PasswordInput, label="Confirm Password")

# <input type="email" name="email">
# widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Email'})
