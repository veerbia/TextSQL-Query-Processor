import unittest
from query_processor_template import QueryProcessor

class TestQueryProcessor(unittest.TestCase):
    def setUp(self):
        self.query_processor = QueryProcessor(timeout=5)

    def test_process_query(self):
        query = "Find the player with the highest PER in the 2019 regular season"
        result = self.query_processor.process_query(query)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
