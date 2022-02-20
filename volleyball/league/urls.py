""" Record URLs. """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import league as league_views
from .views import new as new_views
from .views import team as team_views
from .views import team_league as team_league_views
from .views import match as match_views

router = DefaultRouter()

router.register(r'new', new_views.NewModelViewSet, basename='new')
router.register(r'league', league_views.LeagueModelViewSet, basename='league')
router.register(r'team', team_views.TeamModelViewSet, basename='team')
router.register(
    r'league/(?P<id>[0-9]+)/teams',
    team_league_views.TeamLeagueModelViewSet,
    basename='team_league'
)
router.register(r'match', match_views.MatchModelViewSet, basename='match')

urlpatterns = [] + router.urls