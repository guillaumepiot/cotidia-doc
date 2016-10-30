from django.conf.urls import url

from cotidia.doc.views.admin.document import (
    DocumentList,
    DocumentCreate,
    DocumentDetail,
    DocumentUpdate,
    DocumentDelete
)


urlpatterns = [
    url(
        r'^$',
        DocumentList.as_view(),
        name='document-list'),
    url(
        r'^add/$',
        DocumentCreate.as_view(),
        name='document-add'),
    url(
        r'^(?P<pk>[\d]+)/$',
        DocumentDetail.as_view(),
        name='document-detail'),
    url(
        r'^(?P<pk>[\d]+)/update/$',
        DocumentUpdate.as_view(),
        name='document-update'),
    url(
        r'^(?P<pk>[\d]+)/delete/$',
        DocumentDelete.as_view(),
        name='document-delete'),
]
