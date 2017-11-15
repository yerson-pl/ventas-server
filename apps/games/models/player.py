from django.db import models


class Player (models.Model):
    MALE = 'M',
    FEMALE = 'F',
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, default='', unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE,)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name