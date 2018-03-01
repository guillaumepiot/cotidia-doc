from django.urls import reverse


def admin_menu(context):
    return [
        {
            'icon': 'file',
            'text': 'Documents',
            'url': reverse('doc-admin:document-list'),
            'permissions': ['doc.add_document', 'doc.change_document'],
        }
    ]
