from django.test import TestCase
import json
# Create your tests here.
from rest_framework.test import APIClient

from apps.exams.models import Question, Choice, Exam, ExamLocation, Student, Grade


class AllInOneTestCase(TestCase):

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

    def test_get_by_id(self):
        response = self.status_code_200('/api/question/1/')
        json_resp = response.json()
        self.check_question(json_resp)

    def check_question(self, json_resp):
        self.assertEquals("First question?", json_resp['title'])
        self.assertEquals([{'choice_id': 1, 'response': 'First choice'}], json_resp['choices'])
        self.assertEquals(1, json_resp['correct_choice'])

    def test_list(self):
        response = self.status_code_200('/api/question/')
        json_resp = response.json()
        self.assertEquals(list, type(json_resp))
        self.check_question(json_resp[0])

    def status_code_200(self, endpoint):
        client = APIClient()
        response = client.get(endpoint)
        self.assertEquals(200, response.status_code)
        return response


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


    def test_put_grades(self):
        client = APIClient()
        data = {'correct': 1}
        response = client.put('/api/exam/1/grades/123/', data)

    """def test_get_grades(self):
        client = APIClient()
        response = client.get('/api/exam/1/grades/')
        self.assertEquals(200, response.status_code)
        print(response.json())"""
