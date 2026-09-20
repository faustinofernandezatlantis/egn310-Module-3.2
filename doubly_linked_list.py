class TrackNode:
    """Represents a single track in the playlist."""
    def __init__(self, title: str, artist: str, duration: str):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.duration})"


class Playlist:
    """Doubly Linked List managing a music playlist."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self._size = 0

    def add_track(self, title: str, artist: str, duration: str):
        """Adds a new track to the end of the playlist."""
        new_node = TrackNode(title, artist, duration)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def remove_track(self, index: int) -> bool:
        """Removes a track by its zero-based index."""
        if index < 0 or index >= self._size or not self.head:
            return False

        current = self.head
        for _ in range(index):
            current = current.next

        # Adjust current pointer if deleting the currently playing track
        if current == self.current:
            self.current = current.next if current.next else current.prev

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        self._size -= 1
        return True

    def next_track(self):
        """Moves player to the next track."""
        if self.current and self.current.next:
            self.current = self.current.next

    def prev_track(self):
        """Moves player to the previous track."""
        if self.current and self.current.prev:
            self.current = self.current.prev

    def move_track_up(self, index: int) -> bool:
        """Moves a track up (towards head)."""
        if index <= 0 or index >= self._size:
            return False

        current = self.head
        for _ in range(index):
            current = current.next

        prev_node = current.prev

        # Swap nodes
        if prev_node.prev:
            prev_node.prev.next = current
        else:
            self.head = current
        current.prev = prev_node.prev

        if current.next:
            current.next.prev = prev_node
        else:
            self.tail = prev_node
        prev_node.next = current.next

        current.next = prev_node
        prev_node.prev = current

        return True

    def to_list(self):
        """Returns a Python list of all tracks for rendering."""
        tracks = []
        curr = self.head
        while curr:
            tracks.append(curr)
            curr = curr.next
        return tracks

    def __len__(self):
        return self._size