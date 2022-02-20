""" Team league views. """

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Serializers
from volleyball.league.serializers.team_league import (
    TeamLeagueModelSerializer,
    AddTeamLeagueSerializer
)

# Models
from volleyball.league.models.team_league import TeamLeague
from volleyball.league.models.league import League

# Utilities
from volleyball.league.paginations import StandardResultsSetPagination


class TeamLeagueModelViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """ Team League model view set. """

    serializer_class = TeamLeagueModelSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):

        id = kwargs.get('id')
        self.league = get_object_or_404(League, id=id)

        return super(TeamLeagueModelViewSet, self).dispatch(
            request, *args, **kwargs
        )
    
    def get_queryset(self):
        """ Get queryset. """

        return TeamLeague.objects.filter(league=self.league)

    def create(self, request, *args, **kwargs):
        """ Create new team league. """

        serializer = AddTeamLeagueSerializer(
            data=request.data,
            context={
                'league': self.league,
                'request': request
            }
        )

        serializer.is_valid(raise_exception=True)
        team_league = serializer.save()

        data = self.get_serializer(team_league).data

        return Response(data, status=status.HTTP_201_CREATED)