from django import forms

class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=0, max_value=10)
    title = forms.CharField(label="Title", max_length=63)
    comment = forms.CharField(label="Comment", max_length=65535)
    mid = forms.CharField(required=False)
    rid = forms.CharField(required=False)
