""" Team league serializers. """

# Django REST Framework
from rest_framework import serializers

# Models
from volleyball.league.models.team_league import TeamLeague

# Serializers
from volleyball.league.serializers.team import TeamModelSerializer


class AddTeamLeagueSerializer(serializers.ModelSerializer):
    """ Team league model serializer. """

    class Meta:
        """ Meta class. """

        model = TeamLeague
        fields = (
            'id',
            'team',
            'points',
            'matches_played',
            'is_active'
        )

    def create(self, validated_data):
        """
        Create and return a new `TeamLeague` instance, 
        given the validated data.
        """

        league = self.context['league']
        team = validated_data['team']
        points = validated_data['points']
        matches_played = validated_data['matches_played']
        is_active = validated_data['is_active']

        teams = TeamLeague.objects.create(
            league=league,
            team=team,
            points=points,
            matches_played=matches_played,
            is_active=is_active
        )

        return teams


class TeamLeagueModelSerializer(serializers.ModelSerializer):
    """ Team league model serializer. """

    team = TeamModelSerializer(allow_null=True)

    class Meta:
        """ Meta class. """

        model = TeamLeague
        fields = (
            'id',
            'team',
            'points',
            'matches_played',
            'is_active'
        )