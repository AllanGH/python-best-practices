import unittest
from lundpy import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        expected_quotes = [
            "Code is like humor. When you have to explain it, it’s bad.",
            "Fix the cause, not the symptom.",
            "Optimism is an occupational hazard of programming.",
            "Welcome to the Python Best Practices Workshop!"
        ]
        self.assertIn(response.data.decode("utf-8"), expected_quotes)

if __name__ == "__main__":
    unittest.main()
