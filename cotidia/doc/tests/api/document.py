from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from cotidia.core.utils.doc import Doc
from cotidia.account import fixtures
from cotidia.doc.factory import DocumentFactory


class DocumentAPITests(APITestCase):

    URLS = {
        'list': 'doc-api:document-list',
        'retrieve': 'doc-api:document-retrieve',
    }

    @fixtures.normal_user
    def setUp(self):
        self.doc = Doc()
        self.private_docs = DocumentFactory.create_batch(10, is_private=True)
        self.public_docs = DocumentFactory.create_batch(10, is_private=False)

    def test_list_private(self):
        """List documents as an authenticated user."""

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.normal_user_token.key)

        url = reverse(self.URLS['list'])

        payload = {}

        response = self.client.get(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 20)

        content = {
            'title': "List documents",
            'http_method': 'GET',
            'url': url,
            'payload': payload,
            'response': response.data[:3]
        }

        self.doc.display_section(content)

    def test_list_public(self):
        """List documents as an anonymous user."""

        url = reverse(self.URLS['list'])

        payload = {}

        response = self.client.get(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_retrieve_private(self):
        """Retrieve a document as an authenticated user."""

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.normal_user_token.key)

        private_doc = DocumentFactory.create(is_private=True)

        url = reverse(self.URLS['retrieve'], kwargs={'slug': private_doc.slug})

        payload = {}

        response = self.client.get(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['uuid'], str(private_doc.uuid))
        self.assertEqual(response.data['title'], private_doc.title)
        self.assertEqual(response.data['slug'], private_doc.slug)
        self.assertEqual(response.data['body'], private_doc.body)

        content = {
            'title': "Retrieve document",
            'http_method': 'GET',
            'url': url,
            'payload': payload,
            'response': response.data
        }

        self.doc.display_section(content)

    def test_retrieve_private_anonymous(self):
        """Test an anonymous user can't retrieve a private document."""

        private_doc = DocumentFactory.create(is_private=True)

        url = reverse(self.URLS['retrieve'], kwargs={'slug': private_doc.slug})

        payload = {}

        response = self.client.get(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_public_anonymous(self):
        """Test an anonymous user can retrieve a public document."""

        public_doc = DocumentFactory.create(is_private=False)

        url = reverse(self.URLS['retrieve'], kwargs={'slug': public_doc.slug})

        payload = {}

        response = self.client.get(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
