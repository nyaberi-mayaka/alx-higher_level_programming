#!/usr/bin/python3

"""Defines a class Node."""


class Node:
    """Node class for a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes a Node object.
        Args:
            data (int): value to be assigned to the data attribute.
            next_node (Node): Node to """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data attribute"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set the data attribute"""
        if isinstance(value, int):
            self.__data = value

        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get the node attribute"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set the node attribute"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Contains nodes for a singly linked list and methods for ->
    insertion"""

    def __init__(self):
        """Initialization called when instance of class created"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
           (based on data)"""
        if self.__head is None:
            self.__head = Node(value)
            return

        else:
            prev = None
            node = self.__head
            while node is not None:
                if node.data > value:
                    break
                prev = node
                node = node.next_node
            new_node = Node(value)
            new_node.next_node = node
            if prev is not None:
                prev.next_node = new_node
            if prev is None:
                self.__head = new_node

    def __str__(self):
        """Used by print to print linked list"""
        temp = self.__head
        string = ""
        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node

            if temp is not None:
                string += '\n'
        return (string)
