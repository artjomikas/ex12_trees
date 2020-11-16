"""."""

from abc import ABCMeta, abstractmethod


class TreeNode(metaclass=ABCMeta):
    """The main node class."""

    def __init__(self, *args):
        """:param make use of *args and store them in a way that it is easy to use them."""
        self.__value = args  # tuple of values

    @property
    @abstractmethod
    def default_operator(self):
        """abstract method which should be overridden to return the default_operator object."""
        pass

    @abstractmethod
    def apply(self):
        """abstract method which should be overridden to compute the value of the given abstract tree."""
        pass

    def class_str(self):
        """:return class string representation of the object."""
        return "Add(Leaf(5), Leaf(6))"

    def __eq__(self, other):
        """:return True when 2 object trees have the same shape and values."""
        return False

    def __ne__(self, other):
        """:return True when 2 object trees have a different shape and/or values."""
        return False

    @property
    @abstractmethod
    def priority(self):
        """
        abstract method witch should be overridden to return priority of the node.

        Visit: https://en.wikipedia.org/wiki/Order_of_operations
        """
        pass

    @property
    @abstractmethod
    def associativity(self):
        """abstract method witch should be overridden to return a boolean whether the node is associative or not."""
        pass
