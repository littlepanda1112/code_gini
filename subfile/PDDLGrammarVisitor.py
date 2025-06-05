# Generated from PDDLGrammar.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PDDLGrammarParser import PDDLGrammarParser
else:
    from PDDLGrammarParser import PDDLGrammarParser

# This class defines a complete generic visitor for a parse tree produced by PDDLGrammarParser.


class PDDLGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PDDLGrammarParser#domain.
    def visitDomain(self, ctx: PDDLGrammarParser.DomainContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#objectDefine.
    def visitObjectDefine(self, ctx: PDDLGrammarParser.ObjectDefineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#terconditionDefine.
    def visitTerconditionDefine(self, ctx: PDDLGrammarParser.TerconditionDefineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#constraintDefine.
    def visitConstraintDefine(self, ctx: PDDLGrammarParser.ConstraintDefineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#predicate.
    def visitPredicate(self, ctx: PDDLGrammarParser.PredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#types.
    def visitTypes(self, ctx: PDDLGrammarParser.TypesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#actionDefine.
    def visitActionDefine(self, ctx: PDDLGrammarParser.ActionDefineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#actionSymbol.
    def visitActionSymbol(self, ctx: PDDLGrammarParser.ActionSymbolContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#typeName.
    def visitTypeName(self, ctx: PDDLGrammarParser.TypeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#isGd.
    def visitIsGd(self, ctx: PDDLGrammarParser.IsGdContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#preGDBracket.
    def visitPreGDBracket(self, ctx: PDDLGrammarParser.PreGDBracketContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#isEffect.
    def visitIsEffect(self, ctx: PDDLGrammarParser.IsEffectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#effectBracket.
    def visitEffectBracket(self, ctx: PDDLGrammarParser.EffectBracketContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#listName.
    def visitListName(self, ctx: PDDLGrammarParser.ListNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#listVariable.
    def visitListVariable(self, ctx: PDDLGrammarParser.ListVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#oneofDefine.
    def visitOneofDefine(self, ctx: PDDLGrammarParser.OneofDefineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#atom.
    def visitAtom(self, ctx: PDDLGrammarParser.AtomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#and.
    def visitAnd(self, ctx: PDDLGrammarParser.AndContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#or.
    def visitOr(self, ctx: PDDLGrammarParser.OrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#not.
    def visitNot(self, ctx: PDDLGrammarParser.NotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#imply.
    def visitImply(self, ctx: PDDLGrammarParser.ImplyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#exists.
    def visitExists(self, ctx: PDDLGrammarParser.ExistsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#forall.
    def visitForall(self, ctx: PDDLGrammarParser.ForallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#predicateA.
    def visitPredicateA(self, ctx: PDDLGrammarParser.PredicateAContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#equal.
    def visitEqual(self, ctx: PDDLGrammarParser.EqualContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#nEqual.
    def visitNEqual(self, ctx: PDDLGrammarParser.NEqualContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#lessThan.
    def visitLessThan(self, ctx: PDDLGrammarParser.LessThanContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#lessThanEqual.
    def visitLessThanEqual(self, ctx: PDDLGrammarParser.LessThanEqualContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#greaterThan.
    def visitGreaterThan(self, ctx: PDDLGrammarParser.GreaterThanContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#greaterThanEqual.
    def visitGreaterThanEqual(self, ctx: PDDLGrammarParser.GreaterThanEqualContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#modTest.
    def visitModTest(self, ctx: PDDLGrammarParser.ModTestContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#termLiteral.
    def visitTermLiteral(self, ctx: PDDLGrammarParser.TermLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#constTerm.
    def visitConstTerm(self, ctx: PDDLGrammarParser.ConstTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#name.
    def visitName(self, ctx: PDDLGrammarParser.NameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#var.
    def visitVar(self, ctx: PDDLGrammarParser.VarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#integer.
    def visitInteger(self, ctx: PDDLGrammarParser.IntegerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#bracketTerm.
    def visitBracketTerm(self, ctx: PDDLGrammarParser.BracketTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#minusTerm.
    def visitMinusTerm(self, ctx: PDDLGrammarParser.MinusTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#minusTermTerm.
    def visitMinusTermTerm(self, ctx: PDDLGrammarParser.MinusTermTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#modTermTerm.
    def visitModTermTerm(self, ctx: PDDLGrammarParser.ModTermTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#termMinusTerm.
    def visitTermMinusTerm(self, ctx: PDDLGrammarParser.TermMinusTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#termModTerm.
    def visitTermModTerm(self, ctx: PDDLGrammarParser.TermModTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#plusTermTerm.
    def visitPlusTermTerm(self, ctx: PDDLGrammarParser.PlusTermTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#multTermTerm.
    def visitMultTermTerm(self, ctx: PDDLGrammarParser.MultTermTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#andCEffect.
    def visitAndCEffect(self, ctx: PDDLGrammarParser.AndCEffectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#ceffect.
    def visitCeffect(self, ctx: PDDLGrammarParser.CeffectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#whenCondEffect.
    def visitWhenCondEffect(self, ctx: PDDLGrammarParser.WhenCondEffectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#cEffectPEffect.
    def visitCEffectPEffect(self, ctx: PDDLGrammarParser.CEffectPEffectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#andPEffect.
    def visitAndPEffect(self, ctx: PDDLGrammarParser.AndPEffectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#condEffectPEffect.
    def visitCondEffectPEffect(self, ctx: PDDLGrammarParser.CondEffectPEffectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#pEffect.
    def visitPEffect(self, ctx: PDDLGrammarParser.PEffectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#inc.
    def visitInc(self, ctx: PDDLGrammarParser.IncContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#dec.
    def visitDec(self, ctx: PDDLGrammarParser.DecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#assign.
    def visitAssign(self, ctx: PDDLGrammarParser.AssignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#problemName.
    def visitProblemName(self, ctx: PDDLGrammarParser.ProblemNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#domainName.
    def visitDomainName(self, ctx: PDDLGrammarParser.DomainNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#agentDefine.
    def visitAgentDefine(self, ctx: PDDLGrammarParser.AgentDefineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx: PDDLGrammarParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#init.
    def visitInit(self, ctx: PDDLGrammarParser.InitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PDDLGrammarParser#constTermAtomForm.
    def visitConstTermAtomForm(self, ctx: PDDLGrammarParser.ConstTermAtomFormContext):
        return self.visitChildren(ctx)


del PDDLGrammarParser
