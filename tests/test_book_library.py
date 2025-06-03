import unittest
from src.book_library import BookLibrary

class TestBookLibrary(unittest.TestCase):
    def setUp(self):
        self.library = BookLibrary()

    def test_add_book(self):
        self.library.add_book("1984")
        self.assertIn("1984", self.library.get_books())

    def test_remove_book(self):
        self.library.add_book("1984")
        self.library.remove_book("1984")
        self.assertNotIn("1984", self.library.get_books())

    def test_get_books(self):
        self.library.add_book("1984")
        self.library.add_book("Brave New World")
        self.assertEqual(self.library.get_books(), ["1984", "Brave New World"])

    def test_remove_nonexistent_book_fail(self):
        with self.assertRaises(ValueError):
            self.library.remove_book("Nonexistent Book")

    def test_clear_library(self):
        self.library.add_book("1984")
        self.library.add_book("Brave New World")
        self.library.clear_library()
        self.assertEqual(self.library.get_books(), [])

    def test_book_count(self):
        self.library.add_book("1984")
        self.library.add_book("Brave New World")
        self.assertEqual(self.library.book_count(), 2)

    def test_book_count_fail(self):
        self.library.add_book("1984")
        self.library.add_book("Brave New World")
        self.assertEqual(self.library.book_count(), 3)

    def test_get_book_by_index(self):
        self.library.add_book("1984")
        self.library.add_book("Brave New World")
        self.assertEqual(self.library.get_book_by_index(1), "Brave New World")

    def test_get_book_by_index_fail(self):
        self.library.add_book("1984")
        self.library.add_book("Brave New World")
        self.assertEqual(self.library.get_book_by_index(2), "Fahrenheit 451")

if __name__ == "__main__":
    unittest.main()
