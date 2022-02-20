""" New serializers. """

# Django REST Framework
from rest_framework import serializers

# Models
from volleyball.league.models.new import New

# Serializers
from volleyball.league.serializers.league import LeagueModelSerializer

# Utilities
from volleyball.utils.optimize_image import OptimizeImage


class NewModelSerializer(serializers.ModelSerializer):
    """ New model serializer. """

    class Meta:
        """ Meta class. """

        model = New
        fields = (
            'id',
            'title',
            'sub_title',
            'content',
            'league',
            'picture',
            'created',
            'modified',
        )
    
    def create(self, validated_data):
        """ Create the instance. """

        picture = validated_data.pop('picture')
        optimize_picture = OptimizeImage(picture)

        new = New.objects.create(
            picture=optimize_picture.optimize(),
            **validated_data
        )

        return new
    
    def to_representation(self, instance):
        """ Representation of the instance. """

        representation = super().to_representation(instance)
        representation['league'] = LeagueModelSerializer(instance.league).data
        return representation