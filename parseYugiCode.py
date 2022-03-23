from concurrent.futures import process
from multiprocessing.sharedctypes import Value
from lexer import *
import copy


class Node():

    def __init__(self, value : str = None, type : Token = None):
        self.value = value
        self.type = type

    def __repr__(self) -> str:
        return ("value: " + ("None " if self.value is None else self.value) + " type: ", self.type)

class OperatorNode(Node):

    def __init__(self, value : str = None, lhs : Node = None, operator : Token = None, rhs : Node = None, type : Token = None):
        Node.__init__(value, type)
        self.value = value
        self.lhs = lhs
        self.operator = operator
        self.rhs = rhs
    

    def __repr__(self) -> str:
        return ("value: " + ("None " if self.value is None else self.value) + " lhs: " + ("None " if self.lhs is None else self.lhs.__repr__())
         + " rhs: " + ("None " if self.rhs is None else self.rhs.__repr__()))

class valueNode(Node):

    def __init__(self, value : str = None, type : Token = None):
        Node.__init__(value, type)
        self.value = value
        self.type = type

    def __repr__(self) -> str:
        return ("value: " + ("None " if self.value is None else self.value) + " type: ", self.type)



def processFunctionToken(tokens : List[Token]):
    print("Joost was hier :)")


def processTokens(tokens : List[Token]):
    tokenList = copy.copy(tokens)
    if len(tokenList) == 0:
        return []

    token, *rest = tokenList

    if isinstance(token, FunctionDef):
        processFunctionToken(tokenList)




def parse(tokens: List[Token]):
    return processTokens(tokens)