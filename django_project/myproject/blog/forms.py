from django import forms 

choice = [
    ("edu", "Education"),
    ("politics", "Politics"),
    ("sports", "Sports"),
    ("games", "Games"),
    ("entertain", "Entertainment")
]

class Addblog(forms.Form):
    title = forms.CharField()
    post = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(widget=forms.Select(choices=choice))