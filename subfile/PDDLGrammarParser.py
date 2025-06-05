# Generated from PDDLGrammar.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u01d3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write("I\n\2\f\2\16\2L\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bp")
        buf.write("\n\b\3\b\3\b\3\b\5\bu\n\b\3\b\3\b\3\b\5\bz\n\b\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\13\5\13\u0085\n\13\3\f\3")
        buf.write("\f\3\f\5\f\u008a\n\f\3\r\7\r\u008d\n\r\f\r\16\r\u0090")
        buf.write("\13\r\3\r\6\r\u0093\n\r\r\r\16\r\u0094\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u009b\n\r\3\16\7\16\u009e\n\16\f\16\16\16\u00a1\13")
        buf.write("\16\3\16\6\16\u00a4\n\16\r\16\16\16\u00a5\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00ac\n\16\3\17\3\17\6\17\u00b0\n\17\r\17")
        buf.write("\16\17\u00b1\3\20\3\20\3\20\3\20\6\20\u00b8\n\20\r\20")
        buf.write("\16\20\u00b9\3\20\3\20\3\20\3\20\3\20\6\20\u00c1\n\20")
        buf.write("\r\20\16\20\u00c2\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00e2\n\20\3\21\3\21\3\21\7\21\u00e7\n\21\f\21\16")
        buf.write("\21\u00ea\13\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u0119\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u0121\n\22\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u0155\n\24\3\25\3\25\3\25\6\25\u015a\n\25\r")
        buf.write("\25\16\25\u015b\3\25\3\25\3\25\5\25\u0161\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\5\26\u016a\n\26\3\27\3\27")
        buf.write("\3\27\6\27\u016f\n\27\r\27\16\27\u0170\3\27\3\27\3\27")
        buf.write("\5\27\u0176\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\5\31\u0181\n\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\6\34\u018b\n\34\r\34\16\34\u018c\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\7\36")
        buf.write("\u019b\n\36\f\36\16\36\u019e\13\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\7\37\u01a5\n\37\f\37\16\37\u01a8\13\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u01d1\n\37\3\37\2\2 \2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<\2\5\5\2\33\33\37\37@@\3\2\30\31\3\2@A\2\u01ec\2>\3")
        buf.write("\2\2\2\4O\3\2\2\2\6U\3\2\2\2\b[\3\2\2\2\na\3\2\2\2\fc")
        buf.write("\3\2\2\2\16e\3\2\2\2\20}\3\2\2\2\22\177\3\2\2\2\24\u0084")
        buf.write("\3\2\2\2\26\u0089\3\2\2\2\30\u009a\3\2\2\2\32\u00ab\3")
        buf.write("\2\2\2\34\u00ad\3\2\2\2\36\u00e1\3\2\2\2 \u0118\3\2\2")
        buf.write("\2\"\u0120\3\2\2\2$\u0122\3\2\2\2&\u0154\3\2\2\2(\u0160")
        buf.write("\3\2\2\2*\u0169\3\2\2\2,\u0175\3\2\2\2.\u0177\3\2\2\2")
        buf.write("\60\u0180\3\2\2\2\62\u0182\3\2\2\2\64\u0184\3\2\2\2\66")
        buf.write("\u0186\3\2\2\28\u0190\3\2\2\2:\u0196\3\2\2\2<\u01d0\3")
        buf.write("\2\2\2>?\7$\2\2?@\7\5\2\2@A\7$\2\2AB\7\3\2\2BC\7@\2\2")
        buf.write("CD\7%\2\2DE\5\4\3\2EF\5\6\4\2FJ\5\b\5\2GI\5\16\b\2HG\3")
        buf.write("\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2LJ\3\2\2")
        buf.write("\2MN\7%\2\2N\3\3\2\2\2OP\7$\2\2PQ\7(\2\2QR\7!\2\2RS\5")
        buf.write("\32\16\2ST\7%\2\2T\5\3\2\2\2UV\7$\2\2VW\7(\2\2WX\7\20")
        buf.write("\2\2XY\5\24\13\2YZ\7%\2\2Z\7\3\2\2\2[\\\7$\2\2\\]\7(\2")
        buf.write("\2]^\7\22\2\2^_\5\24\13\2_`\7%\2\2`\t\3\2\2\2ab\7@\2\2")
        buf.write("b\13\3\2\2\2cd\t\2\2\2d\r\3\2\2\2ef\7$\2\2fg\7(\2\2gh")
        buf.write("\7\n\2\2ho\5\20\t\2ij\7(\2\2jk\7\17\2\2kl\7$\2\2lm\5\32")
        buf.write("\16\2mn\7%\2\2np\3\2\2\2oi\3\2\2\2op\3\2\2\2pt\3\2\2\2")
        buf.write("qr\7(\2\2rs\7\21\2\2su\5\24\13\2tq\3\2\2\2tu\3\2\2\2u")
        buf.write("y\3\2\2\2vw\7(\2\2wx\7\32\2\2xz\5\26\f\2yv\3\2\2\2yz\3")
        buf.write("\2\2\2z{\3\2\2\2{|\7%\2\2|\17\3\2\2\2}~\7@\2\2~\21\3\2")
        buf.write("\2\2\177\u0080\t\3\2\2\u0080\23\3\2\2\2\u0081\u0085\5")
        buf.write("\36\20\2\u0082\u0083\7$\2\2\u0083\u0085\7%\2\2\u0084\u0081")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0085\25\3\2\2\2\u0086\u008a")
        buf.write("\5(\25\2\u0087\u0088\7$\2\2\u0088\u008a\7%\2\2\u0089\u0086")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u008a\27\3\2\2\2\u008b\u008d")
        buf.write("\7@\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u009b\3\2\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0091\u0093\7@\2\2\u0092\u0091\3")
        buf.write("\2\2\2\u0093\u0094\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\7,\2\2\u0097")
        buf.write("\u0098\5\f\7\2\u0098\u0099\5\30\r\2\u0099\u009b\3\2\2")
        buf.write("\2\u009a\u008e\3\2\2\2\u009a\u0092\3\2\2\2\u009b\31\3")
        buf.write("\2\2\2\u009c\u009e\7B\2\2\u009d\u009c\3\2\2\2\u009e\u00a1")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00ac\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a4\7B\2\2")
        buf.write("\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8")
        buf.write("\7,\2\2\u00a8\u00a9\5\f\7\2\u00a9\u00aa\5\32\16\2\u00aa")
        buf.write("\u00ac\3\2\2\2\u00ab\u009f\3\2\2\2\u00ab\u00a3\3\2\2\2")
        buf.write("\u00ac\33\3\2\2\2\u00ad\u00af\7;\2\2\u00ae\u00b0\7B\2")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\35\3\2\2\2\u00b3\u00e2")
        buf.write("\5 \21\2\u00b4\u00b5\7$\2\2\u00b5\u00b7\78\2\2\u00b6\u00b8")
        buf.write("\5\36\20\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\7%\2\2\u00bc\u00e2\3\2\2\2\u00bd\u00be\7")
        buf.write("$\2\2\u00be\u00c0\79\2\2\u00bf\u00c1\5\36\20\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\7%\2\2")
        buf.write("\u00c5\u00e2\3\2\2\2\u00c6\u00c7\7$\2\2\u00c7\u00c8\7")
        buf.write(":\2\2\u00c8\u00c9\5\36\20\2\u00c9\u00ca\7%\2\2\u00ca\u00e2")
        buf.write("\3\2\2\2\u00cb\u00cc\7$\2\2\u00cc\u00cd\7<\2\2\u00cd\u00ce")
        buf.write("\5\36\20\2\u00ce\u00cf\5\36\20\2\u00cf\u00d0\7%\2\2\u00d0")
        buf.write("\u00e2\3\2\2\2\u00d1\u00d2\7$\2\2\u00d2\u00d3\7>\2\2\u00d3")
        buf.write("\u00d4\7$\2\2\u00d4\u00d5\5\32\16\2\u00d5\u00d6\7%\2\2")
        buf.write("\u00d6\u00d7\5\36\20\2\u00d7\u00d8\7%\2\2\u00d8\u00e2")
        buf.write("\3\2\2\2\u00d9\u00da\7$\2\2\u00da\u00db\7=\2\2\u00db\u00dc")
        buf.write("\7$\2\2\u00dc\u00dd\5\32\16\2\u00dd\u00de\7%\2\2\u00de")
        buf.write("\u00df\5\36\20\2\u00df\u00e0\7%\2\2\u00e0\u00e2\3\2\2")
        buf.write("\2\u00e1\u00b3\3\2\2\2\u00e1\u00b4\3\2\2\2\u00e1\u00bd")
        buf.write("\3\2\2\2\u00e1\u00c6\3\2\2\2\u00e1\u00cb\3\2\2\2\u00e1")
        buf.write("\u00d1\3\2\2\2\u00e1\u00d9\3\2\2\2\u00e2\37\3\2\2\2\u00e3")
        buf.write("\u00e4\7$\2\2\u00e4\u00e8\5\n\6\2\u00e5\u00e7\5&\24\2")
        buf.write("\u00e6\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3")
        buf.write("\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00eb\u00ec\7%\2\2\u00ec\u0119\3\2\2\2\u00ed")
        buf.write("\u00ee\7$\2\2\u00ee\u00ef\7\62\2\2\u00ef\u00f0\5&\24\2")
        buf.write("\u00f0\u00f1\5&\24\2\u00f1\u00f2\7%\2\2\u00f2\u0119\3")
        buf.write("\2\2\2\u00f3\u00f4\7$\2\2\u00f4\u00f5\7\63\2\2\u00f5\u00f6")
        buf.write("\5&\24\2\u00f6\u00f7\5&\24\2\u00f7\u00f8\7%\2\2\u00f8")
        buf.write("\u0119\3\2\2\2\u00f9\u00fa\7$\2\2\u00fa\u00fb\7\64\2\2")
        buf.write("\u00fb\u00fc\5&\24\2\u00fc\u00fd\5&\24\2\u00fd\u00fe\7")
        buf.write("%\2\2\u00fe\u0119\3\2\2\2\u00ff\u0100\7$\2\2\u0100\u0101")
        buf.write("\7\65\2\2\u0101\u0102\5&\24\2\u0102\u0103\5&\24\2\u0103")
        buf.write("\u0104\7%\2\2\u0104\u0119\3\2\2\2\u0105\u0106\7$\2\2\u0106")
        buf.write("\u0107\7\66\2\2\u0107\u0108\5&\24\2\u0108\u0109\5&\24")
        buf.write("\2\u0109\u010a\7%\2\2\u010a\u0119\3\2\2\2\u010b\u010c")
        buf.write("\7$\2\2\u010c\u010d\7\67\2\2\u010d\u010e\5&\24\2\u010e")
        buf.write("\u010f\5&\24\2\u010f\u0110\7%\2\2\u0110\u0119\3\2\2\2")
        buf.write("\u0111\u0112\7$\2\2\u0112\u0113\7\61\2\2\u0113\u0114\5")
        buf.write("&\24\2\u0114\u0115\5&\24\2\u0115\u0116\5&\24\2\u0116\u0117")
        buf.write("\7%\2\2\u0117\u0119\3\2\2\2\u0118\u00e3\3\2\2\2\u0118")
        buf.write("\u00ed\3\2\2\2\u0118\u00f3\3\2\2\2\u0118\u00f9\3\2\2\2")
        buf.write("\u0118\u00ff\3\2\2\2\u0118\u0105\3\2\2\2\u0118\u010b\3")
        buf.write("\2\2\2\u0118\u0111\3\2\2\2\u0119!\3\2\2\2\u011a\u0121")
        buf.write("\5 \21\2\u011b\u011c\7$\2\2\u011c\u011d\7:\2\2\u011d\u011e")
        buf.write("\5 \21\2\u011e\u011f\7%\2\2\u011f\u0121\3\2\2\2\u0120")
        buf.write("\u011a\3\2\2\2\u0120\u011b\3\2\2\2\u0121#\3\2\2\2\u0122")
        buf.write("\u0123\t\4\2\2\u0123%\3\2\2\2\u0124\u0155\7@\2\2\u0125")
        buf.write("\u0155\7B\2\2\u0126\u0155\7A\2\2\u0127\u0128\7$\2\2\u0128")
        buf.write("\u0129\5&\24\2\u0129\u012a\7%\2\2\u012a\u0155\3\2\2\2")
        buf.write("\u012b\u012c\7$\2\2\u012c\u012d\7,\2\2\u012d\u012e\5&")
        buf.write("\24\2\u012e\u012f\7%\2\2\u012f\u0155\3\2\2\2\u0130\u0131")
        buf.write("\7$\2\2\u0131\u0132\7,\2\2\u0132\u0133\5&\24\2\u0133\u0134")
        buf.write("\5&\24\2\u0134\u0135\7%\2\2\u0135\u0155\3\2\2\2\u0136")
        buf.write("\u0137\7$\2\2\u0137\u0138\7\60\2\2\u0138\u0139\5&\24\2")
        buf.write("\u0139\u013a\5&\24\2\u013a\u013b\7%\2\2\u013b\u0155\3")
        buf.write("\2\2\2\u013c\u013d\7$\2\2\u013d\u013e\5&\24\2\u013e\u013f")
        buf.write("\7,\2\2\u013f\u0140\5&\24\2\u0140\u0141\7%\2\2\u0141\u0155")
        buf.write("\3\2\2\2\u0142\u0143\7$\2\2\u0143\u0144\5&\24\2\u0144")
        buf.write("\u0145\7\60\2\2\u0145\u0146\5&\24\2\u0146\u0147\7%\2\2")
        buf.write("\u0147\u0155\3\2\2\2\u0148\u0149\7$\2\2\u0149\u014a\7")
        buf.write("-\2\2\u014a\u014b\5&\24\2\u014b\u014c\5&\24\2\u014c\u014d")
        buf.write("\7%\2\2\u014d\u0155\3\2\2\2\u014e\u014f\7$\2\2\u014f\u0150")
        buf.write("\7.\2\2\u0150\u0151\5&\24\2\u0151\u0152\5&\24\2\u0152")
        buf.write("\u0153\7%\2\2\u0153\u0155\3\2\2\2\u0154\u0124\3\2\2\2")
        buf.write("\u0154\u0125\3\2\2\2\u0154\u0126\3\2\2\2\u0154\u0127\3")
        buf.write("\2\2\2\u0154\u012b\3\2\2\2\u0154\u0130\3\2\2\2\u0154\u0136")
        buf.write("\3\2\2\2\u0154\u013c\3\2\2\2\u0154\u0142\3\2\2\2\u0154")
        buf.write("\u0148\3\2\2\2\u0154\u014e\3\2\2\2\u0155\'\3\2\2\2\u0156")
        buf.write("\u0157\7$\2\2\u0157\u0159\78\2\2\u0158\u015a\5*\26\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\7")
        buf.write("%\2\2\u015e\u0161\3\2\2\2\u015f\u0161\5*\26\2\u0160\u0156")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161)\3\2\2\2\u0162\u0163")
        buf.write("\7$\2\2\u0163\u0164\7?\2\2\u0164\u0165\5\36\20\2\u0165")
        buf.write("\u0166\5,\27\2\u0166\u0167\7%\2\2\u0167\u016a\3\2\2\2")
        buf.write("\u0168\u016a\5.\30\2\u0169\u0162\3\2\2\2\u0169\u0168\3")
        buf.write("\2\2\2\u016a+\3\2\2\2\u016b\u016c\7$\2\2\u016c\u016e\7")
        buf.write("8\2\2\u016d\u016f\5.\30\2\u016e\u016d\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0173\7%\2\2\u0173\u0176\3\2\2\2")
        buf.write("\u0174\u0176\5.\30\2\u0175\u016b\3\2\2\2\u0175\u0174\3")
        buf.write("\2\2\2\u0176-\3\2\2\2\u0177\u0178\7$\2\2\u0178\u0179\5")
        buf.write("\60\31\2\u0179\u017a\7B\2\2\u017a\u017b\5&\24\2\u017b")
        buf.write("\u017c\7%\2\2\u017c/\3\2\2\2\u017d\u0181\7\34\2\2\u017e")
        buf.write("\u0181\7\35\2\2\u017f\u0181\7\36\2\2\u0180\u017d\3\2\2")
        buf.write("\2\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181\61\3")
        buf.write("\2\2\2\u0182\u0183\7@\2\2\u0183\63\3\2\2\2\u0184\u0185")
        buf.write("\7@\2\2\u0185\65\3\2\2\2\u0186\u0187\7$\2\2\u0187\u0188")
        buf.write("\7(\2\2\u0188\u018a\7\37\2\2\u0189\u018b\7@\2\2\u018a")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\7")
        buf.write("%\2\2\u018f\67\3\2\2\2\u0190\u0191\7$\2\2\u0191\u0192")
        buf.write("\7(\2\2\u0192\u0193\7!\2\2\u0193\u0194\5\30\r\2\u0194")
        buf.write("\u0195\7%\2\2\u01959\3\2\2\2\u0196\u0197\7$\2\2\u0197")
        buf.write("\u0198\7(\2\2\u0198\u019c\7\"\2\2\u0199\u019b\5<\37\2")
        buf.write("\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019f\u01a0\7%\2\2\u01a0;\3\2\2\2\u01a1\u01a2")
        buf.write("\7$\2\2\u01a2\u01a6\5\n\6\2\u01a3\u01a5\5$\23\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a9\u01aa\7%\2\2\u01aa\u01d1\3\2\2\2\u01ab\u01ac")
        buf.write("\7$\2\2\u01ac\u01ad\7\62\2\2\u01ad\u01ae\5$\23\2\u01ae")
        buf.write("\u01af\5$\23\2\u01af\u01b0\7%\2\2\u01b0\u01d1\3\2\2\2")
        buf.write("\u01b1\u01b2\7$\2\2\u01b2\u01b3\7\64\2\2\u01b3\u01b4\5")
        buf.write("$\23\2\u01b4\u01b5\5$\23\2\u01b5\u01b6\7%\2\2\u01b6\u01d1")
        buf.write("\3\2\2\2\u01b7\u01b8\7$\2\2\u01b8\u01b9\7\65\2\2\u01b9")
        buf.write("\u01ba\5$\23\2\u01ba\u01bb\5$\23\2\u01bb\u01bc\7%\2\2")
        buf.write("\u01bc\u01d1\3\2\2\2\u01bd\u01be\7$\2\2\u01be\u01bf\7")
        buf.write("\66\2\2\u01bf\u01c0\5$\23\2\u01c0\u01c1\5$\23\2\u01c1")
        buf.write("\u01c2\7%\2\2\u01c2\u01d1\3\2\2\2\u01c3\u01c4\7$\2\2\u01c4")
        buf.write("\u01c5\7\67\2\2\u01c5\u01c6\5$\23\2\u01c6\u01c7\5$\23")
        buf.write("\2\u01c7\u01c8\7%\2\2\u01c8\u01d1\3\2\2\2\u01c9\u01ca")
        buf.write("\7$\2\2\u01ca\u01cb\7\61\2\2\u01cb\u01cc\5$\23\2\u01cc")
        buf.write("\u01cd\5$\23\2\u01cd\u01ce\5$\23\2\u01ce\u01cf\7%\2\2")
        buf.write("\u01cf\u01d1\3\2\2\2\u01d0\u01a1\3\2\2\2\u01d0\u01ab\3")
        buf.write("\2\2\2\u01d0\u01b1\3\2\2\2\u01d0\u01b7\3\2\2\2\u01d0\u01bd")
        buf.write("\3\2\2\2\u01d0\u01c3\3\2\2\2\u01d0\u01c9\3\2\2\2\u01d1")
        buf.write("=\3\2\2\2 Joty\u0084\u0089\u008e\u0094\u009a\u009f\u00a5")
        buf.write("\u00ab\u00b1\u00b9\u00c2\u00e1\u00e8\u0118\u0120\u0154")
        buf.write("\u015b\u0160\u0169\u0170\u0175\u0180\u018c\u019c\u01a6")
        buf.write("\u01d0")
        return buf.getvalue()


