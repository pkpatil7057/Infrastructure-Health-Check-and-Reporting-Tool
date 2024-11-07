import unittest
from health_check import ping_server, check_database_connection, check_api_endpoint

class TestHealthCheck(unittest.TestCase):

    def test_ping_server(self):
        self.assertTrue(ping_server("8.8.8.8", 53))  # Google's public DNS

    def test_check_database_connection(self):
        self.assertFalse(check_database_connection("127.0.0.1", 5432))  # Assumes no DB at localhost

    def test_check_api_endpoint(self):
        self.assertTrue(check_api_endpoint("https://api.example.com/health"))

if __name__ == "__main__":
    unittest.main()

