""" New views. """

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from volleyball.league.serializers.new import NewModelSerializer

# Models
from volleyball.league.models.new import New

# Utilities
from volleyball.league.paginations import StandardResultsSetPagination


class NewModelViewSet(viewsets.ModelViewSet):
    """ New model view set. """

    queryset = New.objects.all()
    serializer_class = NewModelSerializer
    pagination_class = StandardResultsSetPagination
    #permission_classes = (IsAuthenticated,)