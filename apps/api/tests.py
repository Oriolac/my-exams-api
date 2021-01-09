from django.test import TestCase
import json
# Create your tests here.
from rest_framework.test import APIClient, APIRequestFactory, RequestsClient

from apps.exams.models import Question, Choice, Exam, ExamLocation, Student, Grade


class AllInOneTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(AllInOneTestCase, cls).setUpClass()
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

    def test_get_student_grade(self):
        client = APIClient()
        response = client.get('/api/exam/1/grades/123/')
        self.assertEquals(200, response.status_code)
        self.assertEquals('123', response.json()['student']['studentID'])
        self.assertEquals(0, response.json()['correct'])

    def test_get_grades(self):
        client = APIClient()
        response = client.get('/api/exam/1/grades/')
        json_resp = response.json()
        self.assertEquals(list, type(json_resp))

    def test_put_grades(self):
        client = APIClient()
        data = {'correct': 2}
        response = client.put('/api/exam/1/grades/123/', data=data)
        self.assertEquals(200, response.status_code)
        self.assertEquals('123', response.json()['student']['studentID'])
        self.assertEquals(2, response.json()['correct'])

    def test_get_list_exam(self):
        client = APIClient()
        response = client.get('/api/exam/')
        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(response.json()))
        exam = response.json()[0]
        self.assertEquals("My first exam", exam['title'])
        self.assertEquals("My first exam description", exam['description'])

    def test_get_exam(self):
        client = APIClient()
        response = client.get('/api/exam/1/')
        self.assertEquals(200, response.status_code)
        exam = response.json()
        self.assertEquals("My first exam", exam['title'])
        self.assertEquals("My first exam description", exam['description'])

    def test_access_student(self):
        client = APIClient()
        response = client.get('/api/exam/1/123/')
        self.assertEquals(200, response.status_code)
        location = response.json()
        self.assertEquals(998, location['port'])
        self.assertEquals('localhost', location['host'])
        self.assertEquals('string1', location['bind_key'])



    def test_delete_exam(self):
        factory = APIClient()
        response = factory.delete('/api/exam/1/')
        self.assertEquals(204, response.status_code)
        response = factory.get('/api/exam/')
        self.assertEquals([], response.json())

    def test_put_exam_description(self):
        client = APIClient()
        data = {'description': "New exam description"}
        response = client.put('/api/exam/1/desc/', data=data)
        self.assertEquals(200, response.status_code)
        self.assertEquals("New exam description", response.json()['description'])

    def test_post_exam(self):
        client = APIClient()
        data = {'title': "My second exam", 'description': "Distributed Computing2",
                'date_start': "2021-01-04T01:36:00Z",
                'date_finish': "2021-01-05T11:40:00Z", 'location': {'port': 998, 'host': "localhost",
                                                                    'bind_key': "string1"},
                'questions': [{'title': "First question?",
                               'choices': [{'choice_id': 1,
                                            'response': "First response"}],
                               'correct_choice': 1}],
                'students': [{'studentID': "423"}]}
        response = client.post('/api/exam/', data=data, format='json')
        response2 = client.get('/api/exam/')
        response3 = client.get('/api/exam/2/')
        json_resp2 = response2.json()
        json_resp3 = response3.json()
        self.assertEquals(201, response.status_code)
        self.assertEquals(list, type(json_resp2))
        self.assertEquals(2, len(json_resp2))
        self.assertEquals("My second exam", json_resp3['title'])
        self.assertEquals("First question?", json_resp3['questions'][0]['title'])
        self.assertEquals([{'choice_id': 1, 'response': "First response"}], json_resp3['questions'][0]['choices'])
        self.assertEquals(1, json_resp3['questions'][0]['correct_choice'])
        self.assertEquals([{'studentID': "423"}], json_resp3['students'])
