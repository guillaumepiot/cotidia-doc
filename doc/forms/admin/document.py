from django import forms

from doc.models import Document


class DocumentAddForm(forms.ModelForm):

    title = forms.CharField(
        label='',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form__text'})
        )

    slug = forms.CharField(
        label='',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form__text'}),
        help_text=(
            "This field must be unique. Only accepts lowercase letters "
            "and numbers separated with hyphens.")
        )

    body = forms.CharField(
        label='',
        widget=forms.HiddenInput,
        required=False
        )

    is_private = forms.BooleanField(
        label="Private",
        required=False,
        initial=True,
        help_text=(
            "Check this box if you only want admin users to access it."
            ))

    class Meta:
        model = Document
        exclude = []


class DocumentUpdateForm(DocumentAddForm):
    class Meta:
        model = Document
        exclude = []
