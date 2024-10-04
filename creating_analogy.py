class Node:
    # Class representing a person in the movie theater line.
    def __init__(self, data=None):
        # When a new person joins, they know who they are (their 'data') but don't have anyone in front or behind yet.
        self.data = data  # Their name or ID (in this case, 'data').
        self.next = None  # The next person in the line (initially, no one is there).
        self.prev = None  # The person behind in the line (initially, no one is behind either).

class DoubleLinkedList:
    # Class representing the movie theater line, where people can join at the front or be moved.
    def __init__(self):
        # When the line is created, it's empty, so there's no one at the front (the head).
        self.head = None  # No one at the front, the line is empty.

    def add(self, value):
        # A new person (a new node) arrives at the theater and wants to be the first in line.
        a = Node(value)  # We create a new person (node) who wants to join the line.
        a.next = self.head  # This person sees whoever is currently at the front of the line (the head) as the next person.

        # If there's already someone in the line (if self.head is not None):
        if self.head is not None:
            # The person at the front now has to look back and see the new person (a) as the one behind them.
            self.head.prev = a

        # Now, the new person (a) becomes the first in line (the new head).
        self.head = a

    def printing(self):
        # This function is like we’re walking through the movie line, announcing each person's name from front to back.
        printvalue = self.head  # We start at the front of the line (the head).

        # While there are people in the line:
        while printvalue is not None:
            print(printvalue.data)  # We say the current person’s name (data).
            printvalue = printvalue.next  # We move to the next person in the line.

# Now let's simulate people arriving at the movie theater line.

# We create the theater line (a doubly linked list).
movieline = DoubleLinkedList()

# 'Andres' arrives first at the theater and stands at the front of the line.
movieline.add("Andres")

# 'Pepe' arrives and wants to be first, pushing 'Andres' back.
movieline.add("Pepe")

# 'Carlos' arrives and also wants to be first, pushing everyone else back.
movieline.add("Carlos")

# Finally, we print the current line (from front to back).
movieline.printing()

# Expected output:
# Carlos
# Pepe
# Andres"""