""" Team views. """

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from volleyball.league.serializers.team import TeamModelSerializer

#  Models
from volleyball.league.models.team import Team

# Utilities
from volleyball.league.paginations import StandardResultsSetPagination


class TeamModelViewSet(viewsets.ModelViewSet):
    """ Team model view set. """

    queryset = Team.objects.all()
    serializer_class = TeamModelSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)