# Niall McKinnon
#
# CSC 231 002
#
# 03/25/2022
#
# Purpose: Demonstrate understanding of Linked Lists
#
# Resources: In-class instruction


class Node:

    def __init__(self, data):
        """
        Purpose: initialize the node
        Parameters: self, data (value stored in node)
        Return: none
        """
        self.data = data
        self.next = None

    def __str__(self):
        """
        Purpose: display node as a string
        Parameters: self
        Return: string of the data
        """
        return str(self.data)


class LinkedList:

    def __init__(self):
        """
        Purpose: initialize the linked list
        Parameters: self
        Return: none
        """
        self.head = None

    def is_empty(self):
        """
        Purpose: determine if the LL is empty
        Parameters: self
        Return: boolean value
        """
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        """
        Purpose: find the size of the LL
        Parameters: self
        Return: int (length of the LL)
        """
        if self.is_empty():
            return 0

        else:
            counter = 1
            current = self.head

            while current.next is not None:
                current = current.next
                counter += 1

            return counter

    def add(self, item):
        """
        Purpose: add a new node to the beginning of the LL
        Parameters: self, item (value to be added)
        Return: none
        """
        newNode = Node(item)
        current = self.head
        self.head = newNode
        newNode.next = current

    def __iter__(self):
        """
        Purpose: allows LL to be called in 'for x in y' loops
        Parameters: self
        Return: none
        Yield: current item in LL
        """
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, item):
        """
        Purpose: adds an item to the end of the LL
        Parameters: self, item (value to be added)
        Return: none
        """
        if self.is_empty():
            self.add(item)

        else:
            newNode = Node(item)
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = newNode

    def pop(self, pos=None):
        """
        Purpose: removes an item from a specified index in the LL
        Parameters: self, pos (index of item to be removed)
        Return: the popped item
        """
        if pos is None or type(pos) is int and self.size() - 1 >= pos >= 0:

            if self.is_empty():
                raise Exception("Can\'t pop from an empty LinkedList")

            elif self.size() == 1:
                output = self.head
                self.head = None
                return output

            elif pos is not None:
                if pos == 0:
                    output = self.head
                    self.head = output.next
                    output.next = None
                    return output

                else:
                    # Find the position
                    counter = 0
                    current = self.head
                    previous = self.head

                    while counter != pos:
                        previous = current
                        current = current.next
                        counter += 1

                    previous.next = current.next
                    current.next = None
                    return current

            else:
                current = self.head
                previous = self.head

                while current.next is not None:
                    previous = current
                    current = current.next

                previous.next = None
                return current

        else:
            raise TypeError("pos must be an integer within index range of the LL")

    def search(self, item):
        """
        Purpose: determines if a specified item is in the LL
        Parameters: self, item
        Return: boolean value
        """
        if self.is_empty():
            raise Exception('Cannot search an empty LinkedList')

        else:
            current = self.head
            while current is not None:
                if current.data == item:
                    return True
                else:
                    current = current.next
            return False

    def remove(self, item):
        """
        Purpose: removes the first occurrence of a specified item from the LL
        Parameters: self, item
        Return: none
        """
        if self.is_empty():
            raise Exception('Cannot remove from an empty LinkedList')
        else:
            if not self.search(item):
                raise Exception('Item does not exist in LinkedList')
            else:
                counter = 0
                current = self.head
                found = False
                while not found and current is not None:
                    if current.data == item:
                        found = True
                        self.pop(counter)
                    else:
                        current = current.next
                        counter += 1
