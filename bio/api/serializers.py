from rest_framework import serializers

from bio.models import Bio, Photo


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['slackUsername', 'backend', 'age', 'bio']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'