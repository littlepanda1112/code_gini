# Generated from PDDLGrammar.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PDDLGrammarParser import PDDLGrammarParser
else:
    from PDDLGrammarParser import PDDLGrammarParser

# This class defines a complete listener for a parse tree produced by PDDLGrammarParser.


class PDDLGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by PDDLGrammarParser#domain.
    def enterDomain(self, ctx: PDDLGrammarParser.DomainContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#domain.
    def exitDomain(self, ctx: PDDLGrammarParser.DomainContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#objectDefine.
    def enterObjectDefine(self, ctx: PDDLGrammarParser.ObjectDefineContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#objectDefine.
    def exitObjectDefine(self, ctx: PDDLGrammarParser.ObjectDefineContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#typeDefine.
    def enterTypeDefine(self, ctx: PDDLGrammarParser.TypeDefineContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#typeDefine.
    def exitTypeDefine(self, ctx: PDDLGrammarParser.TypeDefineContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#terconditionDefine.
    def enterTerconditionDefine(self, ctx: PDDLGrammarParser.TerconditionDefineContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#terconditionDefine.
    def exitTerconditionDefine(self, ctx: PDDLGrammarParser.TerconditionDefineContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#constraintDefine.
    def enterConstraintDefine(self, ctx: PDDLGrammarParser.ConstraintDefineContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#constraintDefine.
    def exitConstraintDefine(self, ctx: PDDLGrammarParser.ConstraintDefineContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#predicate.
    def enterPredicate(self, ctx: PDDLGrammarParser.PredicateContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#predicate.
    def exitPredicate(self, ctx: PDDLGrammarParser.PredicateContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#types.
    def enterTypes(self, ctx: PDDLGrammarParser.TypesContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#types.
    def exitTypes(self, ctx: PDDLGrammarParser.TypesContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#actionDefine.
    def enterActionDefine(self, ctx: PDDLGrammarParser.ActionDefineContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#actionDefine.
    def exitActionDefine(self, ctx: PDDLGrammarParser.ActionDefineContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#actionSymbol.
    def enterActionSymbol(self, ctx: PDDLGrammarParser.ActionSymbolContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#actionSymbol.
    def exitActionSymbol(self, ctx: PDDLGrammarParser.ActionSymbolContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#typeName.
    def enterTypeName(self, ctx: PDDLGrammarParser.TypeNameContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#typeName.
    def exitTypeName(self, ctx: PDDLGrammarParser.TypeNameContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#isGd.
    def enterIsGd(self, ctx: PDDLGrammarParser.IsGdContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#isGd.
    def exitIsGd(self, ctx: PDDLGrammarParser.IsGdContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#preGDBracket.
    def enterPreGDBracket(self, ctx: PDDLGrammarParser.PreGDBracketContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#preGDBracket.
    def exitPreGDBracket(self, ctx: PDDLGrammarParser.PreGDBracketContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#isEffect.
    def enterIsEffect(self, ctx: PDDLGrammarParser.IsEffectContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#isEffect.
    def exitIsEffect(self, ctx: PDDLGrammarParser.IsEffectContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#effectBracket.
    def enterEffectBracket(self, ctx: PDDLGrammarParser.EffectBracketContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#effectBracket.
    def exitEffectBracket(self, ctx: PDDLGrammarParser.EffectBracketContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#listName.
    def enterListName(self, ctx: PDDLGrammarParser.ListNameContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#listName.
    def exitListName(self, ctx: PDDLGrammarParser.ListNameContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#listVariable.
    def enterListVariable(self, ctx: PDDLGrammarParser.ListVariableContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#listVariable.
    def exitListVariable(self, ctx: PDDLGrammarParser.ListVariableContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#oneofDefine.
    def enterOneofDefine(self, ctx: PDDLGrammarParser.OneofDefineContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#oneofDefine.
    def exitOneofDefine(self, ctx: PDDLGrammarParser.OneofDefineContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#atom.
    def enterAtom(self, ctx: PDDLGrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#atom.
    def exitAtom(self, ctx: PDDLGrammarParser.AtomContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#and.
    def enterAnd(self, ctx: PDDLGrammarParser.AndContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#and.
    def exitAnd(self, ctx: PDDLGrammarParser.AndContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#or.
    def enterOr(self, ctx: PDDLGrammarParser.OrContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#or.
    def exitOr(self, ctx: PDDLGrammarParser.OrContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#not.
    def enterNot(self, ctx: PDDLGrammarParser.NotContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#not.
    def exitNot(self, ctx: PDDLGrammarParser.NotContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#imply.
    def enterImply(self, ctx: PDDLGrammarParser.ImplyContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#imply.
    def exitImply(self, ctx: PDDLGrammarParser.ImplyContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#exists.
    def enterExists(self, ctx: PDDLGrammarParser.ExistsContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#exists.
    def exitExists(self, ctx: PDDLGrammarParser.ExistsContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#forall.
    def enterForall(self, ctx: PDDLGrammarParser.ForallContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#forall.
    def exitForall(self, ctx: PDDLGrammarParser.ForallContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#predicateA.
    def enterPredicateA(self, ctx: PDDLGrammarParser.PredicateAContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#predicateA.
    def exitPredicateA(self, ctx: PDDLGrammarParser.PredicateAContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#equal.
    def enterEqual(self, ctx: PDDLGrammarParser.EqualContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#equal.
    def exitEqual(self, ctx: PDDLGrammarParser.EqualContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#nEqual.
    def enterNEqual(self, ctx: PDDLGrammarParser.NEqualContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#nEqual.
    def exitNEqual(self, ctx: PDDLGrammarParser.NEqualContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#lessThan.
    def enterLessThan(self, ctx: PDDLGrammarParser.LessThanContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#lessThan.
    def exitLessThan(self, ctx: PDDLGrammarParser.LessThanContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#lessThanEqual.
    def enterLessThanEqual(self, ctx: PDDLGrammarParser.LessThanEqualContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#lessThanEqual.
    def exitLessThanEqual(self, ctx: PDDLGrammarParser.LessThanEqualContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#greaterThan.
    def enterGreaterThan(self, ctx: PDDLGrammarParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#greaterThan.
    def exitGreaterThan(self, ctx: PDDLGrammarParser.GreaterThanContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#greaterThanEqual.
    def enterGreaterThanEqual(self, ctx: PDDLGrammarParser.GreaterThanEqualContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#greaterThanEqual.
    def exitGreaterThanEqual(self, ctx: PDDLGrammarParser.GreaterThanEqualContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#termLiteral.
    def enterTermLiteral(self, ctx: PDDLGrammarParser.TermLiteralContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#termLiteral.
    def exitTermLiteral(self, ctx: PDDLGrammarParser.TermLiteralContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#constTerm.
    def enterConstTerm(self, ctx: PDDLGrammarParser.ConstTermContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#constTerm.
    def exitConstTerm(self, ctx: PDDLGrammarParser.ConstTermContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#name.
    def enterName(self, ctx: PDDLGrammarParser.NameContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#name.
    def exitName(self, ctx: PDDLGrammarParser.NameContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#var.
    def enterVar(self, ctx: PDDLGrammarParser.VarContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#var.
    def exitVar(self, ctx: PDDLGrammarParser.VarContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#integer.
    def enterInteger(self, ctx: PDDLGrammarParser.IntegerContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#integer.
    def exitInteger(self, ctx: PDDLGrammarParser.IntegerContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#bracketTerm.
    def enterBracketTerm(self, ctx: PDDLGrammarParser.BracketTermContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#bracketTerm.
    def exitBracketTerm(self, ctx: PDDLGrammarParser.BracketTermContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#minusTerm.
    def enterMinusTerm(self, ctx: PDDLGrammarParser.MinusTermContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#minusTerm.
    def exitMinusTerm(self, ctx: PDDLGrammarParser.MinusTermContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#minusTermTerm.
    def enterMinusTermTerm(self, ctx: PDDLGrammarParser.MinusTermTermContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#minusTermTerm.
    def exitMinusTermTerm(self, ctx: PDDLGrammarParser.MinusTermTermContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#modTermTerm.
    def enterModTermTerm(self, ctx: PDDLGrammarParser.ModTermTermContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#modTermTerm.
    def exitModTermTerm(self, ctx: PDDLGrammarParser.ModTermTermContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#termMinusTerm.
    def enterTermMinusTerm(self, ctx: PDDLGrammarParser.TermMinusTermContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#termMinusTerm.
    def exitTermMinusTerm(self, ctx: PDDLGrammarParser.TermMinusTermContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#termModTerm.
    def enterTermModTerm(self, ctx: PDDLGrammarParser.TermModTermContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#termModTerm.
    def exitTermModTerm(self, ctx: PDDLGrammarParser.TermModTermContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#plusTermTerm.
    def enterPlusTermTerm(self, ctx: PDDLGrammarParser.PlusTermTermContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#plusTermTerm.
    def exitPlusTermTerm(self, ctx: PDDLGrammarParser.PlusTermTermContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#andCEffect.
    def enterAndCEffect(self, ctx: PDDLGrammarParser.AndCEffectContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#andCEffect.
    def exitAndCEffect(self, ctx: PDDLGrammarParser.AndCEffectContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#ceffect.
    def enterCeffect(self, ctx: PDDLGrammarParser.CeffectContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#ceffect.
    def exitCeffect(self, ctx: PDDLGrammarParser.CeffectContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#whenCondEffect.
    def enterWhenCondEffect(self, ctx: PDDLGrammarParser.WhenCondEffectContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#whenCondEffect.
    def exitWhenCondEffect(self, ctx: PDDLGrammarParser.WhenCondEffectContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#cEffectPEffect.
    def enterCEffectPEffect(self, ctx: PDDLGrammarParser.CEffectPEffectContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#cEffectPEffect.
    def exitCEffectPEffect(self, ctx: PDDLGrammarParser.CEffectPEffectContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#andPEffect.
    def enterAndPEffect(self, ctx: PDDLGrammarParser.AndPEffectContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#andPEffect.
    def exitAndPEffect(self, ctx: PDDLGrammarParser.AndPEffectContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#condEffectPEffect.
    def enterCondEffectPEffect(self, ctx: PDDLGrammarParser.CondEffectPEffectContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#condEffectPEffect.
    def exitCondEffectPEffect(self, ctx: PDDLGrammarParser.CondEffectPEffectContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#pEffect.
    def enterPEffect(self, ctx: PDDLGrammarParser.PEffectContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#pEffect.
    def exitPEffect(self, ctx: PDDLGrammarParser.PEffectContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#inc.
    def enterInc(self, ctx: PDDLGrammarParser.IncContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#inc.
    def exitInc(self, ctx: PDDLGrammarParser.IncContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#dec.
    def enterDec(self, ctx: PDDLGrammarParser.DecContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#dec.
    def exitDec(self, ctx: PDDLGrammarParser.DecContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#assign.
    def enterAssign(self, ctx: PDDLGrammarParser.AssignContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#assign.
    def exitAssign(self, ctx: PDDLGrammarParser.AssignContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#problemName.
    def enterProblemName(self, ctx: PDDLGrammarParser.ProblemNameContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#problemName.
    def exitProblemName(self, ctx: PDDLGrammarParser.ProblemNameContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#domainName.
    def enterDomainName(self, ctx: PDDLGrammarParser.DomainNameContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#domainName.
    def exitDomainName(self, ctx: PDDLGrammarParser.DomainNameContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#agentDefine.
    def enterAgentDefine(self, ctx: PDDLGrammarParser.AgentDefineContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#agentDefine.
    def exitAgentDefine(self, ctx: PDDLGrammarParser.AgentDefineContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#objectDeclaration.
    def enterObjectDeclaration(self, ctx: PDDLGrammarParser.ObjectDeclarationContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#objectDeclaration.
    def exitObjectDeclaration(self, ctx: PDDLGrammarParser.ObjectDeclarationContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#init.
    def enterInit(self, ctx: PDDLGrammarParser.InitContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#init.
    def exitInit(self, ctx: PDDLGrammarParser.InitContext):
        pass

    # Enter a parse tree produced by PDDLGrammarParser#constTermAtomForm.
    def enterConstTermAtomForm(self, ctx: PDDLGrammarParser.ConstTermAtomFormContext):
        pass

    # Exit a parse tree produced by PDDLGrammarParser#constTermAtomForm.
    def exitConstTermAtomForm(self, ctx: PDDLGrammarParser.ConstTermAtomFormContext):
        pass


del PDDLGrammarParser
