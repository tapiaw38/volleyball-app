""" League serializers. """

# Django REST Framework
from rest_framework import serializers

# Models
from volleyball.league.models.league import League

# Utilities
from volleyball.utils.optimize_image import OptimizeImage


class LeagueModelSerializer(serializers.ModelSerializer):
    """ League model serializer. """

    class Meta:
        """ Meta class. """

        model = League
        fields = (
            'id',
            'name',
            'description',
            'picture',
            'is_active',
        )

    def create(self, validated_data):
        """ Create the instance. """

        picture = validated_data.pop('picture')
        optimize_picture = OptimizeImage(picture)

        league = League.objects.create(
            picture=optimize_picture.optimize(),
            **validated_data
        )

        return league