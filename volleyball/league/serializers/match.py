
""" Match serializers. """

# Django REST Framework
from rest_framework import serializers

# Models
from volleyball.league.models.match import Match

# Serializers
from volleyball.league.serializers.league import LeagueModelSerializer
from volleyball.league.serializers.team import TeamModelSerializer

class MatchModelSerializer(serializers.ModelSerializer):
    """ Match model serializer. """

    class Meta:
        """ Meta class. """

        model = Match
        fields = (
            'id',
            'league',
            'home_team',
            'away_team',
            'date',
            'is_active',
        )

    def to_representation(self, instance):
        """ Representation of the instance. """

        representation = super().to_representation(instance)
        representation['league'] = LeagueModelSerializer(instance.league).data
        representation['home_team'] = TeamModelSerializer(instance.home_team).data
        representation['away_team'] = TeamModelSerializer(instance.away_team).data
        return representation