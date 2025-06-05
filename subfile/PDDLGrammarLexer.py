# Generated from PDDLGrammar.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0219\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\39\39\3:\3:\3:\3:\3:\3:\3;\3;\3;")
        buf.write("\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3>\3>\3>\3>\3>\3?\3?\7?\u01f3\n?\f?\16?\u01f6\13")
        buf.write("?\3@\6@\u01f9\n@\r@\16@\u01fa\3A\3A\3B\3B\3C\3C\3C\3C")
        buf.write("\3C\3C\3C\5C\u0208\nC\3D\3D\5D\u020c\nD\3E\3E\3E\3F\3")
        buf.write("F\3G\6G\u0214\nG\rG\16G\u0215\3G\3G\2\2H\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087\2\u0089B\u008bC\u008dD\3\2\5")
        buf.write("\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2\u021e\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2")
        buf.write("\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0096\3\2\2\2\7")
        buf.write("\u009e\3\2\2\2\t\u00a5\3\2\2\2\13\u00ad\3\2\2\2\r\u00b7")
        buf.write("\3\2\2\2\17\u00bc\3\2\2\2\21\u00c7\3\2\2\2\23\u00ce\3")
        buf.write("\2\2\2\25\u00d4\3\2\2\2\27\u00db\3\2\2\2\31\u00e4\3\2")
        buf.write("\2\2\33\u00ef\3\2\2\2\35\u00fa\3\2\2\2\37\u0107\3\2\2")
        buf.write("\2!\u0114\3\2\2\2#\u011f\3\2\2\2%\u0128\3\2\2\2\'\u0134")
        buf.write("\3\2\2\2)\u0138\3\2\2\2+\u013c\3\2\2\2-\u0144\3\2\2\2")
        buf.write("/\u014b\3\2\2\2\61\u0152\3\2\2\2\63\u0159\3\2\2\2\65\u0160")
        buf.write("\3\2\2\2\67\u0169\3\2\2\29\u0172\3\2\2\2;\u0179\3\2\2")
        buf.write("\2=\u017f\3\2\2\2?\u0186\3\2\2\2A\u018e\3\2\2\2C\u0193")
        buf.write("\3\2\2\2E\u0198\3\2\2\2G\u019a\3\2\2\2I\u019c\3\2\2\2")
        buf.write("K\u019e\3\2\2\2M\u01a0\3\2\2\2O\u01a2\3\2\2\2Q\u01a4\3")
        buf.write("\2\2\2S\u01a6\3\2\2\2U\u01a8\3\2\2\2W\u01aa\3\2\2\2Y\u01ac")
        buf.write("\3\2\2\2[\u01ae\3\2\2\2]\u01b0\3\2\2\2_\u01b2\3\2\2\2")
        buf.write("a\u01b5\3\2\2\2c\u01b7\3\2\2\2e\u01ba\3\2\2\2g\u01bc\3")
        buf.write("\2\2\2i\u01bf\3\2\2\2k\u01c1\3\2\2\2m\u01c4\3\2\2\2o\u01c8")
        buf.write("\3\2\2\2q\u01cb\3\2\2\2s\u01cf\3\2\2\2u\u01d5\3\2\2\2")
        buf.write("w\u01dd\3\2\2\2y\u01e4\3\2\2\2{\u01eb\3\2\2\2}\u01f0\3")
        buf.write("\2\2\2\177\u01f8\3\2\2\2\u0081\u01fc\3\2\2\2\u0083\u01fe")
        buf.write("\3\2\2\2\u0085\u0207\3\2\2\2\u0087\u020b\3\2\2\2\u0089")
        buf.write("\u020d\3\2\2\2\u008b\u0210\3\2\2\2\u008d\u0213\3\2\2\2")
        buf.write("\u008f\u0090\7f\2\2\u0090\u0091\7q\2\2\u0091\u0092\7o")
        buf.write("\2\2\u0092\u0093\7c\2\2\u0093\u0094\7k\2\2\u0094\u0095")
        buf.write("\7p\2\2\u0095\4\3\2\2\2\u0096\u0097\7r\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\u0099\7q\2\2\u0099\u009a\7d\2\2\u009a\u009b")
        buf.write("\7n\2\2\u009b\u009c\7g\2\2\u009c\u009d\7o\2\2\u009d\6")
        buf.write("\3\2\2\2\u009e\u009f\7f\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1")
        buf.write("\7h\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7")
        buf.write("\7i\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7f\2\2\u00ac\n")
        buf.write("\3\2\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3")
        buf.write("\7c\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6")
        buf.write("\7u\2\2\u00b6\f\3\2\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9")
        buf.write("\7{\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb\7g\2\2\u00bb\16")
        buf.write("\3\2\2\2\u00bc\u00bd\7r\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7f\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7e\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7u\2\2\u00c6\20\3\2\2\2\u00c7\u00c8")
        buf.write("\7c\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7p\2\2\u00cd\22")
        buf.write("\3\2\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7x\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\24")
        buf.write("\3\2\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7x\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da")
        buf.write("\7u\2\2\u00da\26\3\2\2\2\u00db\u00dc\7r\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7f\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7i\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\30\3\2\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6")
        buf.write("\7x\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7o\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7f\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7n\2\2\u00ee\32")
        buf.write("\3\2\2\2\u00ef\u00f0\7r\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7o\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8\u00f9\7u\2\2\u00f9\34\3\2\2\2\u00fa\u00fb")
        buf.write("\7v\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe")
        buf.write("\7e\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7f\2\2\u0101\u0102\7k\2\2\u0102\u0103\7v\2\2\u0103\u0104")
        buf.write("\7k\2\2\u0104\u0105\7q\2\2\u0105\u0106\7p\2\2\u0106\36")
        buf.write("\3\2\2\2\u0107\u0108\7r\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a\u010b\7e\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d\u010e\7f\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7v\2\2\u0110\u0111\7k\2\2\u0111\u0112\7q\2\2\u0112\u0113")
        buf.write("\7p\2\2\u0113 \3\2\2\2\u0114\u0115\7e\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\u0117\7p\2\2\u0117\u0118\7u\2\2\u0118\u0119")
        buf.write("\7v\2\2\u0119\u011a\7t\2\2\u011a\u011b\7c\2\2\u011b\u011c")
        buf.write("\7k\2\2\u011c\u011d\7p\2\2\u011d\u011e\7v\2\2\u011e\"")
        buf.write("\3\2\2\2\u011f\u0120\7t\2\2\u0120\u0121\7g\2\2\u0121\u0122")
        buf.write("\7u\2\2\u0122\u0123\7r\2\2\u0123\u0124\7q\2\2\u0124\u0125")
        buf.write("\7p\2\2\u0125\u0126\7u\2\2\u0126\u0127\7g\2\2\u0127$\3")
        buf.write("\2\2\2\u0128\u0129\7q\2\2\u0129\u012a\7d\2\2\u012a\u012b")
        buf.write("\7u\2\2\u012b\u012c\7g\2\2\u012c\u012d\7t\2\2\u012d\u012e")
        buf.write("\7x\2\2\u012e\u012f\7c\2\2\u012f\u0130\7v\2\2\u0130\u0131")
        buf.write("\7k\2\2\u0131\u0132\7q\2\2\u0132\u0133\7p\2\2\u0133&\3")
        buf.write("\2\2\2\u0134\u0135\7o\2\2\u0135\u0136\7k\2\2\u0136\u0137")
        buf.write("\7p\2\2\u0137(\3\2\2\2\u0138\u0139\7o\2\2\u0139\u013a")
        buf.write("\7c\2\2\u013a\u013b\7z\2\2\u013b*\3\2\2\2\u013c\u013d")
        buf.write("\7p\2\2\u013d\u013e\7w\2\2\u013e\u013f\7o\2\2\u013f\u0140")
        buf.write("\7d\2\2\u0140\u0141\7g\2\2\u0141\u0142\7t\2\2\u0142\u0143")
        buf.write("\7u\2\2\u0143,\3\2\2\2\u0144\u0145\7p\2\2\u0145\u0146")
        buf.write("\7q\2\2\u0146\u0147\7t\2\2\u0147\u0148\7o\2\2\u0148\u0149")
        buf.write("\7c\2\2\u0149\u014a\7n\2\2\u014a.\3\2\2\2\u014b\u014c")
        buf.write("\7o\2\2\u014c\u014d\7k\2\2\u014d\u014e\7u\2\2\u014e\u014f")
        buf.write("\7g\2\2\u014f\u0150\7t\2\2\u0150\u0151\7g\2\2\u0151\60")
        buf.write("\3\2\2\2\u0152\u0153\7g\2\2\u0153\u0154\7h\2\2\u0154\u0155")
        buf.write("\7h\2\2\u0155\u0156\7g\2\2\u0156\u0157\7e\2\2\u0157\u0158")
        buf.write("\7v\2\2\u0158\62\3\2\2\2\u0159\u015a\7q\2\2\u015a\u015b")
        buf.write("\7d\2\2\u015b\u015c\7l\2\2\u015c\u015d\7g\2\2\u015d\u015e")
        buf.write("\7e\2\2\u015e\u015f\7v\2\2\u015f\64\3\2\2\2\u0160\u0161")
        buf.write("\7k\2\2\u0161\u0162\7p\2\2\u0162\u0163\7e\2\2\u0163\u0164")
        buf.write("\7t\2\2\u0164\u0165\7g\2\2\u0165\u0166\7c\2\2\u0166\u0167")
        buf.write("\7u\2\2\u0167\u0168\7g\2\2\u0168\66\3\2\2\2\u0169\u016a")
        buf.write("\7f\2\2\u016a\u016b\7g\2\2\u016b\u016c\7e\2\2\u016c\u016d")
        buf.write("\7t\2\2\u016d\u016e\7g\2\2\u016e\u016f\7c\2\2\u016f\u0170")
        buf.write("\7u\2\2\u0170\u0171\7g\2\2\u01718\3\2\2\2\u0172\u0173")
        buf.write("\7c\2\2\u0173\u0174\7u\2\2\u0174\u0175\7u\2\2\u0175\u0176")
        buf.write("\7k\2\2\u0176\u0177\7i\2\2\u0177\u0178\7p\2\2\u0178:\3")
        buf.write("\2\2\2\u0179\u017a\7c\2\2\u017a\u017b\7i\2\2\u017b\u017c")
        buf.write("\7g\2\2\u017c\u017d\7p\2\2\u017d\u017e\7v\2\2\u017e<\3")
        buf.write("\2\2\2\u017f\u0180\7g\2\2\u0180\u0181\7k\2\2\u0181\u0182")
        buf.write("\7v\2\2\u0182\u0183\7j\2\2\u0183\u0184\7g\2\2\u0184\u0185")
        buf.write("\7t\2\2\u0185>\3\2\2\2\u0186\u0187\7q\2\2\u0187\u0188")
        buf.write("\7d\2\2\u0188\u0189\7l\2\2\u0189\u018a\7g\2\2\u018a\u018b")
        buf.write("\7e\2\2\u018b\u018c\7v\2\2\u018c\u018d\7u\2\2\u018d@\3")
        buf.write("\2\2\2\u018e\u018f\7k\2\2\u018f\u0190\7p\2\2\u0190\u0191")
        buf.write("\7k\2\2\u0191\u0192\7v\2\2\u0192B\3\2\2\2\u0193\u0194")
        buf.write("\7i\2\2\u0194\u0195\7q\2\2\u0195\u0196\7c\2\2\u0196\u0197")
        buf.write("\7n\2\2\u0197D\3\2\2\2\u0198\u0199\7*\2\2\u0199F\3\2\2")
        buf.write("\2\u019a\u019b\7+\2\2\u019bH\3\2\2\2\u019c\u019d\7]\2")
        buf.write("\2\u019dJ\3\2\2\2\u019e\u019f\7_\2\2\u019fL\3\2\2\2\u01a0")
        buf.write("\u01a1\7<\2\2\u01a1N\3\2\2\2\u01a2\u01a3\7A\2\2\u01a3")
        buf.write("P\3\2\2\2\u01a4\u01a5\7\60\2\2\u01a5R\3\2\2\2\u01a6\u01a7")
        buf.write("\7a\2\2\u01a7T\3\2\2\2\u01a8\u01a9\7/\2\2\u01a9V\3\2\2")
        buf.write("\2\u01aa\u01ab\7-\2\2\u01abX\3\2\2\2\u01ac\u01ad\7,\2")
        buf.write("\2\u01adZ\3\2\2\2\u01ae\u01af\7\61\2\2\u01af\\\3\2\2\2")
        buf.write("\u01b0\u01b1\7\'\2\2\u01b1^\3\2\2\2\u01b2\u01b3\7\'\2")
        buf.write("\2\u01b3\u01b4\7?\2\2\u01b4`\3\2\2\2\u01b5\u01b6\7?\2")
        buf.write("\2\u01b6b\3\2\2\2\u01b7\u01b8\7#\2\2\u01b8\u01b9\7?\2")
        buf.write("\2\u01b9d\3\2\2\2\u01ba\u01bb\7>\2\2\u01bbf\3\2\2\2\u01bc")
        buf.write("\u01bd\7>\2\2\u01bd\u01be\7?\2\2\u01beh\3\2\2\2\u01bf")
        buf.write("\u01c0\7@\2\2\u01c0j\3\2\2\2\u01c1\u01c2\7@\2\2\u01c2")
        buf.write("\u01c3\7?\2\2\u01c3l\3\2\2\2\u01c4\u01c5\7c\2\2\u01c5")
        buf.write("\u01c6\7p\2\2\u01c6\u01c7\7f\2\2\u01c7n\3\2\2\2\u01c8")
        buf.write("\u01c9\7q\2\2\u01c9\u01ca\7t\2\2\u01cap\3\2\2\2\u01cb")
        buf.write("\u01cc\7p\2\2\u01cc\u01cd\7q\2\2\u01cd\u01ce\7v\2\2\u01ce")
        buf.write("r\3\2\2\2\u01cf\u01d0\7q\2\2\u01d0\u01d1\7p\2\2\u01d1")
        buf.write("\u01d2\7g\2\2\u01d2\u01d3\7q\2\2\u01d3\u01d4\7h\2\2\u01d4")
        buf.write("t\3\2\2\2\u01d5\u01d6\7K\2\2\u01d6\u01d7\7o\2\2\u01d7")
        buf.write("\u01d8\7r\2\2\u01d8\u01d9\7n\2\2\u01d9\u01da\7k\2\2\u01da")
        buf.write("\u01db\7g\2\2\u01db\u01dc\7u\2\2\u01dcv\3\2\2\2\u01dd")
        buf.write("\u01de\7h\2\2\u01de\u01df\7q\2\2\u01df\u01e0\7t\2\2\u01e0")
        buf.write("\u01e1\7c\2\2\u01e1\u01e2\7n\2\2\u01e2\u01e3\7n\2\2\u01e3")
        buf.write("x\3\2\2\2\u01e4\u01e5\7g\2\2\u01e5\u01e6\7z\2\2\u01e6")
        buf.write("\u01e7\7k\2\2\u01e7\u01e8\7u\2\2\u01e8\u01e9\7v\2\2\u01e9")
        buf.write("\u01ea\7u\2\2\u01eaz\3\2\2\2\u01eb\u01ec\7y\2\2\u01ec")
        buf.write("\u01ed\7j\2\2\u01ed\u01ee\7g\2\2\u01ee\u01ef\7p\2\2\u01ef")
        buf.write("|\3\2\2\2\u01f0\u01f4\5\u0081A\2\u01f1\u01f3\5\u0085C")
        buf.write("\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5~\3\2\2\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f7\u01f9\5\u0083B\2\u01f8\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2")
        buf.write("\u01fb\u0080\3\2\2\2\u01fc\u01fd\t\2\2\2\u01fd\u0082\3")
        buf.write("\2\2\2\u01fe\u01ff\t\3\2\2\u01ff\u0084\3\2\2\2\u0200\u0208")
        buf.write("\5\u0081A\2\u0201\u0208\5\u0083B\2\u0202\u0208\5U+\2\u0203")
        buf.write("\u0208\5W,\2\u0204\u0208\5]/\2\u0205\u0208\5S*\2\u0206")
        buf.write("\u0208\5Y-\2\u0207\u0200\3\2\2\2\u0207\u0201\3\2\2\2\u0207")
        buf.write("\u0202\3\2\2\2\u0207\u0203\3\2\2\2\u0207\u0204\3\2\2\2")
        buf.write("\u0207\u0205\3\2\2\2\u0207\u0206\3\2\2\2\u0208\u0086\3")
        buf.write("\2\2\2\u0209\u020c\5E#\2\u020a\u020c\5G$\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020a\3\2\2\2\u020c\u0088\3\2\2\2\u020d")
        buf.write("\u020e\5O(\2\u020e\u020f\5}?\2\u020f\u008a\3\2\2\2\u0210")
        buf.write("\u0211\5}?\2\u0211\u008c\3\2\2\2\u0212\u0214\t\4\2\2\u0213")
        buf.write("\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0215\u0216\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0218\b")
        buf.write("G\2\2\u0218\u008e\3\2\2\2\b\2\u01f4\u01fa\u0207\u020b")
        buf.write("\u0215\3\b\2\2")
        return buf.getvalue()


class PDDLGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    DOMAIN = 1
    PROBLEM = 2
    DEFINE = 3
    AGENTID = 4
    CONST = 5
    TYPE = 6
    PREDICATE = 7
    ACTION = 8
    EVENT = 9
    EVENTS = 10
    PLDEGREE = 11
    EVENTMODEL = 12
    PARAMETER = 13
    TERCONDITION = 14
    PRECONDITION = 15
    CONSTRAINT = 16
    RESPONSE = 17
    OBSERVATION = 18
    MIN = 19
    MAX = 20
    NUMS = 21
    NORMAL = 22
    MISERE = 23
    EFFECT = 24
    OBJECT = 25
    INC = 26
    DEC = 27
    ASSIGN = 28
    AGENT = 29
    EITHER = 30
    OBJS = 31
    INIT = 32
    GOAL = 33
    LB = 34
    RB = 35
    LSB = 36
    RSB = 37
    COLON = 38
    QM = 39
    POINT = 40
    UL = 41
    MINUS = 42
    PLUS = 43
    MULT = 44
    DIV = 45
    MOD = 46
    MODTEST = 47
    EQ = 48
    NEQ = 49
    LT = 50
    LEQ = 51
    GT = 52
    GEQ = 53
    AND = 54
    OR = 55
    NOT = 56
    ONEOF = 57
    IMPLIES = 58
    FORALL = 59
    EXISTS = 60
    WHEN = 61
    NAME = 62
    INTEGER = 63
    VAR = 64
    FUNSYM = 65
    WS = 66

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'domain'", "'problem'", "'define'", "'agentid'", "'constants'",
                    "'type'", "'predicates'", "'action'", "'event'", "'events'",
                    "'pldegree'", "'eventmodel'", "'parameters'", "'tercondition'",
                    "'precondition'", "'constraint'", "'response'", "'observation'",
                    "'min'", "'max'", "'numbers'", "'normal'", "'misere'", "'effect'",
                    "'object'", "'increase'", "'decrease'", "'assign'", "'agent'",
                    "'either'", "'objects'", "'init'", "'goal'", "'('", "')'", "'['",
                    "']'", "':'", "'?'", "'.'", "'_'", "'-'", "'+'", "'*'", "'/'",
                    "'%'", "'%='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='",
                    "'and'", "'or'", "'not'", "'oneof'", "'Implies'", "'forall'",
                    "'exists'", "'when'"]

    symbolicNames = ["<INVALID>",
                     "DOMAIN", "PROBLEM", "DEFINE", "AGENTID", "CONST", "TYPE", "PREDICATE",
                     "ACTION", "EVENT", "EVENTS", "PLDEGREE", "EVENTMODEL", "PARAMETER",
                     "TERCONDITION", "PRECONDITION", "CONSTRAINT", "RESPONSE", "OBSERVATION",
                     "MIN", "MAX", "NUMS", "NORMAL", "MISERE", "EFFECT", "OBJECT",
                     "INC", "DEC", "ASSIGN", "AGENT", "EITHER", "OBJS", "INIT", "GOAL",
                     "LB", "RB", "LSB", "RSB", "COLON", "QM", "POINT", "UL", "MINUS",
                     "PLUS", "MULT", "DIV", "MOD", "MODTEST", "EQ", "NEQ", "LT",
                     "LEQ", "GT", "GEQ", "AND", "OR", "NOT", "ONEOF", "IMPLIES",
                     "FORALL", "EXISTS", "WHEN", "NAME", "INTEGER", "VAR", "FUNSYM",
                     "WS"]

    ruleNames = ["DOMAIN", "PROBLEM", "DEFINE", "AGENTID", "CONST", "TYPE",
                 "PREDICATE", "ACTION", "EVENT", "EVENTS", "PLDEGREE",
                 "EVENTMODEL", "PARAMETER", "TERCONDITION", "PRECONDITION",
                 "CONSTRAINT", "RESPONSE", "OBSERVATION", "MIN", "MAX",
                 "NUMS", "NORMAL", "MISERE", "EFFECT", "OBJECT", "INC",
                 "DEC", "ASSIGN", "AGENT", "EITHER", "OBJS", "INIT", "GOAL",
                 "LB", "RB", "LSB", "RSB", "COLON", "QM", "POINT", "UL",
                 "MINUS", "PLUS", "MULT", "DIV", "MOD", "MODTEST", "EQ",
                 "NEQ", "LT", "LEQ", "GT", "GEQ", "AND", "OR", "NOT", "ONEOF",
                 "IMPLIES", "FORALL", "EXISTS", "WHEN", "NAME", "INTEGER",
                 "LETTER", "DIGIT", "CHAR", "BRACKET", "VAR", "FUNSYM",
                 "WS"]

    grammarFileName = "PDDLGrammar.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
