from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Student(models.Model):
    studentID = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.studentID}"


class ExamLocation(models.Model):
    port = models.IntegerField()
    host = models.CharField(default="127.0.0.1", max_length=25)
    bind_key = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.host}:{self.port}/{self.bind_key}"


class Choice(models.Model):
    choice_id = models.IntegerField()
    response = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.choice_id}. {self.response}"


class Question(models.Model):
    title = models.CharField(max_length=40)
    choices = models.ManyToManyField(Choice, related_name='choices')
    correct_choice = models.IntegerField()

    def __str__(self):
        choices_str = '\n'.join(map(lambda x: f'\t{x}', map(str, self.choices.all())))
        return f"{self.title}\n{choices_str}"


class Exam(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    location = models.ForeignKey(ExamLocation, on_delete=models.DO_NOTHING)
    questions = models.ManyToManyField(Question)
    students = models.ManyToManyField(Student, through='Grade')

    def __str__(self):
        return f"{self.id} - {self.title}"

    def save(self, **kwargs):
        if self.date_start <= self.date_finish:
            super(Exam, self).save(**kwargs)
        else:
            raise ValidationError(f"{self.date_start} > {self.date_finish}")


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    correct = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.correct} / {len(self.exam.questions.all())}"
