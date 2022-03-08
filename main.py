from lexer import lexYugiCode, extractWords, Token


prog = "stamp odd drawPhase TrueKingOfAllCalamities n standbyPhase mainPhase resolves? drawPhase n lifeEqualizer 0 standbyPhase mainPhase bounce trueDraco nextPhase endPhase bounce even drawPhase n levelReturner 10 standbyPhase nextPhase endPhase"
progWords = extractWords(prog, [])

lexed = lexYugiCode(progWords, [])
print(lexed)
print(type(lexed[4]))
