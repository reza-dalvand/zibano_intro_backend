"""
Forms for zibano_intro website.
"""

from django import forms


class ContactForm(forms.Form):
    """فرم تماس با ما"""

    full_name = forms.CharField(
        max_length=100,
        required=True,
    )
    phone = forms.CharField(
        max_length=20,
        required=True,
    )
    email = forms.EmailField(
        required=False,
    )
    subject = forms.CharField(
        max_length=200,
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
    )