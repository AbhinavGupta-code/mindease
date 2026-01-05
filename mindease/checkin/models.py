from django.db import models

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Okay'),
        (4, 'Good'),
        (5, 'Very Good'),
    ]

    mood = models.IntegerField(choices=MOOD_CHOICES)
    reflection = models.TextField()
    sentiment_score = models.FloatField(null=True, blank=True)
    sentiment_label = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mood {self.mood} on {self.created_at.date()}"
