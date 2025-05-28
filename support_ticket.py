class Ticket:
    def __init__(self, ticket_id, issue_description):
        self.ticket_id = ticket_id
        self.issue_description = issue_description

class Queue:
    def __init__(self):
        self._queue = []


    def enqueue(self, item):
        self._queue.append(item) 

    def dequeue(self):
        return self._queue.pop(0)
    
    def peek(self):
        return self._queue[0]
    
    def is_empty(self):
        return len(self._queue) == 0
    
    def size(self):
        return len(self._queue)
    
class Stack:
    def __init__(self):
        self._stack = []
    
    def push(self, item):
        self._stack.append(item) 

    def pop(self):
        return self._stack.pop()
    
    def peek(self):
        return self._stack[-1]
    
    def is_empty(self):
        return len(self._stack) == 0
    
    def size(self):
        return len(self._stack)

def main():
    new_tickets = Queue()
    processed_tickets = Stack()
    ticket_counter = 0

    while True:
        print("1. Submit new ticket")
        print("2. Process next ticket")
        print("3. Revert Last proceeded ticket")
        print("4. Viev next ticket")
        print("5. Viev last proceeded ticket")
        print("6. Viev status")

        choice = input("enter number: ")
        if choice == '1':
            ticket_counter += 1
            issue_description = input("Enter issue")
            ticket = Ticket(f"T{ticket_counter:03d}", issue_description)
            new_tickets.enqueue(ticket)
        elif choice == '2':
            new_tickets.enqueue(ticket)
        elif choice == '3':
            new_tickets.pop()
        elif choice == '4':
            new_tickets.peek()
        elif choice == '5':
            processed_tickets.peek()
        elif choice == '6':
            print(f"Number of new tickets in queque: {new_tickets.size()}")
            print(f"Number of new tickets in queque: {processed_tickets.size()}")
        

if __name__ == "__main__":
    main()