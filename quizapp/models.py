from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    username = models.CharField(
        max_length=50,
        unique=True
    )

    password = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.username


class Quiz(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    duration = models.IntegerField(
        default=10
    )

    difficulty = models.CharField(
        max_length=20,
        default='Easy'
    )

    def __str__(self):

        return self.title


class Question(models.Model):

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    question_text = models.TextField()

    def __str__(self):

        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
    )

    choice_text = models.CharField(
        max_length=200
    )

    is_correct = models.BooleanField(
        default=False
    )

    def __str__(self):

        return self.choice_text
