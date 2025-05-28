import unittest
from library_reservation import Queue, Reservation

class TestLibraryReservation(unittest.TestCase):

    def test_enqueue_order(self):
        reservation_system = Queue()
        res1 = Reservation("Alice", "The Great Gatsby")
        res2 = Reservation("Bob", "1984")
        res3 = Reservation("Charlie", "To Kill a Mockingbird")

        reservation_system.enqueue(res1)
        

        self.assertEqual(reservation_system.size(), 1)
        self.assertIs(reservation_system.peek(), res1)
        self.assertEqual(reservation_system.peek().user_name, "Alice")
        self.assertEqual(reservation_system.peek().book_title, "The Great Gatsby")
    def test_dequeue_removes_correct_reservation(self):
        reservation_system = Queue()
        res1 = Reservation("Alice", "The Great Gatsby")
        res2 = Reservation("Bob", "1984")

        reservation_system.enqueue(res1)
        reservation_system.enqueue(res2)

        dequeued_res = reservation_system.dequeue()
        self.assertIs(dequeued_res, res1) 
        self.assertEqual(dequeued_res.user_name, "Alice")
        self.assertEqual(dequeued_res.book_title, "The Great Gatsby")
        self.assertEqual(reservation_system.size(), 1)
        self.assertIs(reservation_system.peek(), res2) 

        dequeued_res = reservation_system.dequeue()
        self.assertIs(dequeued_res, res2) 
        self.assertEqual(dequeued_res.user_name, "Bob")
        self.assertEqual(dequeued_res.book_title, "1984")
        self.assertEqual(reservation_system.size(), 0)
        self.assertTrue(reservation_system.is_empty())

    

    def test_is_empty(self):
        reservation_system = Queue()
        self.assertTrue(reservation_system.is_empty())

        res1 = Reservation("Alice", "The Great Gatsby")
        reservation_system.enqueue(res1)
        self.assertFalse(reservation_system.is_empty())

        reservation_system.dequeue()
        self.assertTrue(reservation_system.is_empty())

    

    

if __name__ == '__main__':
    unittest.main()