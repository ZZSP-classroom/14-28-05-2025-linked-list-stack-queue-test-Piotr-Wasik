class Reservation:
    def __init__(self, user_name, book_title):
        self.user_name = user_name
        self.book_title = book_title

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
    

def main():
    reservation_system = Queue()

    while True:
        print("1. add reservation")
        print("2. cancel reservation")
        print("3. viev next")
        print("4. Check if system is empty")
        print("5. Number of reservations")

        choice = input("enter number")
        if choice == '1':
            user_name = input("enter name: ")
            book_title = input("enter book: ")
            reservation = Reservation(user_name, book_title)
            reservation_system.enqueue(reservation)
        elif choice == '2':
            reservation_system.dequeue()
        elif choice == '3':
            reservation_system.peek()
        elif choice == '4':
            if reservation_system.is_empty():
                print("is empty")
            else:
                print("Is not empty")
        elif choice == '5':
            print(f"Number of reservations: {reservation_system.size()}")
        

if __name__ == "__main__":
    main()