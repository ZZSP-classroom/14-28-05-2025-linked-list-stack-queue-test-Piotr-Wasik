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
    history = Stack()

    while True:
        print("1. visit page")
        print("2. go back")
        print("3. Viev current page")
        print("4. Check if history is empty")
        print("5. Number of pages")

        choice = input("enter number")
        if choice == '1':
            url = input("Enter url: ")
            history.push(url)
            print("Visited: ", url)
            
        elif choice == '2':
            history.pop()
        elif choice == '3':
            history.peek()
        elif choice == '4':
            if history.is_empty():
                print("is empty")
            else:
                print("Is not empty")
        elif choice == '5':
            print(f"Number of pages: {history.size()}")
        

if __name__ == "__main__":
    main()