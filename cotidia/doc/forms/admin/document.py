from django import forms

from betterforms.forms import BetterModelForm

from cotidia.doc.models import Document


class DocumentAddForm(BetterModelForm):

    slug = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form__text'}),
        help_text=(
            "This field must be unique. Only accepts lowercase letters "
            "and numbers separated with hyphens.")
    )

    is_private = forms.BooleanField(
        label="Is private?",
        required=False,
        initial=True,
        help_text=(
            "Check this box if you only want admin users to access it."
        )
    )

    class Meta:
        model = Document
        exclude = []
        fieldsets = (
            ('document', {'fields': (('title', 'slug'), 'body'), 'legend': 'Document'}),
            ('access', {'fields': ('is_private',), 'legend': 'Access'}),
        )


class DocumentUpdateForm(DocumentAddForm):
    class Meta:
        model = Document
        exclude = []
