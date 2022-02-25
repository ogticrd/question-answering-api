import json
import unittest

from fastapi.testclient import TestClient
from requests import head

from api import app


class TestWebhook(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        self.data = json.dumps({'text': 'Cuantas personas hablan espanol'})
        self.headers = {'Content-Type': 'application/json'}

    def test_dialogflow_qa(self):
        res = self.client.post('/webhook/v1/dialogflow/qa',
                               data=self.data, headers=self.headers)
        self.assertEqual(res.status_code, 200)
