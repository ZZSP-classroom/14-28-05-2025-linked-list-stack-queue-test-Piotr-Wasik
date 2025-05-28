import unittest
from browser_history import Stack

class TestBrowserHistory(unittest.TestCase):

    def test_push(self):
        history = Stack()
        history.push("google.com")
        self.assertEqual(history.peek(), "google.com")
        self.assertEqual(history.size(), 1)

        history.push("youtube.com")
        self.assertEqual(history.peek(), "youtube.com")
        self.assertEqual(history.size(), 2)

    def test_pop(self):
        history = Stack()
        history.push("google.com")
        history.push("youtube.com")

        popped_url = history.pop()
        self.assertEqual(popped_url, "youtube.com")
        self.assertEqual(history.size(), 1)
        self.assertEqual(history.peek(), "google.com")

        popped_url = history.pop()
        self.assertEqual(popped_url, "google.com")
        self.assertEqual(history.size(), 0)
        self.assertTrue(history.is_empty())

  

   
    def test_is_empty(self):
        history = Stack()
        self.assertTrue(history.is_empty())

        history.push("google.com")
        self.assertFalse(history.is_empty())

        history.pop()
        self.assertTrue(history.is_empty())

    def test_size(self):
        history = Stack()
        self.assertEqual(history.size(), 0)

        history.push("google.com")
        self.assertEqual(history.size(), 1)

        history.push("youtube.com")
        self.assertEqual(history.size(), 2)

        history.pop()
        self.assertEqual(history.size(), 1)
        history.pop()
        self.assertEqual(history.size(), 0)


if __name__ == '__main__':
    unittest.main()