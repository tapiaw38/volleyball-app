""" Match views. """

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from volleyball.league.serializers.match import MatchModelSerializer

# Models
from volleyball.league.models.match import Match

# Utilities
from volleyball.league.paginations import StandardResultsSetPagination


class MatchModelViewSet(viewsets.ModelViewSet):
    """ Match model view set. """

    queryset = Match.objects.all()
    serializer_class = MatchModelSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)