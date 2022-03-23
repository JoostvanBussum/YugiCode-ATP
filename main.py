from lexer import lexYugiCode, extractWords, Token
from parseYugiCode import parse


prog = "summon odd stamp drawPhase TrueKingOfAllCalamities n standbyPhase mainPhase resolves? drawPhase n lifeEqualizer 0 standbyPhase mainPhase bounce trueDraco nextPhase endPhase bounce even drawPhase 10 levelReturner 10 standbyPhase nextPhase endPhase absoluteEnd"
progWords = extractWords(prog, [])

lexed = lexYugiCode(progWords, [])
print(lexed)
# parsed = parse(lexed)

# nodes = lexed[0:-1]
# print(nodes)
