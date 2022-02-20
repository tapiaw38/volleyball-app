""" League views. """

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from volleyball.league.serializers.league import LeagueModelSerializer

# Models
from volleyball.league.models.league import League

# Utilities
from volleyball.league.paginations import StandardResultsSetPagination


class LeagueModelViewSet(viewsets.ModelViewSet):
    """ League model view set. """

    queryset = League.objects.all()
    serializer_class = LeagueModelSerializer
    pagination_class = StandardResultsSetPagination
    #permission_classes = (IsAuthenticated,)