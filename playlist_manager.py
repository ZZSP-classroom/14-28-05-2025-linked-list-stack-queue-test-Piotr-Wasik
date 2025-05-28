class Song:
    def init(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None 

class LinkedList:
    def init(self):
        self.head = None
        self._size = 0

    def add_song(self, title, artist):
        """Adds a new song to the end of the playlist."""
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        self._size += 1
        print(f"Added '{title}' by {artist} to the playlist.")

    def remove_song(self, title, artist):
        """Removes a song from the playlist by title and artist."""
        if not self.head:
            print("Playlist is empty. Cannot remove song.")
            return None

        # Handle removing the head
        if self.head.title == title and self.head.artist == artist:
            removed_song = self.head
            self.head = self.head.next
            self._size -= 1
            print(f"Removed '{title}' by {artist} from the playlist.")
            return removed_song

        current = self.head
        while current.next:
            if current.next.title == title and current.next.artist == artist:
                removed_song = current.next
                current.next = current.next.next
                self._size -= 1
                print(f"Removed '{title}' by {artist} from the playlist.")
                return removed_song
            current = current.next
            print(f"Song '{title}' by {artist} not found in playlist.")
            return None

    def get_next_song(self):
        """Returns the next song in the playlist (the head) without removing it."""
        if self.head:
            return self.head
        return None

    def is_empty(self):
        """Checks if the playlist is empty."""
        return self.head is None

    def size(self):
        """Returns the number of songs in the playlist."""
        return self._size

    def display_playlist(self):
        """Prints all songs in the playlist."""
        if not self.head:
            print("Playlist is empty.")
            return
        current = self.head
        print("\n--- Current Playlist ---")
        while current:
            print(f"Title: {current.title}, Artist: {current.artist}")
            current = current.next
        print("------------------------")

def main():
    playlist = LinkedList()
    print("--- Playlist Management System ---")

    while True:
        print("\nOptions:")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. View Next Song")
        print("4. Display All Songs")
        print("5. Check if playlist is empty")
        print("6. View number of songs in playlist")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            playlist.add_song(title, artist)
        elif choice == '2':
            title = input("Enter title of song to remove: ")
            artist = input("Enter artist of song to remove: ")
            playlist.remove_song(title, artist)
        elif choice == '3':
            next_song = playlist.get_next_song()
            if next_song:
                print(f"Next song: Title: '{next_song.title}', Artist: '{next_song.artist}'")
            else:
                print("Playlist is empty. No next song.")
        elif choice == '4':
            playlist.display_playlist()
        elif choice == '5':
            if playlist.is_empty():
                print("The playlist is empty.")
            else:
                print("There are songs in the playlist.")
        elif choice == '6':
            print(f"Number of songs in playlist: {playlist.size()}")
        elif choice == '7':
            print("Exiting Playlist Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()