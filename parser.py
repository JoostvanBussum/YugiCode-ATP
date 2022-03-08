from multiprocessing.sharedctypes import Value
from lexer import *


class Node():

    def __init__(self, value : str = None, type : Token = None):
        self.value = value
        self.type = type

    def __repr__(self):
        return ("value: " + self.value + " type: ", self.type)

class OperatorNode(Node):

    def __init__(self, value : str = None, lhs : Node = None, rhs : Node = None, type : Token = None):
        Node.__init__(value, type)
        self.value = value
        self.lhs = lhs
        self.rhs = rhs
    