class PDDLGrammarParser ( Parser ):

    grammarFileName = "PDDLGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'domain'", "'problem'", "'define'", "'agentid'", 
                     "'constants'", "'type'", "'predicates'", "'action'", 
                     "'event'", "'events'", "'pldegree'", "'eventmodel'", 
                     "'parameters'", "'tercondition'", "'precondition'", 
                     "'constraint'", "'response'", "'observation'", "'min'", 
                     "'max'", "'numbers'", "'normal'", "'misere'", "'effect'", 
                     "'object'", "'increase'", "'decrease'", "'assign'", 
                     "'agent'", "'either'", "'objects'", "'init'", "'goal'", 
                     "'('", "')'", "'['", "']'", "':'", "'?'", "'.'", "'_'", 
                     "'-'", "'+'", "'*'", "'/'", "'%'", "'%='", "'='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'and'", "'or'", "'not'", 
                     "'oneof'", "'Implies'", "'forall'", "'exists'", "'when'" ]

    symbolicNames = [ "<INVALID>", "DOMAIN", "PROBLEM", "DEFINE", "AGENTID", 
                      "CONST", "TYPE", "PREDICATE", "ACTION", "EVENT", "EVENTS", 
                      "PLDEGREE", "EVENTMODEL", "PARAMETER", "TERCONDITION", 
                      "PRECONDITION", "CONSTRAINT", "RESPONSE", "OBSERVATION", 
                      "MIN", "MAX", "NUMS", "NORMAL", "MISERE", "EFFECT", 
                      "OBJECT", "INC", "DEC", "ASSIGN", "AGENT", "EITHER", 
                      "OBJS", "INIT", "GOAL", "LB", "RB", "LSB", "RSB", 
                      "COLON", "QM", "POINT", "UL", "MINUS", "PLUS", "MULT", 
                      "DIV", "MOD", "MODTEST", "EQ", "NEQ", "LT", "LEQ", 
                      "GT", "GEQ", "AND", "OR", "NOT", "ONEOF", "IMPLIES", 
                      "FORALL", "EXISTS", "WHEN", "NAME", "INTEGER", "VAR", 
                      "FUNSYM", "WS" ]

    RULE_domain = 0
    RULE_objectDefine = 1
    RULE_terconditionDefine = 2
    RULE_constraintDefine = 3
    RULE_predicate = 4
    RULE_types = 5
    RULE_actionDefine = 6
    RULE_actionSymbol = 7
    RULE_typeName = 8
    RULE_emptyOrPreGD = 9
    RULE_emptyOrEffect = 10
    RULE_listName = 11
    RULE_listVariable = 12
    RULE_oneofDefine = 13
    RULE_gd = 14
    RULE_termAtomForm = 15
    RULE_termLiteral = 16
    RULE_constTerm = 17
    RULE_term = 18
    RULE_effect = 19
    RULE_cEffect = 20
    RULE_condEffect = 21
    RULE_pEffect = 22
    RULE_assignop = 23
    RULE_problemName = 24
    RULE_domainName = 25
    RULE_agentDefine = 26
    RULE_objectDeclaration = 27
    RULE_init = 28
    RULE_constTermAtomForm = 29

    ruleNames =  [ "domain", "objectDefine", "terconditionDefine", "constraintDefine", 
                   "predicate", "types", "actionDefine", "actionSymbol", 
                   "typeName", "emptyOrPreGD", "emptyOrEffect", "listName", 
                   "listVariable", "oneofDefine", "gd", "termAtomForm", 
                   "termLiteral", "constTerm", "term", "effect", "cEffect", 
                   "condEffect", "pEffect", "assignop", "problemName", "domainName", 
                   "agentDefine", "objectDeclaration", "init", "constTermAtomForm" ]

    EOF = Token.EOF
    DOMAIN=1
    PROBLEM=2
    DEFINE=3
    AGENTID=4
    CONST=5
    TYPE=6
    PREDICATE=7
    ACTION=8
    EVENT=9
    EVENTS=10
    PLDEGREE=11
    EVENTMODEL=12
    PARAMETER=13
    TERCONDITION=14
    PRECONDITION=15
    CONSTRAINT=16
    RESPONSE=17
    OBSERVATION=18
    MIN=19
    MAX=20
    NUMS=21
    NORMAL=22
    MISERE=23
    EFFECT=24
    OBJECT=25
    INC=26
    DEC=27
    ASSIGN=28
    AGENT=29
    EITHER=30
    OBJS=31
    INIT=32
    GOAL=33
    LB=34
    RB=35
    LSB=36
    RSB=37
    COLON=38
    QM=39
    POINT=40
    UL=41
    MINUS=42
    PLUS=43
    MULT=44
    DIV=45
    MOD=46
    MODTEST=47
    EQ=48
    NEQ=49
    LT=50
    LEQ=51
    GT=52
    GEQ=53
    AND=54
    OR=55
    NOT=56
    ONEOF=57
    IMPLIES=58
    FORALL=59
    EXISTS=60
    WHEN=61
    NAME=62
    INTEGER=63
    VAR=64
    FUNSYM=65
    WS=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DomainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.LB)
            else:
                return self.getToken(PDDLGrammarParser.LB, i)

        def DEFINE(self):
            return self.getToken(PDDLGrammarParser.DEFINE, 0)

        def DOMAIN(self):
            return self.getToken(PDDLGrammarParser.DOMAIN, 0)

        def NAME(self):
            return self.getToken(PDDLGrammarParser.NAME, 0)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.RB)
            else:
                return self.getToken(PDDLGrammarParser.RB, i)

        def objectDefine(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ObjectDefineContext,0)


        def terconditionDefine(self):
            return self.getTypedRuleContext(PDDLGrammarParser.TerconditionDefineContext,0)


        def constraintDefine(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ConstraintDefineContext,0)


        def actionDefine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.ActionDefineContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.ActionDefineContext,i)


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_domain

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomain" ):
                return visitor.visitDomain(self)
            else:
                return visitor.visitChildren(self)




    def domain(self):

        localctx = PDDLGrammarParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(PDDLGrammarParser.LB)
            self.state = 61
            self.match(PDDLGrammarParser.DEFINE)
            self.state = 62
            self.match(PDDLGrammarParser.LB)
            self.state = 63
            self.match(PDDLGrammarParser.DOMAIN)
            self.state = 64
            self.match(PDDLGrammarParser.NAME)
            self.state = 65
            self.match(PDDLGrammarParser.RB)
            self.state = 66
            self.objectDefine()
            self.state = 67
            self.terconditionDefine()
            self.state = 68
            self.constraintDefine()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PDDLGrammarParser.LB:
                self.state = 69
                self.actionDefine()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectDefineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def COLON(self):
            return self.getToken(PDDLGrammarParser.COLON, 0)

        def OBJS(self):
            return self.getToken(PDDLGrammarParser.OBJS, 0)

        def listVariable(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ListVariableContext,0)


        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_objectDefine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectDefine" ):
                return visitor.visitObjectDefine(self)
            else:
                return visitor.visitChildren(self)




    def objectDefine(self):

        localctx = PDDLGrammarParser.ObjectDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_objectDefine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(PDDLGrammarParser.LB)
            self.state = 78
            self.match(PDDLGrammarParser.COLON)
            self.state = 79
            self.match(PDDLGrammarParser.OBJS)
            self.state = 80
            self.listVariable()
            self.state = 81
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerconditionDefineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def COLON(self):
            return self.getToken(PDDLGrammarParser.COLON, 0)

        def TERCONDITION(self):
            return self.getToken(PDDLGrammarParser.TERCONDITION, 0)

        def emptyOrPreGD(self):
            return self.getTypedRuleContext(PDDLGrammarParser.EmptyOrPreGDContext,0)


        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_terconditionDefine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerconditionDefine" ):
                return visitor.visitTerconditionDefine(self)
            else:
                return visitor.visitChildren(self)




    def terconditionDefine(self):

        localctx = PDDLGrammarParser.TerconditionDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_terconditionDefine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(PDDLGrammarParser.LB)
            self.state = 84
            self.match(PDDLGrammarParser.COLON)
            self.state = 85
            self.match(PDDLGrammarParser.TERCONDITION)
            self.state = 86
            self.emptyOrPreGD()
            self.state = 87
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintDefineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def COLON(self):
            return self.getToken(PDDLGrammarParser.COLON, 0)

        def CONSTRAINT(self):
            return self.getToken(PDDLGrammarParser.CONSTRAINT, 0)

        def emptyOrPreGD(self):
            return self.getTypedRuleContext(PDDLGrammarParser.EmptyOrPreGDContext,0)


        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_constraintDefine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraintDefine" ):
                return visitor.visitConstraintDefine(self)
            else:
                return visitor.visitChildren(self)




    def constraintDefine(self):

        localctx = PDDLGrammarParser.ConstraintDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constraintDefine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(PDDLGrammarParser.LB)
            self.state = 90
            self.match(PDDLGrammarParser.COLON)
            self.state = 91
            self.match(PDDLGrammarParser.CONSTRAINT)
            self.state = 92
            self.emptyOrPreGD()
            self.state = 93
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PDDLGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_predicate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = PDDLGrammarParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(PDDLGrammarParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT(self):
            return self.getToken(PDDLGrammarParser.OBJECT, 0)

        def AGENT(self):
            return self.getToken(PDDLGrammarParser.AGENT, 0)

        def NAME(self):
            return self.getToken(PDDLGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = PDDLGrammarParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PDDLGrammarParser.OBJECT) | (1 << PDDLGrammarParser.AGENT) | (1 << PDDLGrammarParser.NAME))) != 0)):
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


    class ActionDefineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.LB)
            else:
                return self.getToken(PDDLGrammarParser.LB, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.COLON)
            else:
                return self.getToken(PDDLGrammarParser.COLON, i)

        def ACTION(self):
            return self.getToken(PDDLGrammarParser.ACTION, 0)

        def actionSymbol(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ActionSymbolContext,0)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.RB)
            else:
                return self.getToken(PDDLGrammarParser.RB, i)

        def PARAMETER(self):
            return self.getToken(PDDLGrammarParser.PARAMETER, 0)

        def listVariable(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ListVariableContext,0)


        def PRECONDITION(self):
            return self.getToken(PDDLGrammarParser.PRECONDITION, 0)

        def emptyOrPreGD(self):
            return self.getTypedRuleContext(PDDLGrammarParser.EmptyOrPreGDContext,0)


        def EFFECT(self):
            return self.getToken(PDDLGrammarParser.EFFECT, 0)

        def emptyOrEffect(self):
            return self.getTypedRuleContext(PDDLGrammarParser.EmptyOrEffectContext,0)


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_actionDefine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionDefine" ):
                return visitor.visitActionDefine(self)
            else:
                return visitor.visitChildren(self)




    def actionDefine(self):

        localctx = PDDLGrammarParser.ActionDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_actionDefine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(PDDLGrammarParser.LB)
            self.state = 100
            self.match(PDDLGrammarParser.COLON)
            self.state = 101
            self.match(PDDLGrammarParser.ACTION)
            self.state = 102
            self.actionSymbol()
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 103
                self.match(PDDLGrammarParser.COLON)
                self.state = 104
                self.match(PDDLGrammarParser.PARAMETER)
                self.state = 105
                self.match(PDDLGrammarParser.LB)
                self.state = 106
                self.listVariable()
                self.state = 107
                self.match(PDDLGrammarParser.RB)


            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(PDDLGrammarParser.COLON)
                self.state = 112
                self.match(PDDLGrammarParser.PRECONDITION)
                self.state = 113
                self.emptyOrPreGD()


            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PDDLGrammarParser.COLON:
                self.state = 116
                self.match(PDDLGrammarParser.COLON)
                self.state = 117
                self.match(PDDLGrammarParser.EFFECT)
                self.state = 118
                self.emptyOrEffect()


            self.state = 121
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionSymbolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PDDLGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_actionSymbol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionSymbol" ):
                return visitor.visitActionSymbol(self)
            else:
                return visitor.visitChildren(self)




    def actionSymbol(self):

        localctx = PDDLGrammarParser.ActionSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_actionSymbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(PDDLGrammarParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL(self):
            return self.getToken(PDDLGrammarParser.NORMAL, 0)

        def MISERE(self):
            return self.getToken(PDDLGrammarParser.MISERE, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_typeName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeName" ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = PDDLGrammarParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not(_la==PDDLGrammarParser.NORMAL or _la==PDDLGrammarParser.MISERE):
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


    class EmptyOrPreGDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_emptyOrPreGD

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PreGDBracketContext(EmptyOrPreGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.EmptyOrPreGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreGDBracket" ):
                return visitor.visitPreGDBracket(self)
            else:
                return visitor.visitChildren(self)


    class IsGdContext(EmptyOrPreGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.EmptyOrPreGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def gd(self):
            return self.getTypedRuleContext(PDDLGrammarParser.GdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsGd" ):
                return visitor.visitIsGd(self)
            else:
                return visitor.visitChildren(self)



    def emptyOrPreGD(self):

        localctx = PDDLGrammarParser.EmptyOrPreGDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_emptyOrPreGD)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = PDDLGrammarParser.IsGdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.gd()
                pass

            elif la_ == 2:
                localctx = PDDLGrammarParser.PreGDBracketContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(PDDLGrammarParser.LB)
                self.state = 129
                self.match(PDDLGrammarParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyOrEffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_emptyOrEffect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IsEffectContext(EmptyOrEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.EmptyOrEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def effect(self):
            return self.getTypedRuleContext(PDDLGrammarParser.EffectContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsEffect" ):
                return visitor.visitIsEffect(self)
            else:
                return visitor.visitChildren(self)


    class EffectBracketContext(EmptyOrEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.EmptyOrEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEffectBracket" ):
                return visitor.visitEffectBracket(self)
            else:
                return visitor.visitChildren(self)



    def emptyOrEffect(self):

        localctx = PDDLGrammarParser.EmptyOrEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_emptyOrEffect)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = PDDLGrammarParser.IsEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.effect()
                pass

            elif la_ == 2:
                localctx = PDDLGrammarParser.EffectBracketContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(PDDLGrammarParser.LB)
                self.state = 134
                self.match(PDDLGrammarParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.NAME)
            else:
                return self.getToken(PDDLGrammarParser.NAME, i)

        def MINUS(self):
            return self.getToken(PDDLGrammarParser.MINUS, 0)

        def types(self):
            return self.getTypedRuleContext(PDDLGrammarParser.TypesContext,0)


        def listName(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ListNameContext,0)


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_listName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListName" ):
                return visitor.visitListName(self)
            else:
                return visitor.visitChildren(self)




    def listName(self):

        localctx = PDDLGrammarParser.ListNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listName)
        self._la = 0 # Token type
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PDDLGrammarParser.NAME:
                    self.state = 137
                    self.match(PDDLGrammarParser.NAME)
                    self.state = 142
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 143
                    self.match(PDDLGrammarParser.NAME)
                    self.state = 146 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==PDDLGrammarParser.NAME):
                        break

                self.state = 148
                self.match(PDDLGrammarParser.MINUS)
                self.state = 149
                self.types()
                self.state = 150
                self.listName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListVariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.VAR)
            else:
                return self.getToken(PDDLGrammarParser.VAR, i)

        def MINUS(self):
            return self.getToken(PDDLGrammarParser.MINUS, 0)

        def types(self):
            return self.getTypedRuleContext(PDDLGrammarParser.TypesContext,0)


        def listVariable(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ListVariableContext,0)


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_listVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListVariable" ):
                return visitor.visitListVariable(self)
            else:
                return visitor.visitChildren(self)




    def listVariable(self):

        localctx = PDDLGrammarParser.ListVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listVariable)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PDDLGrammarParser.VAR:
                    self.state = 154
                    self.match(PDDLGrammarParser.VAR)
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 160
                    self.match(PDDLGrammarParser.VAR)
                    self.state = 163 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==PDDLGrammarParser.VAR):
                        break

                self.state = 165
                self.match(PDDLGrammarParser.MINUS)
                self.state = 166
                self.types()
                self.state = 167
                self.listVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OneofDefineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONEOF(self):
            return self.getToken(PDDLGrammarParser.ONEOF, 0)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.VAR)
            else:
                return self.getToken(PDDLGrammarParser.VAR, i)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_oneofDefine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOneofDefine" ):
                return visitor.visitOneofDefine(self)
            else:
                return visitor.visitChildren(self)




    def oneofDefine(self):

        localctx = PDDLGrammarParser.OneofDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_oneofDefine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(PDDLGrammarParser.ONEOF)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.match(PDDLGrammarParser.VAR)
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PDDLGrammarParser.VAR):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_gd

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NotContext(GdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.GdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def NOT(self):
            return self.getToken(PDDLGrammarParser.NOT, 0)
        def gd(self):
            return self.getTypedRuleContext(PDDLGrammarParser.GdContext,0)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(GdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.GdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def OR(self):
            return self.getToken(PDDLGrammarParser.OR, 0)
        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)
        def gd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.GdContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.GdContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class ImplyContext(GdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.GdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def IMPLIES(self):
            return self.getToken(PDDLGrammarParser.IMPLIES, 0)
        def gd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.GdContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.GdContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImply" ):
                return visitor.visitImply(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(GdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.GdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def AND(self):
            return self.getToken(PDDLGrammarParser.AND, 0)
        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)
        def gd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.GdContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.GdContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class ForallContext(GdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.GdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.LB)
            else:
                return self.getToken(PDDLGrammarParser.LB, i)
        def FORALL(self):
            return self.getToken(PDDLGrammarParser.FORALL, 0)
        def listVariable(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ListVariableContext,0)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.RB)
            else:
                return self.getToken(PDDLGrammarParser.RB, i)
        def gd(self):
            return self.getTypedRuleContext(PDDLGrammarParser.GdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForall" ):
                return visitor.visitForall(self)
            else:
                return visitor.visitChildren(self)


    class ExistsContext(GdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.GdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.LB)
            else:
                return self.getToken(PDDLGrammarParser.LB, i)
        def EXISTS(self):
            return self.getToken(PDDLGrammarParser.EXISTS, 0)
        def listVariable(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ListVariableContext,0)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.RB)
            else:
                return self.getToken(PDDLGrammarParser.RB, i)
        def gd(self):
            return self.getTypedRuleContext(PDDLGrammarParser.GdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExists" ):
                return visitor.visitExists(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(GdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.GdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termAtomForm(self):
            return self.getTypedRuleContext(PDDLGrammarParser.TermAtomFormContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def gd(self):

        localctx = PDDLGrammarParser.GdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_gd)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = PDDLGrammarParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.termAtomForm()
                pass

            elif la_ == 2:
                localctx = PDDLGrammarParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(PDDLGrammarParser.LB)
                self.state = 179
                self.match(PDDLGrammarParser.AND)
                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 180
                    self.gd()
                    self.state = 183 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==PDDLGrammarParser.LB):
                        break

                self.state = 185
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 3:
                localctx = PDDLGrammarParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(PDDLGrammarParser.LB)
                self.state = 188
                self.match(PDDLGrammarParser.OR)
                self.state = 190 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 189
                    self.gd()
                    self.state = 192 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==PDDLGrammarParser.LB):
                        break

                self.state = 194
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 4:
                localctx = PDDLGrammarParser.NotContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.match(PDDLGrammarParser.LB)
                self.state = 197
                self.match(PDDLGrammarParser.NOT)
                self.state = 198
                self.gd()
                self.state = 199
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 5:
                localctx = PDDLGrammarParser.ImplyContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 201
                self.match(PDDLGrammarParser.LB)
                self.state = 202
                self.match(PDDLGrammarParser.IMPLIES)
                self.state = 203
                self.gd()
                self.state = 204
                self.gd()
                self.state = 205
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 6:
                localctx = PDDLGrammarParser.ExistsContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.match(PDDLGrammarParser.LB)
                self.state = 208
                self.match(PDDLGrammarParser.EXISTS)
                self.state = 209
                self.match(PDDLGrammarParser.LB)
                self.state = 210
                self.listVariable()
                self.state = 211
                self.match(PDDLGrammarParser.RB)
                self.state = 212
                self.gd()
                self.state = 213
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 7:
                localctx = PDDLGrammarParser.ForallContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.match(PDDLGrammarParser.LB)
                self.state = 216
                self.match(PDDLGrammarParser.FORALL)
                self.state = 217
                self.match(PDDLGrammarParser.LB)
                self.state = 218
                self.listVariable()
                self.state = 219
                self.match(PDDLGrammarParser.RB)
                self.state = 220
                self.gd()
                self.state = 221
                self.match(PDDLGrammarParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermAtomFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_termAtomForm

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqualContext(TermAtomFormContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermAtomFormContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def EQ(self):
            return self.getToken(PDDLGrammarParser.EQ, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class NEqualContext(TermAtomFormContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermAtomFormContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def NEQ(self):
            return self.getToken(PDDLGrammarParser.NEQ, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNEqual" ):
                return visitor.visitNEqual(self)
            else:
                return visitor.visitChildren(self)


    class LessThanEqualContext(TermAtomFormContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermAtomFormContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def LEQ(self):
            return self.getToken(PDDLGrammarParser.LEQ, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThanEqual" ):
                return visitor.visitLessThanEqual(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanEqualContext(TermAtomFormContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermAtomFormContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def GEQ(self):
            return self.getToken(PDDLGrammarParser.GEQ, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThanEqual" ):
                return visitor.visitGreaterThanEqual(self)
            else:
                return visitor.visitChildren(self)


    class PredicateAContext(TermAtomFormContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermAtomFormContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def predicate(self):
            return self.getTypedRuleContext(PDDLGrammarParser.PredicateContext,0)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicateA" ):
                return visitor.visitPredicateA(self)
            else:
                return visitor.visitChildren(self)


    class LessThanContext(TermAtomFormContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermAtomFormContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def LT(self):
            return self.getToken(PDDLGrammarParser.LT, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThan" ):
                return visitor.visitLessThan(self)
            else:
                return visitor.visitChildren(self)


    class ModTestContext(TermAtomFormContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermAtomFormContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def MODTEST(self):
            return self.getToken(PDDLGrammarParser.MODTEST, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModTest" ):
                return visitor.visitModTest(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanContext(TermAtomFormContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermAtomFormContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def GT(self):
            return self.getToken(PDDLGrammarParser.GT, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThan" ):
                return visitor.visitGreaterThan(self)
            else:
                return visitor.visitChildren(self)



    def termAtomForm(self):

        localctx = PDDLGrammarParser.TermAtomFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_termAtomForm)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = PDDLGrammarParser.PredicateAContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(PDDLGrammarParser.LB)
                self.state = 226
                self.predicate()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & ((1 << (PDDLGrammarParser.LB - 34)) | (1 << (PDDLGrammarParser.NAME - 34)) | (1 << (PDDLGrammarParser.INTEGER - 34)) | (1 << (PDDLGrammarParser.VAR - 34)))) != 0):
                    self.state = 227
                    self.term()
                    self.state = 232
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 233
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 2:
                localctx = PDDLGrammarParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(PDDLGrammarParser.LB)
                self.state = 236
                self.match(PDDLGrammarParser.EQ)
                self.state = 237
                self.term()
                self.state = 238
                self.term()
                self.state = 239
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 3:
                localctx = PDDLGrammarParser.NEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.match(PDDLGrammarParser.LB)
                self.state = 242
                self.match(PDDLGrammarParser.NEQ)
                self.state = 243
                self.term()
                self.state = 244
                self.term()
                self.state = 245
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 4:
                localctx = PDDLGrammarParser.LessThanContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.match(PDDLGrammarParser.LB)
                self.state = 248
                self.match(PDDLGrammarParser.LT)
                self.state = 249
                self.term()
                self.state = 250
                self.term()
                self.state = 251
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 5:
                localctx = PDDLGrammarParser.LessThanEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.match(PDDLGrammarParser.LB)
                self.state = 254
                self.match(PDDLGrammarParser.LEQ)
                self.state = 255
                self.term()
                self.state = 256
                self.term()
                self.state = 257
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 6:
                localctx = PDDLGrammarParser.GreaterThanContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 259
                self.match(PDDLGrammarParser.LB)
                self.state = 260
                self.match(PDDLGrammarParser.GT)
                self.state = 261
                self.term()
                self.state = 262
                self.term()
                self.state = 263
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 7:
                localctx = PDDLGrammarParser.GreaterThanEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 265
                self.match(PDDLGrammarParser.LB)
                self.state = 266
                self.match(PDDLGrammarParser.GEQ)
                self.state = 267
                self.term()
                self.state = 268
                self.term()
                self.state = 269
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 8:
                localctx = PDDLGrammarParser.ModTestContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 271
                self.match(PDDLGrammarParser.LB)
                self.state = 272
                self.match(PDDLGrammarParser.MODTEST)
                self.state = 273
                self.term()
                self.state = 274
                self.term()
                self.state = 275
                self.term()
                self.state = 276
                self.match(PDDLGrammarParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termAtomForm(self):
            return self.getTypedRuleContext(PDDLGrammarParser.TermAtomFormContext,0)


        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def NOT(self):
            return self.getToken(PDDLGrammarParser.NOT, 0)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_termLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermLiteral" ):
                return visitor.visitTermLiteral(self)
            else:
                return visitor.visitChildren(self)




    def termLiteral(self):

        localctx = PDDLGrammarParser.TermLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_termLiteral)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.termAtomForm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(PDDLGrammarParser.LB)
                self.state = 282
                self.match(PDDLGrammarParser.NOT)
                self.state = 283
                self.termAtomForm()
                self.state = 284
                self.match(PDDLGrammarParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PDDLGrammarParser.NAME, 0)

        def INTEGER(self):
            return self.getToken(PDDLGrammarParser.INTEGER, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_constTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstTerm" ):
                return visitor.visitConstTerm(self)
            else:
                return visitor.visitChildren(self)




    def constTerm(self):

        localctx = PDDLGrammarParser.ConstTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            _la = self._input.LA(1)
            if not(_la==PDDLGrammarParser.NAME or _la==PDDLGrammarParser.INTEGER):
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


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ModTermTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def MOD(self):
            return self.getToken(PDDLGrammarParser.MOD, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModTermTerm" ):
                return visitor.visitModTermTerm(self)
            else:
                return visitor.visitChildren(self)


    class MinusTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def MINUS(self):
            return self.getToken(PDDLGrammarParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(PDDLGrammarParser.TermContext,0)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusTerm" ):
                return visitor.visitMinusTerm(self)
            else:
                return visitor.visitChildren(self)


    class TermMinusTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def MINUS(self):
            return self.getToken(PDDLGrammarParser.MINUS, 0)
        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermMinusTerm" ):
                return visitor.visitTermMinusTerm(self)
            else:
                return visitor.visitChildren(self)


    class TermModTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def MOD(self):
            return self.getToken(PDDLGrammarParser.MOD, 0)
        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermModTerm" ):
                return visitor.visitTermModTerm(self)
            else:
                return visitor.visitChildren(self)


    class BracketTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def term(self):
            return self.getTypedRuleContext(PDDLGrammarParser.TermContext,0)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracketTerm" ):
                return visitor.visitBracketTerm(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(PDDLGrammarParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class MultTermTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def MULT(self):
            return self.getToken(PDDLGrammarParser.MULT, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultTermTerm" ):
                return visitor.visitMultTermTerm(self)
            else:
                return visitor.visitChildren(self)


    class NameContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(PDDLGrammarParser.NAME, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)


    class PlusTermTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def PLUS(self):
            return self.getToken(PDDLGrammarParser.PLUS, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusTermTerm" ):
                return visitor.visitPlusTermTerm(self)
            else:
                return visitor.visitChildren(self)


    class MinusTermTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def MINUS(self):
            return self.getToken(PDDLGrammarParser.MINUS, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.TermContext,i)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusTermTerm" ):
                return visitor.visitMinusTermTerm(self)
            else:
                return visitor.visitChildren(self)


    class IntegerContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(PDDLGrammarParser.INTEGER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = PDDLGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = PDDLGrammarParser.NameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(PDDLGrammarParser.NAME)
                pass

            elif la_ == 2:
                localctx = PDDLGrammarParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(PDDLGrammarParser.VAR)
                pass

            elif la_ == 3:
                localctx = PDDLGrammarParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.match(PDDLGrammarParser.INTEGER)
                pass

            elif la_ == 4:
                localctx = PDDLGrammarParser.BracketTermContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 293
                self.match(PDDLGrammarParser.LB)
                self.state = 294
                self.term()
                self.state = 295
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 5:
                localctx = PDDLGrammarParser.MinusTermContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 297
                self.match(PDDLGrammarParser.LB)
                self.state = 298
                self.match(PDDLGrammarParser.MINUS)
                self.state = 299
                self.term()
                self.state = 300
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 6:
                localctx = PDDLGrammarParser.MinusTermTermContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 302
                self.match(PDDLGrammarParser.LB)
                self.state = 303
                self.match(PDDLGrammarParser.MINUS)
                self.state = 304
                self.term()
                self.state = 305
                self.term()
                self.state = 306
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 7:
                localctx = PDDLGrammarParser.ModTermTermContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 308
                self.match(PDDLGrammarParser.LB)
                self.state = 309
                self.match(PDDLGrammarParser.MOD)
                self.state = 310
                self.term()
                self.state = 311
                self.term()
                self.state = 312
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 8:
                localctx = PDDLGrammarParser.TermMinusTermContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 314
                self.match(PDDLGrammarParser.LB)
                self.state = 315
                self.term()
                self.state = 316
                self.match(PDDLGrammarParser.MINUS)
                self.state = 317
                self.term()
                self.state = 318
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 9:
                localctx = PDDLGrammarParser.TermModTermContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 320
                self.match(PDDLGrammarParser.LB)
                self.state = 321
                self.term()
                self.state = 322
                self.match(PDDLGrammarParser.MOD)
                self.state = 323
                self.term()
                self.state = 324
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 10:
                localctx = PDDLGrammarParser.PlusTermTermContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 326
                self.match(PDDLGrammarParser.LB)
                self.state = 327
                self.match(PDDLGrammarParser.PLUS)
                self.state = 328
                self.term()
                self.state = 329
                self.term()
                self.state = 330
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 11:
                localctx = PDDLGrammarParser.MultTermTermContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 332
                self.match(PDDLGrammarParser.LB)
                self.state = 333
                self.match(PDDLGrammarParser.MULT)
                self.state = 334
                self.term()
                self.state = 335
                self.term()
                self.state = 336
                self.match(PDDLGrammarParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_effect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AndCEffectContext(EffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.EffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def AND(self):
            return self.getToken(PDDLGrammarParser.AND, 0)
        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)
        def cEffect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.CEffectContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.CEffectContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndCEffect" ):
                return visitor.visitAndCEffect(self)
            else:
                return visitor.visitChildren(self)


    class CeffectContext(EffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.EffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cEffect(self):
            return self.getTypedRuleContext(PDDLGrammarParser.CEffectContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCeffect" ):
                return visitor.visitCeffect(self)
            else:
                return visitor.visitChildren(self)



    def effect(self):

        localctx = PDDLGrammarParser.EffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = PDDLGrammarParser.AndCEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(PDDLGrammarParser.LB)
                self.state = 341
                self.match(PDDLGrammarParser.AND)
                self.state = 343 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 342
                    self.cEffect()
                    self.state = 345 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==PDDLGrammarParser.LB):
                        break

                self.state = 347
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 2:
                localctx = PDDLGrammarParser.CeffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.cEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CEffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_cEffect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhenCondEffectContext(CEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.CEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def WHEN(self):
            return self.getToken(PDDLGrammarParser.WHEN, 0)
        def gd(self):
            return self.getTypedRuleContext(PDDLGrammarParser.GdContext,0)

        def condEffect(self):
            return self.getTypedRuleContext(PDDLGrammarParser.CondEffectContext,0)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhenCondEffect" ):
                return visitor.visitWhenCondEffect(self)
            else:
                return visitor.visitChildren(self)


    class CEffectPEffectContext(CEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.CEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pEffect(self):
            return self.getTypedRuleContext(PDDLGrammarParser.PEffectContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCEffectPEffect" ):
                return visitor.visitCEffectPEffect(self)
            else:
                return visitor.visitChildren(self)



    def cEffect(self):

        localctx = PDDLGrammarParser.CEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_cEffect)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = PDDLGrammarParser.WhenCondEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(PDDLGrammarParser.LB)
                self.state = 353
                self.match(PDDLGrammarParser.WHEN)
                self.state = 354
                self.gd()
                self.state = 355
                self.condEffect()
                self.state = 356
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 2:
                localctx = PDDLGrammarParser.CEffectPEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.pEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondEffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_condEffect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AndPEffectContext(CondEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.CondEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)
        def AND(self):
            return self.getToken(PDDLGrammarParser.AND, 0)
        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)
        def pEffect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.PEffectContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.PEffectContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndPEffect" ):
                return visitor.visitAndPEffect(self)
            else:
                return visitor.visitChildren(self)


    class CondEffectPEffectContext(CondEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.CondEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pEffect(self):
            return self.getTypedRuleContext(PDDLGrammarParser.PEffectContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondEffectPEffect" ):
                return visitor.visitCondEffectPEffect(self)
            else:
                return visitor.visitChildren(self)



    def condEffect(self):

        localctx = PDDLGrammarParser.CondEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_condEffect)
        self._la = 0 # Token type
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                localctx = PDDLGrammarParser.AndPEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(PDDLGrammarParser.LB)
                self.state = 362
                self.match(PDDLGrammarParser.AND)
                self.state = 364 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 363
                    self.pEffect()
                    self.state = 366 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==PDDLGrammarParser.LB):
                        break

                self.state = 368
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 2:
                localctx = PDDLGrammarParser.CondEffectPEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.pEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PEffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def assignop(self):
            return self.getTypedRuleContext(PDDLGrammarParser.AssignopContext,0)


        def VAR(self):
            return self.getToken(PDDLGrammarParser.VAR, 0)

        def term(self):
            return self.getTypedRuleContext(PDDLGrammarParser.TermContext,0)


        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_pEffect

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPEffect" ):
                return visitor.visitPEffect(self)
            else:
                return visitor.visitChildren(self)




    def pEffect(self):

        localctx = PDDLGrammarParser.PEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_pEffect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(PDDLGrammarParser.LB)
            self.state = 374
            self.assignop()
            self.state = 375
            self.match(PDDLGrammarParser.VAR)
            self.state = 376
            self.term()
            self.state = 377
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_assignop

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DecContext(AssignopContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.AssignopContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEC(self):
            return self.getToken(PDDLGrammarParser.DEC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec" ):
                return visitor.visitDec(self)
            else:
                return visitor.visitChildren(self)


    class IncContext(AssignopContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.AssignopContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INC(self):
            return self.getToken(PDDLGrammarParser.INC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInc" ):
                return visitor.visitInc(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(AssignopContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PDDLGrammarParser.AssignopContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(PDDLGrammarParser.ASSIGN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def assignop(self):

        localctx = PDDLGrammarParser.AssignopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignop)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PDDLGrammarParser.INC]:
                localctx = PDDLGrammarParser.IncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(PDDLGrammarParser.INC)
                pass
            elif token in [PDDLGrammarParser.DEC]:
                localctx = PDDLGrammarParser.DecContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(PDDLGrammarParser.DEC)
                pass
            elif token in [PDDLGrammarParser.ASSIGN]:
                localctx = PDDLGrammarParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(PDDLGrammarParser.ASSIGN)
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


    class ProblemNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PDDLGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_problemName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProblemName" ):
                return visitor.visitProblemName(self)
            else:
                return visitor.visitChildren(self)




    def problemName(self):

        localctx = PDDLGrammarParser.ProblemNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_problemName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(PDDLGrammarParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PDDLGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_domainName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomainName" ):
                return visitor.visitDomainName(self)
            else:
                return visitor.visitChildren(self)




    def domainName(self):

        localctx = PDDLGrammarParser.DomainNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_domainName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(PDDLGrammarParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentDefineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def COLON(self):
            return self.getToken(PDDLGrammarParser.COLON, 0)

        def AGENT(self):
            return self.getToken(PDDLGrammarParser.AGENT, 0)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(PDDLGrammarParser.NAME)
            else:
                return self.getToken(PDDLGrammarParser.NAME, i)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_agentDefine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentDefine" ):
                return visitor.visitAgentDefine(self)
            else:
                return visitor.visitChildren(self)




    def agentDefine(self):

        localctx = PDDLGrammarParser.AgentDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_agentDefine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(PDDLGrammarParser.LB)
            self.state = 389
            self.match(PDDLGrammarParser.COLON)
            self.state = 390
            self.match(PDDLGrammarParser.AGENT)
            self.state = 392 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 391
                self.match(PDDLGrammarParser.NAME)
                self.state = 394 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PDDLGrammarParser.NAME):
                    break

            self.state = 396
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def COLON(self):
            return self.getToken(PDDLGrammarParser.COLON, 0)

        def OBJS(self):
            return self.getToken(PDDLGrammarParser.OBJS, 0)

        def listName(self):
            return self.getTypedRuleContext(PDDLGrammarParser.ListNameContext,0)


        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_objectDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectDeclaration" ):
                return visitor.visitObjectDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def objectDeclaration(self):

        localctx = PDDLGrammarParser.ObjectDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_objectDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(PDDLGrammarParser.LB)
            self.state = 399
            self.match(PDDLGrammarParser.COLON)
            self.state = 400
            self.match(PDDLGrammarParser.OBJS)
            self.state = 401
            self.listName()
            self.state = 402
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def COLON(self):
            return self.getToken(PDDLGrammarParser.COLON, 0)

        def INIT(self):
            return self.getToken(PDDLGrammarParser.INIT, 0)

        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def constTermAtomForm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.ConstTermAtomFormContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.ConstTermAtomFormContext,i)


        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = PDDLGrammarParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(PDDLGrammarParser.LB)
            self.state = 405
            self.match(PDDLGrammarParser.COLON)
            self.state = 406
            self.match(PDDLGrammarParser.INIT)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PDDLGrammarParser.LB:
                self.state = 407
                self.constTermAtomForm()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 413
            self.match(PDDLGrammarParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstTermAtomFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(PDDLGrammarParser.LB, 0)

        def predicate(self):
            return self.getTypedRuleContext(PDDLGrammarParser.PredicateContext,0)


        def RB(self):
            return self.getToken(PDDLGrammarParser.RB, 0)

        def constTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PDDLGrammarParser.ConstTermContext)
            else:
                return self.getTypedRuleContext(PDDLGrammarParser.ConstTermContext,i)


        def EQ(self):
            return self.getToken(PDDLGrammarParser.EQ, 0)

        def LT(self):
            return self.getToken(PDDLGrammarParser.LT, 0)

        def LEQ(self):
            return self.getToken(PDDLGrammarParser.LEQ, 0)

        def GT(self):
            return self.getToken(PDDLGrammarParser.GT, 0)

        def GEQ(self):
            return self.getToken(PDDLGrammarParser.GEQ, 0)

        def MODTEST(self):
            return self.getToken(PDDLGrammarParser.MODTEST, 0)

        def getRuleIndex(self):
            return PDDLGrammarParser.RULE_constTermAtomForm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstTermAtomForm" ):
                return visitor.visitConstTermAtomForm(self)
            else:
                return visitor.visitChildren(self)




    def constTermAtomForm(self):

        localctx = PDDLGrammarParser.ConstTermAtomFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_constTermAtomForm)
        self._la = 0 # Token type
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(PDDLGrammarParser.LB)
                self.state = 416
                self.predicate()
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PDDLGrammarParser.NAME or _la==PDDLGrammarParser.INTEGER:
                    self.state = 417
                    self.constTerm()
                    self.state = 422
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 423
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.match(PDDLGrammarParser.LB)
                self.state = 426
                self.match(PDDLGrammarParser.EQ)
                self.state = 427
                self.constTerm()
                self.state = 428
                self.constTerm()
                self.state = 429
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.match(PDDLGrammarParser.LB)
                self.state = 432
                self.match(PDDLGrammarParser.LT)
                self.state = 433
                self.constTerm()
                self.state = 434
                self.constTerm()
                self.state = 435
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 437
                self.match(PDDLGrammarParser.LB)
                self.state = 438
                self.match(PDDLGrammarParser.LEQ)
                self.state = 439
                self.constTerm()
                self.state = 440
                self.constTerm()
                self.state = 441
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 443
                self.match(PDDLGrammarParser.LB)
                self.state = 444
                self.match(PDDLGrammarParser.GT)
                self.state = 445
                self.constTerm()
                self.state = 446
                self.constTerm()
                self.state = 447
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 449
                self.match(PDDLGrammarParser.LB)
                self.state = 450
                self.match(PDDLGrammarParser.GEQ)
                self.state = 451
                self.constTerm()
                self.state = 452
                self.constTerm()
                self.state = 453
                self.match(PDDLGrammarParser.RB)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 455
                self.match(PDDLGrammarParser.LB)
                self.state = 456
                self.match(PDDLGrammarParser.MODTEST)
                self.state = 457
                self.constTerm()
                self.state = 458
                self.constTerm()
                self.state = 459
                self.constTerm()
                self.state = 460
                self.match(PDDLGrammarParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





