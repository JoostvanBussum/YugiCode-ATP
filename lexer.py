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
    def setValue(self, value):
        self.x = value
        return self

    def __repr__(self):
        return "TypeDec: Bool " + str(self.x)

class Int(Token):
    def setValue(self, value):
        self.x = value
        return self

    def __repr__(self):
        return "TypeDec: int " + str(self.x)

class UnsignedInt(Token):
    def setValue(self, value):
        self.x = value
        return self

    def __repr__(self):
        return "TypeDec: unsigned int " + str(self.x)

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
    def setValue(self, value):
        self.x = value
        return self

    def __repr__(self):
        return "EqualCheck to " + str(self.x)
    
class TrueToken(Token):
    def __repr__(self):
        return "True"

class FalseToken(Token):
    def __repr__(self):
        return "False"

class Return(Token):
    def __repr__(self):
        return "Return"

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

class Variable(Token):
    def setValue(self, value):
        self.x = value
        return self

    def __repr__(self):
        return "Variable " + str(self.x)

possibleTokens = ['summon', 'stamp', 'gloriousNumbers', 'TrueKingOfAllCalamities', 
                  'drawPhase', 'standbyPhase', 'mainPhase', 'endPhase', 'nextPhase', 
                  'resolves?', 'lifeEqualizer', 'levelReturner', 'mathmechAddition', 
                  'trueDraco', 'solemnJudgment', 'bounce']
typeList = [OpenParen, CloseParen, OpenCurly, CloseCurly, Semicolon, Return]

tokendict = dict()
tokendict['summon']                     = ("function definition", lambda: FunctionDef())
tokendict['stamp']                      = ("Bool", lambda: Bool())
tokendict['gloriousNumbers']            = ("Int", lambda: Int())
tokendict['TrueKingOfAllCalamities']    = ("Unsigned int", lambda: UnsignedInt())
tokendict['drawPhase']                  = ("OpenParen", lambda: OpenParen())
tokendict['standbyPhase']               = ("CloseParen", lambda: CloseParen())
tokendict['mainPhase']                  = ("OpenCurly", lambda: OpenCurly())
tokendict['endPhase']                   = ("CloseCurly", lambda: CloseCurly())
tokendict['nextPhase']                  = ("Semicolon", lambda: Semicolon())
tokendict['resolves?']                  = ("If", lambda: IfStatement())
tokendict['lifeEqualizer']              = ("EqualCheck", lambda: EqualCheck())
tokendict['levelReturner']              = ("Subtract", lambda: Subtract())
tokendict['mathmechAddition']           = ("Add", lambda: Add())
tokendict['trueDraco']                  = ("True", lambda: TrueToken())
tokendict['solemnJudgment']             = ("False", lambda: FalseToken())
tokendict['bounce']                     = ("Return", lambda: Return())
tokendict['Variable']                   = ('Variable', lambda: Variable())

def lexYugiCode(prog: str, lexed: list[Token]) -> List[Token]:
    if not prog:
        return lexed

    c, *progrest = prog

    print("c: " + c)
    if c in possibleTokens:
        lexed.append(tokendict[c][1]())
    elif type(lexed[-1]) not in typeList:
        lexed[-1] = lexed[-1].setValue(c)
    else:
        lexed.append(tokendict['Variable'][1]())
        lexed[-1] = lexed[-1].setValue(c)
    
    return lexYugiCode(progrest, lexed)

prog = "stamp odd drawPhase TrueKingOfAllCalamities n standbyPhase mainPhase resolves? drawPhase n lifeEqualizer 0 standbyPhase mainPhase bounce trueDraco nextPhase endPhase bounce even drawPhase n levelReturner 1 standbyPhase nextPhase endPhase"
prog = prog.split()


lexed = lexYugiCode(prog, [])
print(lexed)