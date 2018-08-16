import django_filters

from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminCreateView,
    AdminUpdateView,
    AdminDeleteView
)
from cotidia.doc.models import Document
from cotidia.doc.forms.admin.document import (
    DocumentAddForm,
    DocumentUpdateForm)


class DocumentFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Title"
    )

    class Meta:
        model = Document
        fields = ['title']


class DocumentList(AdminListView):
    model = Document
    columns = (
        ('Title', 'title'),
        ('Slug', 'slug'),
        ('Access', 'is_private'),
    )
    filterset = DocumentFilter


class DocumentDetail(AdminDetailView):
    model = Document
    fieldsets = [
        {
            "legend": "Document",
            "fields": [
                [
                    {
                        "label": "Title",
                        "field": "title",
                    },
                    {
                        "label": "Slug",
                        "field": "slug",
                    }

                ],
                {
                    "label": "Body",
                    "field": "body",
                }
            ]
        },
        {
            "legend": "Access",
            "fields": [
                {
                    "label": "Is private?",
                    "field": "is_private",
                }
            ]
        }
    ]


class DocumentCreate(AdminCreateView):
    model = Document
    form_class = DocumentAddForm


class DocumentUpdate(AdminUpdateView):
    model = Document
    form_class = DocumentUpdateForm


class DocumentDelete(AdminDeleteView):
    model = Document
