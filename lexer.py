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

tokenDict = dict()
tokenDict['summon'] = ("function definition", lambda: FunctionDef())
tokenDict['stamp'] = ("Bool", lambda: Bool())
tokenDict['gloriousNumbers'] = ("Int", lambda: Int())
tokenDict['TrueKingOfAllCalamities'] = ("Unsigned int", lambda: UnsignedInt())
tokenDict['drawPhase'] = ("OpenParen", lambda: OpenParen())
tokenDict['standbyPhase'] = ("CloseParen", lambda: CloseParen())
tokenDict['mainPhase'] = ("OpenCurly", lambda: OpenCurly())
tokenDict['endPhase'] = ("CloseCurly", lambda: CloseCurly())
tokenDict['nextPhase'] = ("Semicolon", lambda: Semicolon())
tokenDict['resolves?'] = ("If", lambda: IfStatement())
tokenDict['lifeEqualizer'] = ("EqualCheck", lambda: EqualCheck())
tokenDict['levelReturner'] = ("Subtract", lambda: Subtract())
tokenDict['mathmechAddition'] = ("Add", lambda: Add())
tokenDict['trueDraco'] = ("True", lambda: TrueToken())
tokenDict['solemnJudgment'] = ("False", lambda: FalseToken())
tokenDict['bounce'] = ("Return", lambda: Return())
tokenDict['Variable'] = ('Variable', lambda: Variable())

def lexYugiCode(prog: str, lexed: list[Token]) -> List[Token]:
    if not prog:
        return lexed

    c, *progrest = prog

    if c in possibleTokens:
        lexed.append(tokenDict[c][1]())
    elif type(lexed[-1]) not in typeList:
        lexed[-1] = lexed[-1].setValue(c)
    else:
        lexed.append(tokenDict['Variable'][1]())
        lexed[-1] = lexed[-1].setValue(c)

    return lexYugiCode(progrest, lexed)


def extractWords(prog: str, words: List[str], word: str = ""):
    if not prog:
        return words

    c, *progrest = prog

    if c == " ":
        words.append(word)
        return extractWords(progrest, words, "")
    else:
        word += c
        return extractWords(progrest, words, word)