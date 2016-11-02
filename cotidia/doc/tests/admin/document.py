from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

from cotidia.account.models import User
from cotidia.doc.models import Document
from cotidia.doc.factory import DocumentFactory


@override_settings(ACCOUNT_FORCE_ADMIN_TWO_FACTOR=False)
class DocumentAdminTests(TestCase):

    def setUp(self):
        """Create the default data."""

        # Create a super user
        self.user = User.objects.create(
            username="admin",
            email="admin@test.com",
            is_superuser=True,
            is_active=True)
        self.user.set_password("demo")
        self.user.save()

        # Create a default object, to use with update, retrieve, list & delete
        self.object = DocumentFactory.create()

        # Create the client and login the user
        self.c = Client()
        self.c.login(username=self.user.username, password='demo')

    def test_add_document(self):
        """Test that we can add a new object."""

        url = reverse('doc-admin:document-add')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            'title': "The sunset",
            'slug': "the-sunset",
            'body': "Vestibulum urna augue, aliquet id tortor eu.",
            'is_private': True
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Document.objects.filter().latest('id')
        self.assertEqual(obj.title, "The sunset")
        self.assertEqual(obj.slug, "the-sunset")
        self.assertEqual(
            obj.body,
            "Vestibulum urna augue, aliquet id tortor eu."
            )
        self.assertEqual(obj.is_private, True)

    def test_update_document(self):
        """Test that we can update an existing object."""

        url = reverse(
            'doc-admin:document-update',
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            'title': "The sunset",
            'slug': "the-sunset",
            'body': "Vestibulum urna augue, aliquet id tortor eu.",
            'is_private': False
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Document.objects.get(id=self.object.id)
        self.assertEqual(obj.title, "The sunset")
        self.assertEqual(obj.slug, "the-sunset")
        self.assertEqual(
            obj.body,
            "Vestibulum urna augue, aliquet id tortor eu."
            )
        self.assertEqual(obj.is_private, False)

    def test_retrieve_document(self):
        """Test that we can retrieve an object from its ID."""

        url = reverse(
            'doc-admin:document-detail',
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_document(self):
        """Test that we can list objects."""

        url = reverse('doc-admin:document-list')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_document(self):
        """Test that we can delete an object."""

        url = reverse(
            'doc-admin:document-delete',
            kwargs={
                'pk': self.object.id
                }
            )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Action detail with POST call
        response = self.c.post(url)
        self.assertEqual(response.status_code, 302)

        # Test that the record has been deleted
        obj = Document.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
