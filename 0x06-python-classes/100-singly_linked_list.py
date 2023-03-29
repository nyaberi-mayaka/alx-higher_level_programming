#!/usr/bin/python3

class Node:
    """
    Node class for a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        initialization called when instance of class created
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        get the data attribute
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        set the data attribute
        """
        if isinstance(value, int):
            self.__data = value

        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        get the node attribute
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        set the node attribute
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    contains nodes for a singly linked list and methods for ->
    insertion
    """

    def __init__(self):
        """
        initialization called when instance of class created
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position
        (based on data)
        """
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
        """
        used by print to print linked list
        """
        temp = self.__head
        string = ""
        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node

            if temp is not None:
                string += '\n'
        return (string)
