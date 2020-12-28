from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Student(models.Model):
    studentID = models.CharField(unique=True, editable=False)

    def __str__(self):
        return f"{self.studentID}"


class ExamLocation(models.Model):
    port = models.IntegerField(editable=False)
    host = models.CharField(editable=False, default="127.0.0.1")
    bind_key = models.CharField(editable=False)

    def __str__(self):
        return f"{self.host}:{self.port}/{self.bind_key}"


class Choice(models.Model):
    choice_id = models.IntegerField()
    response = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.choice_id}. {self.response}"


class Question(models.Model):
    title = models.CharField(max_length=40)
    choices = models.ManyToManyField(Choice)
    correct_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        choices_str = '\n'.join(map(lambda x: f'\t{x}', map(str, self.choices)))
        return f"{self.title}\n{choices_str}"

    def save(self, **kwargs):
        if self.correct_choice in self.choices:
            super(Question, self).save(**kwargs)
        else:
            raise ValidationError("Correct choice not in Choices")


class Exam(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    location = models.ForeignKey(ExamLocation, on_delete=models.DO_NOTHING)
    questions = models.ManyToManyField(Question, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Grade')

    def __str__(self):
        return f"{self.id} - {self.title}"

    def save(self, **kwargs):
        if self.date_start < self.date_finish:
            super(Exam, self).save(**kwargs)
        else:
            raise ValidationError("Correct choice not in Choices")


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    correct = models.IntegerField()

    def __str__(self):
        return f"{self.correct} / {len(self.exam.questions)}"
