from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages

from cotidia.account.utils import StaffPermissionRequiredMixin
from cotidia.doc.models import Document
from cotidia.doc.forms.admin.document import (
    DocumentAddForm,
    DocumentUpdateForm)


class DocumentList(StaffPermissionRequiredMixin, ListView):
    model = Document
    template_name = 'admin/doc/document/document_list.html'
    permission_required = 'doc.change_document'
    paginate_by = 25

    def get_queryset(self):
        queryset = Document.objects.filter()
    #     queryset = Invoice.objects.filter()

    #     status = self.request.GET.get('status')

    #     if status == 'PAID':
    #         queryset = queryset.filter(paid=True)
    #     elif status == 'UNPAID':
    #         queryset = queryset.exclude(paid=True)
    #     elif status == 'NEW':
    #         queryset = queryset.filter(pay_date=None)

        return queryset

    # def get_context_data(self, **kwargs):

    #     # Call the base implementation first to get a context
    #     context = super(InvoiceList, self).get_context_data(**kwargs)
    #     # The url params are used to add the url if the pagination is
    #     #enabled, so the filtering data is not lost when changing page
    #     context['url_params'] = ""

    #     # Add get params
    #     if self.request.GET.get('status'):
    #         context['status'] = self.request.GET.get('status')
    #         context['url_params'] +=  "status=%s&" % context['status']

    #     return context


class DocumentDetail(StaffPermissionRequiredMixin, DetailView):
    model = Document
    template_name = 'admin/doc/document/document_detail.html'
    permission_required = 'doc.change_document'


class DocumentCreate(StaffPermissionRequiredMixin, CreateView):
    model = Document
    form_class = DocumentAddForm
    template_name = 'admin/doc/document/document_form.html'
    permission_required = 'doc.add_document'

    def get_success_url(self):
        messages.success(self.request, 'Document has been created.')
        return reverse(
            'doc-admin:document-detail',
            kwargs={'pk': self.object.id})


class DocumentUpdate(StaffPermissionRequiredMixin, UpdateView):
    model = Document
    form_class = DocumentUpdateForm
    template_name = 'admin/doc/document/document_form.html'
    permission_required = 'doc.change_document'

    def get_success_url(self):
        messages.success(self.request, 'Document details have been updated.')
        return reverse(
            'doc-admin:document-detail',
            kwargs={'pk': self.object.id})


class DocumentDelete(StaffPermissionRequiredMixin, DeleteView):
    model = Document
    permission_required = 'doc.delete_document'
    template_name = 'admin/doc/document/document_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Document has been deleted.')
        return reverse('doc-admin:document-list')
