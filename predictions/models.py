from django.db import models

# Create your models here.

class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date = models.DateTimeField()
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2}"

class Prediction(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team1_win_probability = models.FloatField()
    team2_win_probability = models.FloatField()
    predicted_winner = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.match}"
