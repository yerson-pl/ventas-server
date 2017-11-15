from django.db import models
from .player import Player
from .game import Game


class PlayerScore(models.Model):
    player = models.ForeignKey(Player,
                               related_name='scores',
                               on_delete=models.CASCADE)
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE)
    score = models.ImageField()
    score_date = models.DateTimeField()

    class Meta:
        # order by score descending
        ordering = ('-score',)
