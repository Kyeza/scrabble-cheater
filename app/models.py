from django.db import models


class ScrabbleWord(models.Model):
    word = models.CharField(max_length=256)
    score = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.word)

    class Meta:
        ordering = ['word', 'score']
        verbose_name = 'Scrabble Dictionary'
        verbose_name_plural = 'Scrabble Dictionary'
