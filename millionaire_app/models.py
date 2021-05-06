from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username


class Question(models.Model):
    question_text = models.CharField(max_length=200, blank=False, null=False)
    question_point = models.IntegerField(default=5)

    def answers(self):
        return self.answer.all()

    def __str__(self) -> str:
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=100, blank=False)
    answer_status = models.BooleanField(verbose_name="is_correct")

    def __str__(self) -> str:
        return self.answer_text
