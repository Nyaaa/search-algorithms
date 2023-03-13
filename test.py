from search import a_star, dijkstra, dijkstra_queue, binary
from search.errors import PathNotFound, VertexNotFound
import unittest
import string

test = {'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'C': 2, 'D': 4},
        'C': {'A': 5, 'B': 2, 'D': 5},
        'D': {'B': 4, 'C': 5, 'E': 2},
        'E': {'C': 5, 'D': 2}
        }

test2 = {'A': {'B': 2},
         'B': {'A': 2},
         'C': {}
         }


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.test_function = dijkstra.search

    def test_path_true(self):
        self.assertEqual(self.test_function(test, 'A', 'D'), ['A', 'B', 'D'])

    def test_illegal_stop(self):
        self.assertRaises(VertexNotFound, self.test_function, test, 'A', 'N')

    def test_illegal_start(self):
        self.assertRaises(VertexNotFound, self.test_function, test, 'N', 'A')

    def test_no_path(self):
        self.assertRaises(PathNotFound, self.test_function, test2, 'A', 'C')


class TestDijkstraQueue(TestDijkstra):
    def setUp(self):
        self.test_function = dijkstra_queue.search


class TestAstar(TestDijkstra):
    def setUp(self):
        self.test_function = a_star.search


class TestBinary(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = range(-10, 11)
        cls.strings = list(string.ascii_lowercase)

    def test_negative(self):
        self.assertEqual(binary.search(self.data, -10), 0)

    def test_positive(self):
        self.assertEqual(binary.search(self.data, 10), 20)

    def test_zero(self):
        self.assertEqual(binary.search(self.data, 0), 10)

    def test_str(self):
        self.assertEqual(binary.search(self.strings, 'a'), 0)

    def test_item_not_in_list(self):
        self.assertRaises(VertexNotFound, binary.search, self.data, -30)
        self.assertRaises(VertexNotFound, binary.search, self.data, 30)
        self.assertRaises(VertexNotFound, binary.search, self.strings, 'Z')

