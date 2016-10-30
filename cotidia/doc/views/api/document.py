from rest_framework import generics
from rest_framework import permissions

from cotidia.doc.serializers import DocumentSerializer
from cotidia.doc.models import Document


class DocumentMixin(object):

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Document.objects.filter()
        else:
            # Return only public document if the user is not authenticated.
            return Document.objects.filter(is_private=False)

    def get_serializer_class(self):
        return DocumentSerializer

    def get_permissions(self):
        return []


class DocumentRetrieve(DocumentMixin, generics.RetrieveAPIView):
    lookup_field = 'slug'
    lookup_field_kwarg = 'slug'


class DocumentList(DocumentMixin, generics.ListAPIView):
    pass
