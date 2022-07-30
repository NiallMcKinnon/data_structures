# Niall McKinnon
#
# CSC 231 002
#
# 03/25/2022
#
# Purpose: Demonstrate understanding of Doubly Linked Lists
#
# Resources: In-class instruction

# For some reason, end=' ' doesn't work unless I include this import line
from __future__ import print_function


class Node:

    def __init__(self, data):
        """
        Purpose: initialize the node
        Parameters: self, data (value stored in node)
        Return: none
        """
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """
        Purpose: display node as a string
        Parameters: self
        Return: string of the data
        """
        return str(self.data)


class DoublyLinkedList:

    def __init__(self):
        """
        Purpose: initialize the doubly linked list
        Parameters: self
        Return: none
        """
        self.head = None
        self.tail = None

    def is_empty(self):
        """
        Purpose: determine if the DLL is empty
        Parameters: self
        Return: boolean value
        """
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        """
        Purpose: find the size of the DLL
        Parameters: self
        Return: int (length of the DLL)
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
        Purpose: add a new node to the beginning of the DLL
        Parameters: self, item (value to be added)
        Return: none
        """

        newNode = Node(item)

        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            current = self.head
            self.head = newNode
            newNode.next = current
            current.prev = newNode

    def __iter__(self):
        """
        Purpose: allows DLL to be called in 'for x in y' loops
        Parameters: self
        Return: none
        Yield: current item in DLL
        """
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, item):
        """
        Purpose: adds an item to the end of the DLL
        Parameters: self, item (value to be added)
        Return: none
        """
        if self.is_empty():
            self.add(item)

        else:
            newNode = Node(item)
            current = self.tail
            self.tail = newNode
            current.next = newNode
            newNode.prev = current

    def pop(self, pos=None):
        """
        Purpose: removes an item from a specified index in the DLL
        Parameters: self, pos (index of item to be removed)
        Return: the popped item
        """
        if pos is None or type(pos) is int and self.size()-1 >= pos >= 0:

            if self.is_empty():
                raise Exception("Can\'t pop from an empty DoublyLinkedList")

            elif self.size() == 1:
                output = self.head
                self.tail = None
                self.head = None
                return output

            elif pos is not None:
                if pos == 0:
                    output = self.head
                    self.head = output.next
                    output.next.prev = None
                    output.next = None
                    output.prev = None
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

                    upcoming = current.next

                    if upcoming is None:
                        self.tail = previous
                        previous.next = None
                        current.prev = None

                    else:
                        previous.next = upcoming
                        upcoming.prev = previous
                        current.next = None
                        current.prev = None

                    return current

            else:
                current = self.tail
                previous = current.prev

                previous.next = None
                self.tail = previous
                return current

        else:
            raise TypeError("pos must be an integer within index range of the DLL")

    def search(self, item):
        """
        Purpose: determines if a specified item is in the DLL
        Parameters: self, item
        Return: boolean value
        """
        if self.is_empty():
            raise Exception('Cannot search an empty DoublyLinkedList')

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
        Purpose: removes the first occurrence of a specified item from the DLL
        Parameters: self, item
        Return: none
        """
        if self.is_empty():
            raise Exception('Cannot remove from an empty DoublyLinkedList')
        else:
            if not self.search(item):
                raise Exception('Item does not exist in DoublyLinkedList')
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

    def display(self):
        """
        This function simply helps me visualize the DLL so I can verify everything works properly.
        """
        for node in self:
            if node.prev is None:
                print("{} <--> {} <--> {}".format(node.prev, node.data, node.next), end=" ")
            else:
                print("<--> {}".format(node.next), end=" ")

        print('\n')
