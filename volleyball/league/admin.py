""" League admin. """

# Django
from django.contrib import admin

# Models
from volleyball.league.models import (
    Person,
    Player,
    Team,
    TeamLeague,
    League,
    Match,
    New
)

admin.site.register(Person)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(TeamLeague)
admin.site.register(League)
admin.site.register(Match)
admin.site.register(New)