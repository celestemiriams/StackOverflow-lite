"""
Tests module
"""
from unittest import TestCase
from flask import json
from api.run import App



class Tests(TestCase):
    """
    Tests run for the api
    """
    def setUp(self):
        self.app = App
        self.client = self.app.test_client

    def test_get_questions(self):
        """
        Test case for get questions endpoint, it gets all questions
        """
        result = self.client().get('/api/v1/questions/')
        self.assertEqual(result.status_code, 200)

    def test_get_a_question(self):
        """
        Test case for get a question endpoint, it gets a single question
        """
        result = self.client().get('/api/v1/questions/1/')
        self.assertEqual(result.status_code, 200)

        result1 = self.client().get('/api/v1/questions/jon/')
        self.assertEqual(result1.status_code, 404)

        result2 = self.client().get('/api/v1/questions/@')
        self.assertEqual(result2.status_code, 404)

        result3 = self.client().get('/api/v1/questions/10/')
        self.assertEqual(result3.status_code, 200)

        result4 = self.client().get('/api/v1/questions/2/')
        # resp = json.loads(result4.data.decode("utf8"))
        self.assertEqual(result4.status_code, 200)

    def test_post_a_question(self):
        """
        Test case for post a question endpoint, it posts a question
        """
        result = self.client().post('/api/v1/questions/', data=json.dumps(
            dict(question_id=1, person_who_asked="Miriam", the_question="How to join fellowship",
                 Answers=['no answer'])), content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_post_answers(self):
        """
        Test case for post answers endpoint, it posts answers
        """
        result = self.client().post('/api/v1/questions/2/answers/', data=json.dumps(
            dict(Answers="About 4 weeks")), content_type='application/json')
        self.assertEqual(result.status_code, 204)
