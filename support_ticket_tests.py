import unittest
from support_ticket import Queue, Stack, Ticket

class TestCustomerSupportTicketSystem(unittest.TestCase):

    def setUp(self):
        self.new_tickets = Queue()
        self.processed_tickets = Stack()

    def test_submit_new_ticket(self):
        ticket1 = Ticket("T001", "Printer not working")
        self.new_tickets.enqueue(ticket1)
        self.assertEqual(self.new_tickets.size(), 1)
        self.assertIs(self.new_tickets.peek(), ticket1)


    def test_process_ticket(self):
        ticket1 = Ticket("T001", "Printer not working")
        ticket2 = Ticket("T002", "Software installation issue")
        self.new_tickets.enqueue(ticket1)
        self.new_tickets.enqueue(ticket2)

        processed_ticket = self.new_tickets.dequeue()
        self.processed_tickets.push(processed_ticket)

        self.assertIs(processed_ticket, ticket1)

        self.assertEqual(processed_ticket.ticket_id, "T001")
        self.assertEqual(processed_ticket.issue_description, "Printer not working")
        self.assertEqual(self.new_tickets.size(), 1)
        self.assertEqual(self.processed_tickets.size(), 1)
        self.assertIs(self.processed_tickets.peek(), ticket1)
        self.assertIs(self.new_tickets.peek(), ticket2)

    def test_revert_processed_ticket(self):
        ticket1 = Ticket("T001", "Printer not working")
        ticket2 = Ticket("T002", "Software installation issue")
        self.new_tickets.enqueue(ticket1)
        self.new_tickets.enqueue(ticket2)

        # Process ticket1
        processed_ticket_1 = self.new_tickets.dequeue()
        self.processed_tickets.push(processed_ticket_1)
        processed_ticket_2 = self.new_tickets.dequeue()
        self.processed_tickets.push(processed_ticket_2)

        # Revert ticket2
        reverted_ticket = self.processed_tickets.pop()
        self.new_tickets.enqueue(reverted_ticket) 

        self.assertIs(reverted_ticket, ticket2)
        self.assertEqual(reverted_ticket.ticket_id, "T002")
        self.assertEqual(reverted_ticket.issue_description, "Software installation issue")
        self.assertEqual(self.processed_tickets.size(), 1)
        self.assertIs(self.processed_tickets.peek(), ticket1)
        self.assertEqual(self.new_tickets.size(), 1)
        self.assertIs(self.new_tickets.peek(), ticket2) 


    

   
   


if __name__ == '__main__':
    unittest.main()