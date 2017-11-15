from django.contrib import admin
from apps.games.models.game import Game
from apps.games.models.game_category import GameCategory
from apps.games.models.player import Player
from apps.games.models.player_score import PlayerScore

# Register your models here.

admin.site.register(Game)
admin.site.register(GameCategory)
admin.site.register(Player)
admin.site.register(PlayerScore)
