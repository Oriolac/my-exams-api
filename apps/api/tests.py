from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient

from apps.exams.models import Question, Choice


class QuestionTestCase(TestCase):

    def setUp(self) -> None:
        instance = Question.objects.create(title="How works?", correct_choice=1)
        choice = Choice.objects.create(choice_id=1, response="Well")
        instance.choices.set([choice])

    def test_response_code(self):
        client = APIClient()
        response = client.get('/api/question/1/')
        self.assertEquals(200, response.status_code)
        print(response.json())

