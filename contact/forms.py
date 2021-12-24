from django import forms
from contact.models import FeedBack


class FeedBackForm(forms.ModelForm):
    # name = forms.CharField(label='Your name', max_length=100)
    # surname = forms.CharField(label='Your surname', max_length=100)
    # comment = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea
    (attrs={'class': 'text_area_form',
            'id': 'some_id'}))
    class Meta:
        model = FeedBack
        fields = "__all__"