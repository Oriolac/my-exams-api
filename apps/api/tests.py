from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient

from apps.exams.models import Question, Choice, Exam, ExamLocation, Student, Grade


"""class QuestionTestCase(TestCase):

    def setUp(self) -> None:
        instance = Question.objects.create(title="How works?", correct_choice=1)
        choice = Choice.objects.create(choice_id=1, response="Well")
        instance.choices.set([choice])

    def test_response_code(self):
        client = APIClient()
        response = client.get('/api/question/1/')
        self.assertEquals(200, response.status_code)
        print(response.json())"""


class GradesTestCase(TestCase):

    def setUp(self) -> None:
        location = ExamLocation.objects.create(port=998, host="localhost", bind_key="string1")
        exam = Exam.objects.create(title="My first exam", description="My first exam description",
                                   date_start="2021-01-04T01:36:00Z", date_finish="2021-01-04T01:36:00Z",
                                   location=location)
        question = Question.objects.create(title="First question?", correct_choice=1)
        choice = Choice.objects.create(choice_id=1, response="First choice")
        student = Student.objects.create(studentID="123")

        question.choices.set([choice])
        exam.questions.set([question])
        exam.students.set([student])


    """def test_put_grades(self):
        client = APIClient()
        data = {'correct': 1}
        response = client.put('/api/exam/1/grades/123/', data)
        self.assertEquals(200, response.status_code)"""

    def test_get_grades(self):
        client = APIClient()
        response = client.get('/api/exam/1/grades/123/')
        self.assertEquals(200, response.status_code)
        print(response.json())
