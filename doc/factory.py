import uuid
import factory
import factory.fuzzy
import string


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'doc.Document'

    uuid = factory.LazyAttribute(lambda o: uuid.uuid4())
    title = factory.Faker('name')
    slug = factory.Sequence(lambda n: 'document-%04d' % n)
    body = factory.fuzzy.FuzzyText(
        length=12, chars=string.ascii_letters, prefix=''
        )
    is_private = True
