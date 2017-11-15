from django.db import models
from .game_category import GameCategory


class Game(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='games',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True)
    game_category = models.ForeignKey(GameCategory,
                                      related_name='games',
                                      on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name
