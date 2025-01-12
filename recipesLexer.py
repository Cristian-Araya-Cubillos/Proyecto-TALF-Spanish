# Generated from C:/Users/Yukihana/IdeaProjects/Trabajo/src/recipes.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,36,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,2,4,2,19,8,2,11,2,12,2,20,1,3,4,3,24,8,3,11,3,12,
        3,25,1,4,1,4,1,5,4,5,31,8,5,11,5,12,5,32,1,5,1,5,0,0,6,1,1,3,2,5,
        3,7,4,9,5,11,6,1,0,4,14,0,65,90,97,122,161,161,169,169,173,173,177,
        177,179,179,186,186,195,195,353,353,8216,8216,8220,8220,8240,8240,
        65533,65533,1,0,48,57,2,0,44,44,124,124,3,0,9,10,13,13,32,32,38,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,1,13,1,0,0,0,3,15,1,0,0,0,5,18,1,0,0,0,7,23,1,0,0,0,9,27,
        1,0,0,0,11,30,1,0,0,0,13,14,5,40,0,0,14,2,1,0,0,0,15,16,5,41,0,0,
        16,4,1,0,0,0,17,19,7,0,0,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,1,0,
        0,0,20,21,1,0,0,0,21,6,1,0,0,0,22,24,7,1,0,0,23,22,1,0,0,0,24,25,
        1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,8,1,0,0,0,27,28,7,2,0,0,28,
        10,1,0,0,0,29,31,7,3,0,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,
        0,32,33,1,0,0,0,33,34,1,0,0,0,34,35,6,5,0,0,35,12,1,0,0,0,4,0,20,
        25,32,1,6,0,0
    ]

class recipesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    PALABRA = 3
    NUMERO = 4
    OPERADOR_LOGICO = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "PALABRA", "NUMERO", "OPERADOR_LOGICO", "WS" ]

    ruleNames = [ "T__0", "T__1", "PALABRA", "NUMERO", "OPERADOR_LOGICO", 
                  "WS" ]

    grammarFileName = "recipes.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


