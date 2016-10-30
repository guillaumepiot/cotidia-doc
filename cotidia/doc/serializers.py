from rest_framework import serializers

from doc.models import Document


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = [
            'uuid',
            'title',
            'slug',
            'body',
            ]
