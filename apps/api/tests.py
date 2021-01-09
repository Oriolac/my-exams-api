from django.test import TestCase
import json
# Create your tests here.
from rest_framework.test import APIClient

from apps.exams.models import Question, Choice


class QuestionTestCase(TestCase):

    def setUp(self) -> None:
        instance = Question.objects.create(title="How works?", correct_choice=1)
        choice = Choice.objects.create(choice_id=1, response="Well")
        instance.choices.set([choice])

    def test_get_by_id(self):
        response = self.status_code_200('/api/question/1/')
        json_resp = response.json()
        self.check_question(json_resp)

    def check_question(self, json_resp):
        self.assertEquals("How works?", json_resp['title'])
        self.assertEquals([{'choice_id': 1, 'response': 'Well'}], json_resp['choices'])
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

