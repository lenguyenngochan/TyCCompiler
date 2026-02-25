# Generated from D:/tyc-compiler-main/tyc-compiler-main/src/grammar/TyC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,449,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,106,8,1,
        1,2,1,2,3,2,110,8,2,1,3,1,3,1,4,1,4,3,4,116,8,4,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,129,8,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,144,8,8,1,9,1,9,1,9,1,9,1,9,3,9,
        151,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,162,8,
        10,1,11,1,11,3,11,166,8,11,1,12,1,12,1,12,3,12,171,8,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,3,14,189,8,14,1,15,1,15,3,15,193,8,15,1,16,1,16,1,16,1,16,1,
        17,1,17,3,17,201,8,17,1,18,1,18,1,18,1,18,3,18,207,8,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,220,8,19,1,20,
        1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,246,8,23,
        1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,3,26,267,8,26,1,27,1,27,3,27,271,8,
        27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,3,29,282,8,29,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,3,30,303,8,30,1,31,1,31,1,31,1,32,1,
        32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,3,33,317,8,33,1,34,1,34,1,
        34,1,35,1,35,1,35,1,35,1,35,3,35,327,8,35,1,36,1,36,1,36,1,36,1,
        36,1,36,5,36,335,8,36,10,36,12,36,338,9,36,1,37,1,37,1,37,1,37,1,
        37,1,37,5,37,346,8,37,10,37,12,37,349,9,37,1,38,1,38,1,38,1,38,1,
        38,1,38,5,38,357,8,38,10,38,12,38,360,9,38,1,39,1,39,1,39,1,39,1,
        39,1,39,5,39,368,8,39,10,39,12,39,371,9,39,1,40,1,40,1,40,1,40,1,
        40,1,40,5,40,379,8,40,10,40,12,40,382,9,40,1,41,1,41,1,41,1,41,1,
        41,1,41,5,41,390,8,41,10,41,12,41,393,9,41,1,42,1,42,1,42,1,42,1,
        42,1,42,5,42,401,8,42,10,42,12,42,404,9,42,1,43,1,43,1,43,3,43,409,
        8,43,1,44,1,44,1,44,3,44,414,8,44,1,45,1,45,1,45,1,45,3,45,420,8,
        45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,
        46,1,46,3,46,436,8,46,1,47,1,47,3,47,440,8,47,1,48,1,48,1,48,1,48,
        1,48,3,48,447,8,48,1,48,0,7,72,74,76,78,80,82,84,49,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,0,
        8,3,0,9,9,12,12,14,14,2,0,21,21,49,51,1,0,27,28,1,0,29,32,1,0,22,
        23,1,0,24,26,2,0,22,23,35,35,1,0,36,37,449,0,98,1,0,0,0,2,105,1,
        0,0,0,4,109,1,0,0,0,6,111,1,0,0,0,8,115,1,0,0,0,10,117,1,0,0,0,12,
        128,1,0,0,0,14,130,1,0,0,0,16,143,1,0,0,0,18,150,1,0,0,0,20,161,
        1,0,0,0,22,165,1,0,0,0,24,170,1,0,0,0,26,180,1,0,0,0,28,188,1,0,
        0,0,30,192,1,0,0,0,32,194,1,0,0,0,34,200,1,0,0,0,36,206,1,0,0,0,
        38,219,1,0,0,0,40,221,1,0,0,0,42,224,1,0,0,0,44,228,1,0,0,0,46,245,
        1,0,0,0,48,247,1,0,0,0,50,253,1,0,0,0,52,266,1,0,0,0,54,270,1,0,
        0,0,56,272,1,0,0,0,58,281,1,0,0,0,60,302,1,0,0,0,62,304,1,0,0,0,
        64,307,1,0,0,0,66,316,1,0,0,0,68,318,1,0,0,0,70,326,1,0,0,0,72,328,
        1,0,0,0,74,339,1,0,0,0,76,350,1,0,0,0,78,361,1,0,0,0,80,372,1,0,
        0,0,82,383,1,0,0,0,84,394,1,0,0,0,86,408,1,0,0,0,88,413,1,0,0,0,
        90,419,1,0,0,0,92,435,1,0,0,0,94,439,1,0,0,0,96,446,1,0,0,0,98,99,
        3,2,1,0,99,100,5,0,0,1,100,1,1,0,0,0,101,102,3,4,2,0,102,103,3,2,
        1,0,103,106,1,0,0,0,104,106,1,0,0,0,105,101,1,0,0,0,105,104,1,0,
        0,0,106,3,1,0,0,0,107,110,3,14,7,0,108,110,3,24,12,0,109,107,1,0,
        0,0,109,108,1,0,0,0,110,5,1,0,0,0,111,112,7,0,0,0,112,7,1,0,0,0,
        113,116,3,6,3,0,114,116,5,51,0,0,115,113,1,0,0,0,115,114,1,0,0,0,
        116,9,1,0,0,0,117,118,7,1,0,0,118,11,1,0,0,0,119,120,3,8,4,0,120,
        121,5,51,0,0,121,122,5,46,0,0,122,123,3,12,6,0,123,129,1,0,0,0,124,
        125,3,8,4,0,125,126,5,51,0,0,126,127,5,46,0,0,127,129,1,0,0,0,128,
        119,1,0,0,0,128,124,1,0,0,0,129,13,1,0,0,0,130,131,5,15,0,0,131,
        132,5,51,0,0,132,133,5,42,0,0,133,134,3,12,6,0,134,135,5,43,0,0,
        135,136,5,46,0,0,136,15,1,0,0,0,137,138,5,51,0,0,138,139,5,39,0,
        0,139,144,3,16,8,0,140,141,5,51,0,0,141,142,5,39,0,0,142,144,5,51,
        0,0,143,137,1,0,0,0,143,140,1,0,0,0,144,17,1,0,0,0,145,146,5,3,0,
        0,146,151,5,51,0,0,147,148,3,8,4,0,148,149,5,51,0,0,149,151,1,0,
        0,0,150,145,1,0,0,0,150,147,1,0,0,0,151,19,1,0,0,0,152,153,5,3,0,
        0,153,154,5,51,0,0,154,155,5,38,0,0,155,162,3,70,35,0,156,157,3,
        8,4,0,157,158,5,51,0,0,158,159,5,38,0,0,159,160,3,70,35,0,160,162,
        1,0,0,0,161,152,1,0,0,0,161,156,1,0,0,0,162,21,1,0,0,0,163,166,3,
        18,9,0,164,166,3,20,10,0,165,163,1,0,0,0,165,164,1,0,0,0,166,23,
        1,0,0,0,167,171,3,8,4,0,168,171,5,3,0,0,169,171,5,17,0,0,170,167,
        1,0,0,0,170,168,1,0,0,0,170,169,1,0,0,0,171,172,1,0,0,0,172,173,
        5,51,0,0,173,174,5,44,0,0,174,175,3,30,15,0,175,176,5,45,0,0,176,
        177,5,42,0,0,177,178,3,36,18,0,178,179,5,43,0,0,179,25,1,0,0,0,180,
        181,3,8,4,0,181,182,5,51,0,0,182,27,1,0,0,0,183,184,3,26,13,0,184,
        185,5,47,0,0,185,186,3,28,14,0,186,189,1,0,0,0,187,189,3,26,13,0,
        188,183,1,0,0,0,188,187,1,0,0,0,189,29,1,0,0,0,190,193,3,28,14,0,
        191,193,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,0,193,31,1,0,0,0,194,
        195,3,34,17,0,195,196,5,38,0,0,196,197,3,70,35,0,197,33,1,0,0,0,
        198,201,5,51,0,0,199,201,3,16,8,0,200,198,1,0,0,0,200,199,1,0,0,
        0,201,35,1,0,0,0,202,203,3,38,19,0,203,204,3,36,18,0,204,207,1,0,
        0,0,205,207,1,0,0,0,206,202,1,0,0,0,206,205,1,0,0,0,207,37,1,0,0,
        0,208,220,3,40,20,0,209,220,3,42,21,0,210,220,3,44,22,0,211,220,
        3,46,23,0,212,220,3,48,24,0,213,220,3,50,25,0,214,220,3,60,30,0,
        215,220,3,62,31,0,216,220,3,64,32,0,217,220,3,66,33,0,218,220,3,
        68,34,0,219,208,1,0,0,0,219,209,1,0,0,0,219,210,1,0,0,0,219,211,
        1,0,0,0,219,212,1,0,0,0,219,213,1,0,0,0,219,214,1,0,0,0,219,215,
        1,0,0,0,219,216,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,39,1,
        0,0,0,221,222,3,22,11,0,222,223,5,46,0,0,223,41,1,0,0,0,224,225,
        5,42,0,0,225,226,3,36,18,0,226,227,5,43,0,0,227,43,1,0,0,0,228,229,
        3,32,16,0,229,230,5,46,0,0,230,45,1,0,0,0,231,232,5,11,0,0,232,233,
        5,44,0,0,233,234,3,70,35,0,234,235,5,45,0,0,235,236,3,38,19,0,236,
        246,1,0,0,0,237,238,5,11,0,0,238,239,5,44,0,0,239,240,3,70,35,0,
        240,241,5,45,0,0,241,242,3,38,19,0,242,243,5,8,0,0,243,244,3,38,
        19,0,244,246,1,0,0,0,245,231,1,0,0,0,245,237,1,0,0,0,246,47,1,0,
        0,0,247,248,5,18,0,0,248,249,5,44,0,0,249,250,3,70,35,0,250,251,
        5,45,0,0,251,252,3,38,19,0,252,49,1,0,0,0,253,254,5,10,0,0,254,255,
        5,44,0,0,255,256,3,52,26,0,256,257,5,46,0,0,257,258,3,54,27,0,258,
        259,5,46,0,0,259,260,3,54,27,0,260,261,5,45,0,0,261,262,3,38,19,
        0,262,51,1,0,0,0,263,267,3,22,11,0,264,267,3,32,16,0,265,267,1,0,
        0,0,266,263,1,0,0,0,266,264,1,0,0,0,266,265,1,0,0,0,267,53,1,0,0,
        0,268,271,3,70,35,0,269,271,1,0,0,0,270,268,1,0,0,0,270,269,1,0,
        0,0,271,55,1,0,0,0,272,273,5,5,0,0,273,274,3,70,35,0,274,275,5,48,
        0,0,275,276,3,36,18,0,276,57,1,0,0,0,277,278,3,56,28,0,278,279,3,
        58,29,0,279,282,1,0,0,0,280,282,3,56,28,0,281,277,1,0,0,0,281,280,
        1,0,0,0,282,59,1,0,0,0,283,284,5,16,0,0,284,285,5,44,0,0,285,286,
        3,70,35,0,286,287,5,45,0,0,287,288,5,42,0,0,288,289,3,58,29,0,289,
        290,5,43,0,0,290,303,1,0,0,0,291,292,5,16,0,0,292,293,5,44,0,0,293,
        294,3,70,35,0,294,295,5,45,0,0,295,296,5,42,0,0,296,297,3,58,29,
        0,297,298,5,7,0,0,298,299,5,48,0,0,299,300,3,36,18,0,300,301,5,43,
        0,0,301,303,1,0,0,0,302,283,1,0,0,0,302,291,1,0,0,0,303,61,1,0,0,
        0,304,305,5,4,0,0,305,306,5,46,0,0,306,63,1,0,0,0,307,308,5,6,0,
        0,308,309,5,46,0,0,309,65,1,0,0,0,310,311,5,13,0,0,311,312,3,70,
        35,0,312,313,5,46,0,0,313,317,1,0,0,0,314,315,5,13,0,0,315,317,5,
        46,0,0,316,310,1,0,0,0,316,314,1,0,0,0,317,67,1,0,0,0,318,319,3,
        70,35,0,319,320,5,46,0,0,320,69,1,0,0,0,321,322,3,34,17,0,322,323,
        5,38,0,0,323,324,3,70,35,0,324,327,1,0,0,0,325,327,3,72,36,0,326,
        321,1,0,0,0,326,325,1,0,0,0,327,71,1,0,0,0,328,329,6,36,-1,0,329,
        330,3,74,37,0,330,336,1,0,0,0,331,332,10,2,0,0,332,333,5,33,0,0,
        333,335,3,74,37,0,334,331,1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,
        0,336,337,1,0,0,0,337,73,1,0,0,0,338,336,1,0,0,0,339,340,6,37,-1,
        0,340,341,3,76,38,0,341,347,1,0,0,0,342,343,10,2,0,0,343,344,5,34,
        0,0,344,346,3,76,38,0,345,342,1,0,0,0,346,349,1,0,0,0,347,345,1,
        0,0,0,347,348,1,0,0,0,348,75,1,0,0,0,349,347,1,0,0,0,350,351,6,38,
        -1,0,351,352,3,78,39,0,352,358,1,0,0,0,353,354,10,2,0,0,354,355,
        7,2,0,0,355,357,3,78,39,0,356,353,1,0,0,0,357,360,1,0,0,0,358,356,
        1,0,0,0,358,359,1,0,0,0,359,77,1,0,0,0,360,358,1,0,0,0,361,362,6,
        39,-1,0,362,363,3,80,40,0,363,369,1,0,0,0,364,365,10,2,0,0,365,366,
        7,3,0,0,366,368,3,80,40,0,367,364,1,0,0,0,368,371,1,0,0,0,369,367,
        1,0,0,0,369,370,1,0,0,0,370,79,1,0,0,0,371,369,1,0,0,0,372,373,6,
        40,-1,0,373,374,3,82,41,0,374,380,1,0,0,0,375,376,10,2,0,0,376,377,
        7,4,0,0,377,379,3,82,41,0,378,375,1,0,0,0,379,382,1,0,0,0,380,378,
        1,0,0,0,380,381,1,0,0,0,381,81,1,0,0,0,382,380,1,0,0,0,383,384,6,
        41,-1,0,384,385,3,84,42,0,385,391,1,0,0,0,386,387,10,2,0,0,387,388,
        7,5,0,0,388,390,3,84,42,0,389,386,1,0,0,0,390,393,1,0,0,0,391,389,
        1,0,0,0,391,392,1,0,0,0,392,83,1,0,0,0,393,391,1,0,0,0,394,395,6,
        42,-1,0,395,396,3,86,43,0,396,402,1,0,0,0,397,398,10,2,0,0,398,399,
        5,39,0,0,399,401,3,86,43,0,400,397,1,0,0,0,401,404,1,0,0,0,402,400,
        1,0,0,0,402,403,1,0,0,0,403,85,1,0,0,0,404,402,1,0,0,0,405,406,7,
        6,0,0,406,409,3,86,43,0,407,409,3,88,44,0,408,405,1,0,0,0,408,407,
        1,0,0,0,409,87,1,0,0,0,410,411,7,7,0,0,411,414,3,90,45,0,412,414,
        3,90,45,0,413,410,1,0,0,0,413,412,1,0,0,0,414,89,1,0,0,0,415,416,
        3,92,46,0,416,417,7,7,0,0,417,420,1,0,0,0,418,420,3,92,46,0,419,
        415,1,0,0,0,419,418,1,0,0,0,420,91,1,0,0,0,421,436,5,51,0,0,422,
        436,5,50,0,0,423,436,5,49,0,0,424,436,5,21,0,0,425,426,5,44,0,0,
        426,427,3,70,35,0,427,428,5,45,0,0,428,436,1,0,0,0,429,430,5,51,
        0,0,430,431,5,44,0,0,431,432,3,94,47,0,432,433,5,45,0,0,433,436,
        1,0,0,0,434,436,3,16,8,0,435,421,1,0,0,0,435,422,1,0,0,0,435,423,
        1,0,0,0,435,424,1,0,0,0,435,425,1,0,0,0,435,429,1,0,0,0,435,434,
        1,0,0,0,436,93,1,0,0,0,437,440,3,96,48,0,438,440,1,0,0,0,439,437,
        1,0,0,0,439,438,1,0,0,0,440,95,1,0,0,0,441,442,3,70,35,0,442,443,
        5,47,0,0,443,444,3,96,48,0,444,447,1,0,0,0,445,447,3,70,35,0,446,
        441,1,0,0,0,446,445,1,0,0,0,447,97,1,0,0,0,34,105,109,115,128,143,
        150,161,165,170,188,192,200,206,219,245,266,270,281,302,316,326,
        336,347,358,369,380,391,402,408,413,419,435,439,446
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'case'", "'continue'", "'default'", "'else'", "'float'", 
                     "'for'", "'if'", "'int'", "'return'", "'string'", "'struct'", 
                     "'switch'", "'void'", "'while'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'++'", "'--'", "'='", "'.'", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "CMTONE", "CMTTWO", "AUTO", "BREAK", 
                      "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", 
                      "IF", "INT", "RETURN", "STRING", "STRUCT", "SWITCH", 
                      "VOID", "WHILE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "STRINGLIT", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                      "NOTEQ", "LESS", "GREATER", "LEQU", "GREQ", "OR", 
                      "AND", "NOT", "INCRE", "DECRE", "ASS", "ACC", "LS", 
                      "RS", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "COLON", 
                      "FLOATLIT", "INTLIT", "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declist = 1
    RULE_decl = 2
    RULE_primitive_type = 3
    RULE_type = 4
    RULE_init = 5
    RULE_memstructlst = 6
    RULE_structdecl = 7
    RULE_structmemacc = 8
    RULE_vardecl_no_init = 9
    RULE_vardecl_with_init = 10
    RULE_vardecl = 11
    RULE_funcdecl = 12
    RULE_param = 13
    RULE_paramprime = 14
    RULE_paramlist = 15
    RULE_ass = 16
    RULE_lhs = 17
    RULE_stmtlist = 18
    RULE_stmt = 19
    RULE_vardeclstmt = 20
    RULE_blockstmt = 21
    RULE_asstmt = 22
    RULE_ifstmt = 23
    RULE_whilestmt = 24
    RULE_forstmt = 25
    RULE_for_init = 26
    RULE_for_exp = 27
    RULE_caseclause = 28
    RULE_caselist = 29
    RULE_switchstmt = 30
    RULE_breakstmt = 31
    RULE_contstmt = 32
    RULE_retstmt = 33
    RULE_expstmt = 34
    RULE_exp = 35
    RULE_exp1 = 36
    RULE_exp2 = 37
    RULE_exp3 = 38
    RULE_exp4 = 39
    RULE_exp5 = 40
    RULE_exp6 = 41
    RULE_exp7 = 42
    RULE_exp8 = 43
    RULE_exp9 = 44
    RULE_exp10 = 45
    RULE_exp11 = 46
    RULE_arglist = 47
    RULE_argprime = 48

    ruleNames =  [ "program", "declist", "decl", "primitive_type", "type", 
                   "init", "memstructlst", "structdecl", "structmemacc", 
                   "vardecl_no_init", "vardecl_with_init", "vardecl", "funcdecl", 
                   "param", "paramprime", "paramlist", "ass", "lhs", "stmtlist", 
                   "stmt", "vardeclstmt", "blockstmt", "asstmt", "ifstmt", 
                   "whilestmt", "forstmt", "for_init", "for_exp", "caseclause", 
                   "caselist", "switchstmt", "breakstmt", "contstmt", "retstmt", 
                   "expstmt", "exp", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "exp10", "exp11", "arglist", 
                   "argprime" ]

    EOF = Token.EOF
    CMTONE=1
    CMTTWO=2
    AUTO=3
    BREAK=4
    CASE=5
    CONTINUE=6
    DEFAULT=7
    ELSE=8
    FLOAT=9
    FOR=10
    IF=11
    INT=12
    RETURN=13
    STRING=14
    STRUCT=15
    SWITCH=16
    VOID=17
    WHILE=18
    ILLEGAL_ESCAPE=19
    UNCLOSE_STRING=20
    STRINGLIT=21
    ADD=22
    SUB=23
    MUL=24
    DIV=25
    MOD=26
    EQUAL=27
    NOTEQ=28
    LESS=29
    GREATER=30
    LEQU=31
    GREQ=32
    OR=33
    AND=34
    NOT=35
    INCRE=36
    DECRE=37
    ASS=38
    ACC=39
    LS=40
    RS=41
    LB=42
    RB=43
    LP=44
    RP=45
    SEMI=46
    COMMA=47
    COLON=48
    FLOATLIT=49
    INTLIT=50
    ID=51
    WS=52
    ERROR_CHAR=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declist(self):
            return self.getTypedRuleContext(TyCParser.DeclistContext,0)


        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.declist()
            self.state = 99
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(TyCParser.DeclContext,0)


        def declist(self):
            return self.getTypedRuleContext(TyCParser.DeclistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_declist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclist" ):
                return visitor.visitDeclist(self)
            else:
                return visitor.visitChildren(self)




    def declist(self):

        localctx = TyCParser.DeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declist)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 9, 12, 14, 15, 17, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.decl()
                self.state = 102
                self.declist()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structdecl(self):
            return self.getTypedRuleContext(TyCParser.StructdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(TyCParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = TyCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.structdecl()
                pass
            elif token in [3, 9, 12, 14, 17, 51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = TyCParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 20992) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(TyCParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = TyCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 12, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.primitive_type()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(TyCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(TyCParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(TyCParser.STRINGLIT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = TyCParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3940649676046336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemstructlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def memstructlst(self):
            return self.getTypedRuleContext(TyCParser.MemstructlstContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_memstructlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemstructlst" ):
                return visitor.visitMemstructlst(self)
            else:
                return visitor.visitChildren(self)




    def memstructlst(self):

        localctx = TyCParser.MemstructlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_memstructlst)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.type_()
                self.state = 120
                self.match(TyCParser.ID)
                self.state = 121
                self.match(TyCParser.SEMI)
                self.state = 122
                self.memstructlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.type_()
                self.state = 125
                self.match(TyCParser.ID)
                self.state = 126
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def memstructlst(self):
            return self.getTypedRuleContext(TyCParser.MemstructlstContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = TyCParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(TyCParser.STRUCT)
            self.state = 131
            self.match(TyCParser.ID)
            self.state = 132
            self.match(TyCParser.LB)
            self.state = 133
            self.memstructlst()
            self.state = 134
            self.match(TyCParser.RB)
            self.state = 135
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructmemaccContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def ACC(self):
            return self.getToken(TyCParser.ACC, 0)

        def structmemacc(self):
            return self.getTypedRuleContext(TyCParser.StructmemaccContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_structmemacc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructmemacc" ):
                return visitor.visitStructmemacc(self)
            else:
                return visitor.visitChildren(self)




    def structmemacc(self):

        localctx = TyCParser.StructmemaccContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structmemacc)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(TyCParser.ID)
                self.state = 138
                self.match(TyCParser.ACC)
                self.state = 139
                self.structmemacc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(TyCParser.ID)
                self.state = 141
                self.match(TyCParser.ACC)
                self.state = 142
                self.match(TyCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_no_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_vardecl_no_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_no_init" ):
                return visitor.visitVardecl_no_init(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_no_init(self):

        localctx = TyCParser.Vardecl_no_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vardecl_no_init)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(TyCParser.AUTO)
                self.state = 146
                self.match(TyCParser.ID)
                pass
            elif token in [9, 12, 14, 51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.type_()
                self.state = 148
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_with_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASS(self):
            return self.getToken(TyCParser.ASS, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_vardecl_with_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_with_init" ):
                return visitor.visitVardecl_with_init(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_with_init(self):

        localctx = TyCParser.Vardecl_with_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_vardecl_with_init)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(TyCParser.AUTO)
                self.state = 153
                self.match(TyCParser.ID)
                self.state = 154
                self.match(TyCParser.ASS)
                self.state = 155
                self.exp()
                pass
            elif token in [9, 12, 14, 51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.type_()
                self.state = 157
                self.match(TyCParser.ID)
                self.state = 158
                self.match(TyCParser.ASS)
                self.state = 159
                self.exp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl_no_init(self):
            return self.getTypedRuleContext(TyCParser.Vardecl_no_initContext,0)


        def vardecl_with_init(self):
            return self.getTypedRuleContext(TyCParser.Vardecl_with_initContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = TyCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vardecl)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.vardecl_no_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.vardecl_with_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(TyCParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = TyCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 12, 14, 51]:
                self.state = 167
                self.type_()
                pass
            elif token in [3]:
                self.state = 168
                self.match(TyCParser.AUTO)
                pass
            elif token in [17]:
                self.state = 169
                self.match(TyCParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 172
            self.match(TyCParser.ID)
            self.state = 173
            self.match(TyCParser.LP)
            self.state = 174
            self.paramlist()
            self.state = 175
            self.match(TyCParser.RP)
            self.state = 176
            self.match(TyCParser.LB)
            self.state = 177
            self.stmtlist()
            self.state = 178
            self.match(TyCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = TyCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.type_()
            self.state = 181
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(TyCParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(TyCParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = TyCParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramprime)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.param()
                self.state = 184
                self.match(TyCParser.COMMA)
                self.state = 185
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(TyCParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = TyCParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paramlist)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 12, 14, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.paramprime()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(TyCParser.LhsContext,0)


        def ASS(self):
            return self.getToken(TyCParser.ASS, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_ass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss" ):
                return visitor.visitAss(self)
            else:
                return visitor.visitChildren(self)




    def ass(self):

        localctx = TyCParser.AssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.lhs()
            self.state = 195
            self.match(TyCParser.ASS)
            self.state = 196
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def structmemacc(self):
            return self.getTypedRuleContext(TyCParser.StructmemaccContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = TyCParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lhs)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.structmemacc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = TyCParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmtlist)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 6, 9, 10, 11, 12, 13, 14, 16, 18, 21, 22, 23, 35, 36, 37, 42, 44, 49, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.stmt()
                self.state = 203
                self.stmtlist()
                pass
            elif token in [5, 7, 43]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclstmt(self):
            return self.getTypedRuleContext(TyCParser.VardeclstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(TyCParser.BlockstmtContext,0)


        def asstmt(self):
            return self.getTypedRuleContext(TyCParser.AsstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(TyCParser.IfstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(TyCParser.WhilestmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(TyCParser.ForstmtContext,0)


        def switchstmt(self):
            return self.getTypedRuleContext(TyCParser.SwitchstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(TyCParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(TyCParser.ContstmtContext,0)


        def retstmt(self):
            return self.getTypedRuleContext(TyCParser.RetstmtContext,0)


        def expstmt(self):
            return self.getTypedRuleContext(TyCParser.ExpstmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.vardeclstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.asstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.whilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.forstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.switchstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 215
                self.breakstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 216
                self.contstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 217
                self.retstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 218
                self.expstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_vardeclstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclstmt" ):
                return visitor.visitVardeclstmt(self)
            else:
                return visitor.visitChildren(self)




    def vardeclstmt(self):

        localctx = TyCParser.VardeclstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_vardeclstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.vardecl()
            self.state = 222
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = TyCParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(TyCParser.LB)
            self.state = 225
            self.stmtlist()
            self.state = 226
            self.match(TyCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ass(self):
            return self.getTypedRuleContext(TyCParser.AssContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_asstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsstmt" ):
                return visitor.visitAsstmt(self)
            else:
                return visitor.visitChildren(self)




    def asstmt(self):

        localctx = TyCParser.AsstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_asstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.ass()
            self.state = 229
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = TyCParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifstmt)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(TyCParser.IF)
                self.state = 232
                self.match(TyCParser.LP)
                self.state = 233
                self.exp()
                self.state = 234
                self.match(TyCParser.RP)
                self.state = 235
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(TyCParser.IF)
                self.state = 238
                self.match(TyCParser.LP)
                self.state = 239
                self.exp()
                self.state = 240
                self.match(TyCParser.RP)
                self.state = 241
                self.stmt()
                self.state = 242
                self.match(TyCParser.ELSE)
                self.state = 243
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = TyCParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(TyCParser.WHILE)
            self.state = 248
            self.match(TyCParser.LP)
            self.state = 249
            self.exp()
            self.state = 250
            self.match(TyCParser.RP)
            self.state = 251
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def for_init(self):
            return self.getTypedRuleContext(TyCParser.For_initContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMI)
            else:
                return self.getToken(TyCParser.SEMI, i)

        def for_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.For_expContext)
            else:
                return self.getTypedRuleContext(TyCParser.For_expContext,i)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = TyCParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(TyCParser.FOR)
            self.state = 254
            self.match(TyCParser.LP)
            self.state = 255
            self.for_init()
            self.state = 256
            self.match(TyCParser.SEMI)
            self.state = 257
            self.for_exp()
            self.state = 258
            self.match(TyCParser.SEMI)
            self.state = 259
            self.for_exp()
            self.state = 260
            self.match(TyCParser.RP)
            self.state = 261
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


        def ass(self):
            return self.getTypedRuleContext(TyCParser.AssContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_for_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init" ):
                return visitor.visitFor_init(self)
            else:
                return visitor.visitChildren(self)




    def for_init(self):

        localctx = TyCParser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_init)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.ass()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_for_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_exp" ):
                return visitor.visitFor_exp(self)
            else:
                return visitor.visitChildren(self)




    def for_exp(self):

        localctx = TyCParser.For_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_for_exp)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23, 35, 36, 37, 44, 49, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.exp()
                pass
            elif token in [45, 46]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_caseclause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseclause" ):
                return visitor.visitCaseclause(self)
            else:
                return visitor.visitChildren(self)




    def caseclause(self):

        localctx = TyCParser.CaseclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_caseclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(TyCParser.CASE)
            self.state = 273
            self.exp()
            self.state = 274
            self.match(TyCParser.COLON)
            self.state = 275
            self.stmtlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaselistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseclause(self):
            return self.getTypedRuleContext(TyCParser.CaseclauseContext,0)


        def caselist(self):
            return self.getTypedRuleContext(TyCParser.CaselistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_caselist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaselist" ):
                return visitor.visitCaselist(self)
            else:
                return visitor.visitChildren(self)




    def caselist(self):

        localctx = TyCParser.CaselistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_caselist)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.caseclause()
                self.state = 278
                self.caselist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.caseclause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def caselist(self):
            return self.getTypedRuleContext(TyCParser.CaselistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_switchstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchstmt" ):
                return visitor.visitSwitchstmt(self)
            else:
                return visitor.visitChildren(self)




    def switchstmt(self):

        localctx = TyCParser.SwitchstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switchstmt)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(TyCParser.SWITCH)
                self.state = 284
                self.match(TyCParser.LP)
                self.state = 285
                self.exp()
                self.state = 286
                self.match(TyCParser.RP)
                self.state = 287
                self.match(TyCParser.LB)
                self.state = 288
                self.caselist()
                self.state = 289
                self.match(TyCParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(TyCParser.SWITCH)
                self.state = 292
                self.match(TyCParser.LP)
                self.state = 293
                self.exp()
                self.state = 294
                self.match(TyCParser.RP)
                self.state = 295
                self.match(TyCParser.LB)
                self.state = 296
                self.caselist()
                self.state = 297
                self.match(TyCParser.DEFAULT)
                self.state = 298
                self.match(TyCParser.COLON)
                self.state = 299
                self.stmtlist()
                self.state = 300
                self.match(TyCParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = TyCParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(TyCParser.BREAK)
            self.state = 305
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_contstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContstmt" ):
                return visitor.visitContstmt(self)
            else:
                return visitor.visitChildren(self)




    def contstmt(self):

        localctx = TyCParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(TyCParser.CONTINUE)
            self.state = 308
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_retstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetstmt" ):
                return visitor.visitRetstmt(self)
            else:
                return visitor.visitChildren(self)




    def retstmt(self):

        localctx = TyCParser.RetstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_retstmt)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(TyCParser.RETURN)
                self.state = 311
                self.exp()
                self.state = 312
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.match(TyCParser.RETURN)
                self.state = 315
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpstmt" ):
                return visitor.visitExpstmt(self)
            else:
                return visitor.visitChildren(self)




    def expstmt(self):

        localctx = TyCParser.ExpstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.exp()
            self.state = 319
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(TyCParser.LhsContext,0)


        def ASS(self):
            return self.getToken(TyCParser.ASS, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def exp1(self):
            return self.getTypedRuleContext(TyCParser.Exp1Context,0)


        def getRuleIndex(self):
            return TyCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = TyCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.lhs()
                self.state = 322
                self.match(TyCParser.ASS)
                self.state = 323
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(TyCParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(TyCParser.Exp1Context,0)


        def OR(self):
            return self.getToken(TyCParser.OR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    self.match(TyCParser.OR)
                    self.state = 333
                    self.exp2(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(TyCParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(TyCParser.Exp2Context,0)


        def AND(self):
            return self.getToken(TyCParser.AND, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    self.match(TyCParser.AND)
                    self.state = 344
                    self.exp3(0) 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(TyCParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(TyCParser.Exp3Context,0)


        def EQUAL(self):
            return self.getToken(TyCParser.EQUAL, 0)

        def NOTEQ(self):
            return self.getToken(TyCParser.NOTEQ, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==28):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 355
                    self.exp4(0) 
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(TyCParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(TyCParser.Exp4Context,0)


        def LESS(self):
            return self.getToken(TyCParser.LESS, 0)

        def LEQU(self):
            return self.getToken(TyCParser.LEQU, 0)

        def GREATER(self):
            return self.getToken(TyCParser.GREATER, 0)

        def GREQ(self):
            return self.getToken(TyCParser.GREQ, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 366
                    self.exp5(0) 
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(TyCParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(TyCParser.Exp5Context,0)


        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)

        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.exp6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 375
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 376
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 377
                    self.exp6(0) 
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(TyCParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(TyCParser.Exp6Context,0)


        def MUL(self):
            return self.getToken(TyCParser.MUL, 0)

        def DIV(self):
            return self.getToken(TyCParser.DIV, 0)

        def MOD(self):
            return self.getToken(TyCParser.MOD, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 386
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 387
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 388
                    self.exp7(0) 
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(TyCParser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(TyCParser.Exp7Context,0)


        def ACC(self):
            return self.getToken(TyCParser.ACC, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 397
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 398
                    self.match(TyCParser.ACC)
                    self.state = 399
                    self.exp8() 
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(TyCParser.Exp8Context,0)


        def NOT(self):
            return self.getToken(TyCParser.NOT, 0)

        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)

        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)

        def exp9(self):
            return self.getTypedRuleContext(TyCParser.Exp9Context,0)


        def getRuleIndex(self):
            return TyCParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = TyCParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp8)
        self._la = 0 # Token type
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34372321280) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 406
                self.exp8()
                pass
            elif token in [21, 36, 37, 44, 49, 50, 51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.exp9()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(TyCParser.Exp10Context,0)


        def INCRE(self):
            return self.getToken(TyCParser.INCRE, 0)

        def DECRE(self):
            return self.getToken(TyCParser.DECRE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = TyCParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 411
                self.exp10()
                pass
            elif token in [21, 44, 49, 50, 51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.exp10()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp11(self):
            return self.getTypedRuleContext(TyCParser.Exp11Context,0)


        def INCRE(self):
            return self.getToken(TyCParser.INCRE, 0)

        def DECRE(self):
            return self.getToken(TyCParser.DECRE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = TyCParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.exp11()
                self.state = 416
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.exp11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def INTLIT(self):
            return self.getToken(TyCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(TyCParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(TyCParser.STRINGLIT, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def arglist(self):
            return self.getTypedRuleContext(TyCParser.ArglistContext,0)


        def structmemacc(self):
            return self.getTypedRuleContext(TyCParser.StructmemaccContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = TyCParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exp11)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(TyCParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 423
                self.match(TyCParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 424
                self.match(TyCParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 425
                self.match(TyCParser.LP)
                self.state = 426
                self.exp()
                self.state = 427
                self.match(TyCParser.RP)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 429
                self.match(TyCParser.ID)
                self.state = 430
                self.match(TyCParser.LP)
                self.state = 431
                self.arglist()
                self.state = 432
                self.match(TyCParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 434
                self.structmemacc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argprime(self):
            return self.getTypedRuleContext(TyCParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = TyCParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arglist)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23, 35, 36, 37, 44, 49, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.argprime()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(TyCParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def argprime(self):
            return self.getTypedRuleContext(TyCParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_argprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgprime" ):
                return visitor.visitArgprime(self)
            else:
                return visitor.visitChildren(self)




    def argprime(self):

        localctx = TyCParser.ArgprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_argprime)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.exp()
                self.state = 442
                self.match(TyCParser.COMMA)
                self.state = 443
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.exp1_sempred
        self._predicates[37] = self.exp2_sempred
        self._predicates[38] = self.exp3_sempred
        self._predicates[39] = self.exp4_sempred
        self._predicates[40] = self.exp5_sempred
        self._predicates[41] = self.exp6_sempred
        self._predicates[42] = self.exp7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




