from typing import List

class Token:
    def __init__(self):
        self.x = 1

    def __repr__(self):
        return "undefined"

class FunctionDef(Token):
    def __repr__(self):
        return "funcDef"

class Bool(Token):
    def __repr__(self):
        return "TypeDec: Bool"

class Int(Token):
    def __repr__(self):
        return "TypeDec: int"

class OpenParen(Token):
    def __repr__(self):
        return "OpenParen"
        
class CloseParen(Token):
    def __repr__(self):
        return "CloseParen"

class OpenCurly(Token):
    def __repr__(self):
        return "OpenParen"

class CloseCurly(Token):
    def __repr__(self):
        return "CloseCurly"

class Semicolon(Token):
    def __repr__(self):
        return "Semicolon"

class IfStatement(Token):
    def __repr__(self):
        return "If"

class EqualCheck(Token):
    def __repr__(self):
        return "EqualCheck"

class Subtract(Token):
    def setValue(self, value):
        self.x = value
        return self

    def __repr__(self):
        return "Subtract " + str(self.x)

class Add(Token):
    def setValue(self, value):
        self.x = value
        return self

    def __repr__(self):
        return "Add " + str(self.x)

possibleTokens = ['summon', 'stamp', 'gloriousNumbers', 'drawPhase', 'standbyPhase', 
                  'mainPhase', 'endPhase', 'nextPhase', 'resloves?', 'lifeEqualizer',
                  'levelReturner', 'mathmechAddition', 'trueDraco', 'solemnJudgment',
                  'bounce']

tokendict = dict()
tokendict['summon']             = ("function definition", lambda: FunctionDef())
tokendict['stamp']              = ("Bool", lambda: Bool())
tokendict['gloriousNumbers']    = ("Int", lambda: Int())
tokendict['drawPhase']          = ("OpenParen", lambda: OpenParen())
tokendict['standbyPhase']       = ("CloseParen", lambda: CloseParen())
tokendict['mainPhase']          = ("OpenCurly", lambda: OpenCurly())
tokendict['endPhase']           = ("CloseCurly", lambda: CloseCurly())
tokendict['nextPhase']          = ("Semicolon", lambda: Semicolon())
tokendict['resloves?']          = ("If", lambda: IfStatement())
tokendict['lifeEqualizer?']     = ("EqualCheck", lambda: EqualCheck())
tokendict['levelReturner']      = ("Subtract", lambda: Subtract())
tokendict['mathmechAddition']   = ("Add", lambda: Add())

def lexYugiCode(prog: str, lexed: list[Token]) -> List[Token]:
    if not prog:
        return lexed

    # if not isinstance(prog, list):
    #     splitProg = prog.split()
    #     c, *progrest = splitProg
    # else:
    c, *progrest = prog

    if c in possibleTokens:
        lexed.append(tokendict[c][1]())
    else:
        lexed[-1] = lexed[-1].setValue(c)

    return lexYugiCode(progrest, lexed)

prog = "summon stamp levelReturner 5 mathmechAddition 10"
prog = prog.split()

lexed = lexYugiCode(prog, [])
print(lexed)