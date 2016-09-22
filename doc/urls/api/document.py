from django.conf.urls import url

from doc.views.api.document import (
    DocumentRetrieve,
    DocumentList
)


urlpatterns = [
    url(
        r'^retrieve/(?P<slug>[\w\-]+)$',
        DocumentRetrieve.as_view(),
        name="document-retrieve"),
    url(
        r'^list/$',
        DocumentList.as_view(),
        name="document-list"),
]
