""" Team serializers. """

# Django REST Framework
from rest_framework import serializers

# Models
from volleyball.league.models.team import Team


class TeamModelSerializer(serializers.ModelSerializer):
    """ Team model serializer. """

    class Meta:
        """ Meta class. """

        model = Team
        fields = (
            'id',
            'name',
            'description',
            'picture',
            'is_active',
        )