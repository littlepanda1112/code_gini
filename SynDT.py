import threading
import eventlet
from eventlet.green import thread
import xlrd

from subfile.PDDLGrammarLexer import PDDLGrammarLexer
from subfile.PDDLGrammarParser import PDDLGrammarParser
from math import log
from z3 import *
from MyVisitor import Item, MyVisitor
from MyVisitor import game
from opera import *
from antlr4 import *
import time
from xlwt import *
from xlrd import *
from xlutils.copy import copy
from copy import deepcopy as deepcopy
from itertools import product
import sys
import os
import re
from DT import DT1
from DTEP import DTEP
from DT import DT1
from Incremental import Infer, Incrementallearn

"""================= Game Formalization Import ========================="""
pddlFile = sys.argv[1]
resultFile = sys.argv[2]
game_type = sys.argv[3]

heuristical_way = "InfoGain"
choice_minnode = "n"

choice_method = sys.argv[4]
if choice_method == "ID3":
    heuristical_way = sys.argv[5]
elif choice_method == "Incre":
    choice_minnode = sys.argv[5]

# print(sys.argv[2])

# pddlFile = r"domain\1.Sub\1.1 Take-away\Take-away-30.pddl"
# resultFile = r".\result.xls"
# game_type = "normal" #normal, misere
# heuristical_way = "Gini"  # InfoGain, Gini

# Game variable set
v1 = Int("v1")
v2 = Int("v2")
v3 = Int("v3")
v1_next = Int("v1_next")
v2_next = Int("v2_next")
v3_next = Int("v3_next")
# Action parameters
k = Int('k')
l = Int('l')
(k1, k2, k3) = Ints('k1 k2 k3')

# ptk ptk2 -- number of countexample in each round
# time_out -- Timeout interrupt
ptk = 3
ptk2 = 3
time_out1 = 1200
time_out2 = 1200

gameName = pddlFile.split('\\')[-1][:-5]
print("use method:",choice_method,"game type:",game_type)
print("#################################################################")
print("######################### Formalization #########################")
print("#################################################################")
print("  ")
print("GameName:\n\t", gameName)
oldwb = xlrd.open_workbook(resultFile, encoding_override='utf-8')
sheet1 = oldwb.sheet_by_index(0)
row = sheet1.nrows

input_stream = FileStream(pddlFile)
lexer = PDDLGrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = PDDLGrammarParser(token_stream)
tree = parser.domain()
visitor = MyVisitor()
visitor.visit(tree)

Terminal_Condition = game.tercondition
Constarint = game.constraint
varList = []
for i in game.var_list:
    varList.append(i)
actions = []

for i in game.action_list:
    one = {"action_name": i[0],
           "action_parameter": i[1],
           "precondition": i[2],
           "transition_formula": eval(
               str(i[3]).replace('v1\'', 'v1_next').replace('v2\'', 'v2_next').replace('v3\'', 'v3_next'))}
    actions.append(one)

Game = {"Terminal_Condition": Terminal_Condition,
        "varList": varList,
        "actions": actions,
        "Constraint": Constarint,
        "var_num": game.objectsCount,
        "type": game_type,
        "appeal_constants": game.constantList}

print("Var List:", varList)
varListY = eval(str(varList).replace('v3', 'v3_next').replace('v2', 'v2_next').replace('v1', 'v1_next'))
print("Var next list", varListY)

print("Appeal constant", Game['appeal_constants'])

"""=============================================================================="""

p_vocabulary = [{'Input': ['Int', 'Int'], 'Function_name': 'Equal', 'arity': 2},
                {'Input': ['Int', 'Int'], 'Function_name': 'Ge', 'arity': 2},
                {'Input': ['Int', 'Int'], 'Function_name': 'Gt', 'arity': 2},
                {'Input': ['Int', 'Int', 'Int'], 'Function_name': 'ModTest', 'arity': 3}]

t_vocabulary = [{'Input': ['Int', 'Int'], 'Function_name': 'Add', 'arity': 2},
                {'Input': ['Int', 'Int'], 'Function_name': 'Sub', 'arity': 2}, ]

FunExg = {'Add': Add, 'Sub': Sub, 'Inc': Inc, 'Dec': Dec, 'Ge': Ge, 'ITE': ITE,
          'Gt': Gt, 'OR': OR, 'AND': AND, 'NOT': NOT, 'Equal': Equal, 'Mod': Mod,
          'Unequal': Unequal, 'v1': v1, 'v1_nwxt': v1_next, 'Zero': Zero, 'One': One, 'ModTest': ModTest}


# Cache interResult of enumerate
class InterResult:
    def __init__(self, expSet, sigSet) -> None:
        self.SigSet = sigSet
        self.ExpSet = expSet


interResultPred = InterResult("", "")
interResultTerm = InterResult("", "")


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


nextTermAdd = 5
nextTermSub = 5
predAdd = 4
preSub = 4
predSize = 7

"""Enumerate atomic formulas by size"""


def enumeratePredicate(MaxSize, DTFlag):
    global interResultPred
    SigSet = []
    ExpSet = []
    SizeOneExps = []
    Items = []
    ItemsNum = []
    ItemsVar = []
    if DTFlag:
        SizeOneExps.append({'Expression': 0, 'Isnum': True, 'size': 1})
        SizeOneExps.append({'Expression': 1, 'Isnum': True, 'size': 1})
        SizeOneExps.append({'Expression': v1, 'Isnum': False, 'size': 1})
        for i in Game["appeal_constants"]:
            SizeOneExps.append({'Expression': eval(i), 'Isnum': True, 'size': 1})
        if Game["var_num"] == 2:
            SizeOneExps.append({'Expression': v2, 'Isnum': False, 'size': 1})
        elif Game["var_num"] == 3:
            SizeOneExps.append({'Expression': v2, 'Isnum': False, 'size': 1})
            SizeOneExps.append({'Expression': v3, 'Isnum': False, 'size': 1})
        for i in SizeOneExps:
            Goal1 = []
            if (i['Isnum']):
                for num in range(len(pts)):
                    Goal1.append(i['Expression'])
                if Goal1 not in SigSet:
                    SigSet.append(Goal1)
                    i['outputData'] = Goal1
                    ExpSet.append(i)
            else:
                if i['Expression'] == v1:
                    for pt in pts:
                        Goal1.append(pt[0])
                    if Goal1 not in SigSet:
                        SigSet.append(Goal1)
                        i['outputData'] = Goal1
                        ExpSet.append(i)
                if i['Expression'] == v2:
                    for pt in pts:
                        Goal1.append(pt[1])
                    if Goal1 not in SigSet:
                        SigSet.append(Goal1)
                        i['outputData'] = Goal1
                        ExpSet.append(i)
                if i['Expression'] == v3:
                    for pt in pts:
                        Goal1.append(pt[2])
                    if Goal1 not in SigSet:
                        SigSet.append(Goal1)
                        i['outputData'] = Goal1
                        ExpSet.append(i)
    li = 2
    if DTFlag == False:
        SigSet = interResultPred.SigSet
        ExpSet = interResultPred.ExpSet
        li = MaxSize
    # print("The maximum number of predicate items enumerated",MaxSize)
    while li <= MaxSize:
        if termination_sign:
            print("Time out,about to exit the program")
            sheet1.write(row, 2, "time-out-1200s")
            newwb.save(resultFile)
            sys.exit(0)
        for i in t_vocabulary:
            if i['Function_name'] == 'Add':
                if li <= predAdd:
                    for size1 in range(1, li):
                        for choose1 in ExpSet:
                            if choose1['size'] == size1 and choose1['Isnum'] == False:
                                for choose2 in ExpSet:
                                    if choose2['size'] == li - size1:
                                        term = FunExg[i['Function_name']](
                                            choose1['Expression'], choose2['Expression'])
                                        Goal = []
                                        for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                            Goal.append(
                                                FunExg[i['Function_name']](k1, h))
                                        if Goal not in SigSet:
                                            SigSet.append(Goal)
                                            i['outputData'] = Goal
                                            ExpSet.append(
                                                {'Expression': term, 'Isnum': False, 'outputData': Goal, 'size': li})
                for size1 in range(1, li):  # add(num,num)
                    for choose1 in ExpSet:
                        if choose1['size'] == size1 and choose1['Isnum'] == True:
                            for choose2 in ExpSet:
                                if choose2['size'] == li - size1 and choose2['Isnum']:
                                    term = FunExg[i['Function_name']](
                                        choose1['Expression'], choose2['Expression'])
                                    Goal = []
                                    for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                        Goal.append(
                                            FunExg[i['Function_name']](k1, h))
                                    if Goal not in SigSet:
                                        SigSet.append(Goal)
                                        i['outputData'] = Goal
                                        ExpSet.append(
                                            {'Expression': term, 'Isnum': choose1['Isnum'] and choose2['Isnum'],
                                             'outputData': Goal, 'size': li})
            elif i['Function_name'] == 'Sub':
                if li <= preSub:
                    for size1 in range(1, li):
                        for choose1 in ExpSet:
                            if choose1['size'] == size1 and choose1['Isnum'] == False:
                                for choose2 in ExpSet:
                                    if choose2['size'] == li - size1 and str(choose1['Expression']) != str(
                                            choose2['Expression']):
                                        term = FunExg[i['Function_name']](
                                            choose1['Expression'], choose2['Expression'])
                                        Goal = []
                                        for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                            Goal.append(
                                                FunExg[i['Function_name']](k1, h))
                                        if Goal not in SigSet:
                                            SigSet.append(Goal)
                                            i['outputData'] = Goal
                                            ExpSet.append(
                                                {'Expression': term, 'Isnum': False, 'outputData': Goal, 'size': li})
        li += 1
    interResultPred = InterResult(ExpSet, SigSet)
    for i in ExpSet:
        Items.append(i['Expression'])
        if i['Isnum']:
            ItemsNum.append(i)
        else:
            ItemsVar.append(i)
    # print("Items set generate atom formula:\n\t", Items)

    predGoal = []
    for i in p_vocabulary:
        if i['arity'] == 2:
            for choose1 in ItemsVar:
                for choose2 in ItemsVar:
                    if choose2 != choose1 and choose2["size"] + choose1["size"] <= predSize:
                        # if choose2["size"] <= MaxSize+1-choose1["size"]:#var1+var2 <= maxsize+1
                        tempPredicate = FunExg[i['Function_name']](
                            choose1['Expression'], choose2['Expression'])
                        if str(tempPredicate) != 'False' and str(tempPredicate) != 'True':
                            goal = []
                            for pt in pts:
                                goal.append(ptSatPred(pt, tempPredicate))
                            if goal not in predGoal:
                                predGoal.append(goal)
                                if tempPredicate not in preds:
                                    preds.append(tempPredicate)
                                    if len(preds) == pow(2, len(pts)):
                                        return
                for choose2 in ItemsNum:
                    tempPredicate = FunExg[i['Function_name']](
                        choose1['Expression'], choose2['Expression'])
                    # if choose2["size"] <= MaxSize+1-choose1["size"]: #var1+num <= maxsize + 1
                    if str(tempPredicate) != 'False' and str(tempPredicate) != 'True':
                        goal = []
                        for pt in pts:
                            goal.append(ptSatPred(pt, tempPredicate))
                        if goal not in predGoal:
                            predGoal.append(goal)
                            if tempPredicate not in preds:
                                preds.append(tempPredicate)
                                if len(preds) == pow(2, len(pts)):
                                    return
        if i['arity'] == 3:
            for choose1 in ItemsVar:
                for choose2 in ItemsNum:
                    for choose3 in ItemsNum:
                        # if choose1["size"]+choose2["size"]+choose3["size"]<=MaxSize+1
                        if choose3["Expression"] < choose2["Expression"]:
                            try:
                                tempPredicate = FunExg[i['Function_name']](
                                    choose1["Expression"], choose2["Expression"], choose3["Expression"])
                                if str(tempPredicate) != 'False' and str(tempPredicate) != 'True':
                                    goal = []
                                    for pt in pts:
                                        goal.append(ptSatPred(pt, tempPredicate))
                                    if goal not in predGoal:
                                        predGoal.append(goal)
                                        if tempPredicate not in preds:
                                            preds.append(tempPredicate)
                                            if len(preds) == pow(2, len(pts)):
                                                return
                            except ZeroDivisionError:
                                pass


"""Enumerate term """


def enumerateTerm(pt, ptGoal):
    ExpSet = []
    SigSet = []
    sizeOneExps = []
    sizeOneExps.append({'Expression': 0, 'arity': 0, 'size': 1})
    sizeOneExps.append({'Expression': 1, 'arity': 0, 'size': 1})
    sizeOneExps.append({'Expression': v1, 'arity': 1, 'size': 1})
    if Game["var_num"] == 2:
        sizeOneExps.append({'Expression': v2, 'arity': 1, 'size': 1})
    if Game["var_num"] == 3:
        sizeOneExps.append({'Expression': v2, 'arity': 1, 'size': 1})
        sizeOneExps.append({'Expression': v3, 'arity': 1, 'size': 1})
    for i in sizeOneExps:
        if i['arity'] == 0:
            term = i['Expression']
            if term not in SigSet:
                SigSet.append(term)
                i['outputData'] = term
                ExpSet.append(i)
                if term == ptGoal:
                    return term
        if i['Expression'] == v1:
            term = v1
            Goal = pt[0]
            if Goal not in SigSet:
                SigSet.append(Goal)
                i['outputData'] = Goal
                ExpSet.append(i)
                if Goal == ptGoal:
                    return term
        if i['Expression'] == v2:
            term = v2
            Goal = pt[1]
            if Goal not in SigSet:
                SigSet.append(Goal)
                i['outputData'] = Goal
                ExpSet.append(i)
                if Goal == ptGoal:
                    return term
        if i['Expression'] == v3:
            term = v3
            Goal = pt[2]
            if Goal not in SigSet:
                SigSet.append(Goal)
                i['outputData'] = Goal
                ExpSet.append(i)
                if Goal == ptGoal:
                    return term
    sizeT = 2
    while True:

        for i in t_vocabulary:
            if termination_sign:
                print("Time out,about to exit the program")
                sheet1.write(row, 2, "time-out-1200s")
                newwb.save(resultFile)
                sys.exit(0)
            for size1 in range(1, sizeT):
                for choose1 in ExpSet:
                    if choose1['size'] == size1:
                        for choose2 in ExpSet:
                            if choose2['size'] == sizeT - size1:
                                term = FunExg[i['Function_name']](choose1['Expression'],
                                                                  choose2['Expression'])
                                Goal = FunExg[i['Function_name']](choose1['outputData'],
                                                                  choose2['outputData'])
                                if Goal == ptGoal:
                                    return term
                                if Goal not in SigSet:
                                    SigSet.append(Goal)
                                    i['outputData'] = Goal
                                    ExpSet.append(
                                        {'Expression': term, 'arity': i['arity'], 'outputData': Goal, 'size': sizeT})
        sizeT += 1


def nextSizeTerm(termMaxSize, DTFlag):  # return [actNum,paraNum,paraTerm]
    # print("next size of term:",termMaxSize)
    global interResultTerm
    ExpSet = []
    SigSet = []
    if DTFlag:
        sizeOneExps = []
        sizeOneExps.append({'Expression': 0, 'Isnum': True, 'arity': 0, 'size': 1})
        sizeOneExps.append({'Expression': 1, 'Isnum': True, 'arity': 0, 'size': 1})
        sizeOneExps.append({'Expression': v1, 'Isnum': False, 'arity': 1, 'size': 1})
        if Game["var_num"] == 2:
            sizeOneExps.append({'Expression': v2, 'Isnum': False, 'arity': 1, 'size': 1})
        elif Game["var_num"] == 3:
            sizeOneExps.append({'Expression': v2, 'Isnum': False, 'size': 1})
            sizeOneExps.append({'Expression': v3, 'Isnum': False, 'size': 1})
        for i in Game["appeal_constants"]:
            sizeOneExps.append({'Expression': eval(i), 'Isnum': True, 'size': 1})
        for i in sizeOneExps:
            if i['Isnum']:
                Goal = []
                term = i['Expression']
                for num in range(len(pts)):
                    Goal.append(i['Expression'])
                if Goal not in SigSet:
                    SigSet.append(Goal)
                    i['outputData'] = Goal
                    ExpSet.append(i)
            else:
                if i['Expression'] == v1:
                    Goal = []
                    term = v1
                    for pt in pts:
                        Goal.append(pt[0])
                    if Goal not in SigSet:
                        SigSet.append(Goal)
                        i['outputData'] = Goal
                        ExpSet.append(i)
                if i['Expression'] == v2:
                    Goal = []
                    term = v2
                    for pt in pts:
                        Goal.append(pt[1])
                    if Goal not in SigSet:
                        SigSet.append(Goal)
                        i['outputData'] = Goal
                        ExpSet.append(i)
                if i['Expression'] == v3:
                    Goal = []
                    term = v3
                    for pt in pts:
                        Goal.append(pt[2])
                    if Goal not in SigSet:
                        SigSet.append(Goal)
                        i['outputData'] = Goal
                        ExpSet.append(i)
    li = 2
    if DTFlag == False:
        SigSet = interResultTerm.SigSet
        ExpSet = interResultTerm.ExpSet
        li = termMaxSize
    while li <= termMaxSize:
        for i in t_vocabulary:
            if i['Function_name'] == 'Add':
                if li <= nextTermAdd:
                    for size1 in range(1, li):
                        for choose1 in ExpSet:
                            if choose1['size'] == size1 and choose1['Isnum'] == False:
                                for choose2 in ExpSet:
                                    if choose2['size'] == li - size1:
                                        term = FunExg[i['Function_name']](
                                            choose1['Expression'], choose2['Expression'])
                                        Goal = []
                                        for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                            Goal.append(FunExg[i['Function_name']](k1, h))
                                        if Goal not in SigSet:
                                            SigSet.append(Goal)
                                            i['outputData'] = Goal
                                            ExpSet.append({'Expression': term, 'Isnum': False, 'arity': i['arity'],
                                                           'outputData': Goal, 'size': li})
                for size1 in range(1, li):
                    for choose1 in ExpSet:
                        if choose1['size'] == size1 and choose1['Isnum']:
                            for choose2 in ExpSet:
                                if choose2['size'] == li - size1 and choose2['Isnum']:
                                    term = FunExg[i['Function_name']](
                                        choose1['Expression'], choose2['Expression'])
                                    Goal = []
                                    for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                        Goal.append(FunExg[i['Function_name']](k1, h))
                                    if Goal not in SigSet:
                                        SigSet.append(Goal)
                                        i['outputData'] = Goal
                                        ExpSet.append(
                                            {'Expression': term, 'Isnum': True, 'arity': i['arity'], 'outputData': Goal,
                                             'size': li})
            elif i['Function_name'] == 'Sub':
                if li <= nextTermSub:
                    for size1 in range(1, li):
                        for choose1 in ExpSet:
                            if choose1['size'] == size1 and choose1['Isnum'] == False:
                                for choose2 in ExpSet:
                                    if choose2['size'] == li - size1:
                                        term = FunExg[i['Function_name']](
                                            choose1['Expression'], choose2['Expression'])
                                        Goal = []
                                        for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                            Goal.append(FunExg[i['Function_name']](k1, h))
                                        if Goal not in SigSet:
                                            SigSet.append(Goal)
                                            i['outputData'] = Goal
                                            ExpSet.append({'Expression': term, 'Isnum': False, 'arity': i['arity'],
                                                           'outputData': Goal, 'size': li})
        li += 1
    interResultTerm = InterResult(ExpSet, SigSet)
    for actNum in range(len(actions)):
        action = actions[actNum]
        if len(action["action_parameter"]) == 1:
            for item in ExpSet:
                term = item['Expression']
                Goal = item["outputData"]
                Term = (actNum, term)
                if Term not in cover:
                    coverTemp = []
                    for num in range(len(pts)):
                        pt = pts[num]
                        ptOutput = ptsOutput[num]
                        for output in ptOutput:
                            if output[0] == actNum and Goal[num] == output[1] and len(output) == 2:
                                coverTemp.append(pt)
                                break
                    if coverTemp != []:
                        flag = False
                        for t in cover:
                            if len(cover[t]) == len(coverTemp):
                                list1 = deepcopy(cover[t])
                                list2 = deepcopy(cover[t])
                                if list1.sort() == list2.sort():
                                    flag = True
                                    break
                        if (flag == False):
                            terms.append(Term)
                            cover[Term] = coverTemp
        if len(action["action_parameter"]) == 2:
            for item1 in ExpSet:
                term1 = item1["Expression"]
                Goal1 = item1["outputData"]
                for item2 in ExpSet:
                    term2 = item2["Expression"]
                    Goal2 = item2["outputData"]
                    Term = (actNum, term1, term2)
                    if Term not in cover:
                        coverTemp = []
                        for num in range(len(pts)):
                            pt = pts[num]
                            ptOutput = ptsOutput[num]
                            for output in ptOutput:
                                if len(output) == 3 and output[0] == actNum and Goal1[num] == output[1] and Goal2[
                                    num] == output[2]:
                                    coverTemp.append(pt)
                                    break
                        if coverTemp != []:
                            flag = False
                            for t in cover:
                                if len(cover[t]) == len(coverTemp):
                                    list1 = deepcopy(cover[t])
                                    list2 = deepcopy(cover[t])
                                    if list1.sort() == list2.sort():
                                        flag = True
                                        break
                            if (flag == False):
                                terms.append(Term)
                                cover[Term] = coverTemp

#************************************Learn DT Method **************************
def ForLabelCopy(pts, preds):
    FeatureSet = []
    FeatureSet.append(preds)
    for pt in pts:
        OnePoint = []
        Frontset = []
        for pred in preds:
            if ptSatPred(pt, pred):
                Frontset.append(1)
            else:
                Frontset.append(0)
        OnePoint.append(Frontset)
        Backset = []
        for term in terms:
            index = terms.index(term)
            if pt in cover[term]:
                Backset.append(index)
        OnePoint.append(Backset)
        FeatureSet.append(OnePoint)
    return FeatureSet

# First Method
def learn(pts, preds):
    if pts == []:
        return TreeNode(v1 == v1)
    for term in terms:
        if not [True for i in pts if i not in cover[term]]:
            # print("leaf node ：",term)
            return TreeNode(str(term))
    if preds == [] or preds == None:
        return None
    FeatureSet = ForLabelCopy(pts, preds)
    infer = Incrementallearn.increlearn(FeatureSet, len(preds), len(terms))
    choose = False
    if choice_minnode == 'y':
        choose = True
    if choice_minnode == 'n':
        choose = False
    tree, root = infer.findOptimalTree(1, choose, terms)
    if root is False:
        global DTflag
        DTflag = False
        global RedundantPts
        RedundantPts = pts
        return None
    # print("\n===========tree print===========\n")
    return root

# Second Method
def learn_sat_DT1(pts, preds):
    if pts == []:
        return TreeNode(v1 == v1)
    for term in terms:
        if not [True for i in pts if i not in cover[term]]:
            return Infer.Node(str(term))
    if preds == [] or preds == None:
        return None
    FeatureSet = ForLabelCopy(pts, preds)
    infer = DT1.learnSatDT(FeatureSet, len(preds), len(terms), terms)
    tree, root = infer.findOptimalTree(3)
    if root is False:
        global DTflag
        DTflag = False
        global RedundantPts
        RedundantPts = pts
        return None
    return root

# Third Method
def learn_sat_DTEP(pts, preds):
    if pts == []:
        return TreeNode(v1 == v1)
    for term in terms:
        if not [True for i in pts if i not in cover[term]]:
            return Infer.Node(str(term))
    if preds == [] or preds == None:
        return None
    FeatureSet = ForLabelCopy(pts, preds)
    infer = DTEP.learnSatDT(FeatureSet, len(preds), len(terms), terms)
    root = infer.findOptimalTree(3)
    if root is False:
        global DTflag
        DTflag = False
        global RedundantPts
        RedundantPts = pts
        return None
    return root
#*******************************************************************************
"""learning decision tree use ID3 algorithm"""


def learn_DT(pts, preds):
    if pts == []:
        return TreeNode(v1 == v1)
    for term in terms:
        if not [False for i in pts if i not in cover[term]]:
            # print("leaf node ：",term)
            return TreeNode(str(term))
    if preds == [] or preds == None:
        return None
    Pick_pred = chooseBestPred1(pts, preds) if heuristical_way == "InfoGain" else chooseBestPred2(pts, preds)
    print("Choose best predicate :\n\t", Pick_pred)
    if Pick_pred == False:
        global DTflag
        DTflag = False
        global RedundantPts
        RedundantPts = pts
        return None
    root = TreeNode(Pick_pred)
    ptsYes = []
    ptsNo = []
    for pt in pts:
        if ptSatPred(pt, Pick_pred):
            ptsYes.append(pt)
        else:
            ptsNo.append(pt)
    # print("Divide two part:\n\t")
    # print(ptsYes, ":", ptsNo)
    temp_preds = preds
    temp_preds.remove(Pick_pred)
    # print("Remaining predicates",temp_preds)
    root.left = learn_DT(ptsYes, temp_preds)
    root.right = learn_DT(ptsNo, temp_preds)
    # add9-14
    if root.left == None or root.left == None:
        print("None tree")
        return None
    return root


def Entropy(pts):
    if len(pts) == 0:
        return 0
    entropy = 0.0
    for term in terms:
        probability = 0.0
        for pt in pts:
            sumcount = 0
            if pt not in cover[term]:
                probability += 0
            else:
                for term1 in terms:
                    if pt in cover[term1]:
                        sumcount += 1
                probability += (1 / len(pts)) * (1 / sumcount)
        # print(term," conditional probability is", probability)
        if probability != 0:
            entropy -= probability * log(probability, 2)
        # print(term,probability)
    # print("entropy is", entropy)
    return entropy


def Gini(pts):
    if len(pts) == 0:
        return 1
    gini = 1
    for term in terms:
        probability = 0.0
        for pt in pts:
            sumcount = 0
            if pt not in cover[term]:
                probability += 0
            else:
                for term1 in terms:
                    if pt in cover[term1]:
                        sumcount += 1
                probability += (1 / len(pts)) * (1 / sumcount)
        # print(term," conditional probability is", probability)
        if probability != 0:
            gini -= probability * probability
        # print(term, probability)
    # print("gini is", gini)
    return gini


"""InfoGain"""


def chooseBestPred1(pts, preds):
    Best = {'maxInfoGain': 0, 'predicate': False}
    # print("use InfoGain to choose")
    # print("Set of predicates\n\t", preds)
    # print("pts:", pts)
    for pred in preds:
        ptsYes = []
        ptsNo = []
        for pt in pts:
            if ptSatPred(pt, pred):
                ptsYes.append(pt)
            else:
                ptsNo.append(pt)
        # print("predicate:",pred)
        # print(ptsYes, ":", ptsNo)
        # print((len(ptsYes)/len(pts))*Entropy(ptsYes),
        #       ":", (len(ptsNo)/len(pts))*Entropy(ptsNo))
        # InfoGain =(len(ptsYes)/len(pts)) * \
        #     Entropy(ptsYes) +(len(ptsNo)/len(pts))*Entropy(ptsNo)
        InfoGain = Entropy(pts) - (len(ptsYes) / len(pts)) * \
                   Entropy(ptsYes) - (len(ptsNo) / len(pts)) * Entropy(ptsNo)
        # print("InfoGain is ",InfoGain)
        if InfoGain > Best['maxInfoGain']:
            Best['maxInfoGain'] = InfoGain
            Best['predicate'] = pred
    return Best['predicate']


"""Gini"""


def chooseBestPred2(pts, preds):
    Best = {'minGini': 1 - 1 / len(preds), 'predicate': False}
    # print("use gini to choose")
    # print("Set of predicates\n\t", preds)
    # print("pts:", pts)
    for pred in preds:
        ptsYes = []
        ptsNo = []
        for pt in pts:
            if ptSatPred(pt, pred):
                ptsYes.append(pt)
            else:
                ptsNo.append(pt)
        # print("=============predicate===============================:",pred)
        # print(ptsYes, ":", ptsNo)
        if len(ptsYes) == 0 or len(ptsNo) == 0:
            continue
        gini = (len(ptsYes) / len(pts)) * Gini(ptsYes) + (len(ptsNo) / len(pts)) * Gini(ptsNo)
        # print("gini after split is ", gini)
        if gini < Best['minGini']:
            Best['minGini'] = gini
            Best['predicate'] = pred
    return Best['predicate']


def ptSatPred(pt, pred) -> bool:
    pred = str(pred)
    if Game["var_num"] == 2:
        pred = pred.replace('v2', str(pt[1]))
    elif Game["var_num"] == 3:
        pred = pred.replace('v2', str(pt[1])).replace('v3', str(pt[2]))
    pred = pred.replace('v1', str(pt[0]))
    return eval(pred)


"""tree -> expression"""


def tree2Expr(DT) -> str:
    if not DT:
        return "False"
    if DT == True:
        return "True"
    expr = ""
    # 'NoneType' object has no attribute 'val'
    if (type(DT.val) == type("False")):
        return DT.val
    if (type(DT.val) == type(v1 == v2)):
        expr = "If(" + str(DT.val) + "," + tree2Expr(DT.left) + \
               "," + tree2Expr(DT.right) + ")"
    if (type(DT.val) == type(v1) or type(DT.val) == type(0)):
        expr = str(DT.val)
    return expr


"""tree -> LossingFormula"""


def tree2LossingFormula(DT) -> str:
    if DT == True:
        return "True"
    if (type(DT.val) == type("False")):
        # print(DT.val)
        return DT.val
    # t2ftime = time.time()
    paths = []  # Store path And(,,,)
    stack = []
    p = DT
    pre = None
    while (p != None or len(stack) != 0):
        while (p != None and type(p.val) != type("term")):
            stack.append(p)
            p = p.left
        if p != None and p.val == "True":
            if len(stack) == 1:
                paths.append(stack[0].val)
            else:
                arr = []
                for i in stack[0:-1]:
                    if type(i.left.val) == type("term") and i.left.val == "True":
                        continue
                    if type(i.right.val) == type("term") and i.right.val == "True":
                        continue
                    arr.append(i)
                if arr == []:
                    paths.append(stack[-1].val)
                else:
                    expr = "And("
                    for i in arr:
                        expr = expr + str(i.val) + ","
                    expr = expr + str(stack[-1].val) + ")"
                    paths.append(expr)
        p = stack.pop()
        if (type(p.right.val) == type("term") or p.right == pre):
            if (type(p.right.val) == type("term") and p.right.val == "True"):
                p.val = Not(p.val)
                stack.append(p)
                if len(stack) == 1:
                    paths.append(stack[0].val)
                else:
                    arr = []
                    for i in stack[0:-1]:
                        if type(i.left.val) == type("term") and i.left.val == "True":
                            continue
                        if type(i.right.val) == type("term") and i.right.val == "True":
                            continue
                        arr.append(i)
                    if arr == []:
                        paths.append(stack[-1].val)
                    else:
                        expr = "And("
                        for i in arr:
                            expr = expr + str(i.val) + ","
                        expr = expr + str(stack[-1].val) + ")"
                        paths.append(expr)
                stack = stack[:-1]
            pre = p
            p = None
        else:
            p.val = Not(p.val)
            stack.append(p)
            p = p.right
    if len(paths) == 1:
        # print("Tiem of tree transform normal expression：", time.time()-t2ftime)
        return str(paths[0])
    else:
        expr = "Or("
        for i in paths:
            expr = expr + str(i) + ","
        expr = expr[0:len(expr) - 1] + ")"
        # print("Time of tree transform normal expression：", time.time()-t2ftime)
        return expr


"""global transition formula"""
global_transition_formula = "Or("
for i in Game["actions"]:
    if i['action_parameter'] != []:
        temp = "["
        for j in i['action_parameter']:
            temp = temp + str(j) + ","
        temp = temp[:-1]
        temp += "],"
        global_transition_formula = global_transition_formula + \
                                    "Exists(" + temp + str(i["transition_formula"]) + "),"
    else:
        global_transition_formula = global_transition_formula + \
                                    str(i["transition_formula"]) + ","

global_transition_formula = global_transition_formula[:-1]
global_transition_formula = global_transition_formula + ")"

print("Global transition formula:\n\t", global_transition_formula)
global_transition_formula = simplify(eval(global_transition_formula))

"""
default state 
"""
position = []
if Game['var_num'] == 1:
    for i in range(0, 200):
        position.append('illegal')
elif Game['var_num'] == 2:
    for i in range(0, 100):
        position.append([])
        for j in range(0, 100):
            position[i].append('illegal')
elif Game['var_num'] == 3:
    for i in range(0, 100):
        position.append([])
        for i1 in range(0, 100):
            position[i].append([])
            for i2 in range(0, 100):
                position[i][i1].append("illegal")

"""
set all terminate state position  
"""
TerminatePosition = []
while (True):
    s = Solver()
    s.add(Game["Terminal_Condition"])
    s.add(Game["Constraint"])
    if Game["var_num"] == 1:
        s.add(v1 < 200)
        for i in TerminatePosition:
            s.add(v1 != i[0])
        if (s.check() == sat):
            m = s.model()
            a = m[v1].as_long()
            TerminatePosition.append([a])
            if Game["type"] == "normal":
                position[a] = True
            else:
                position[a] = False
        else:
            break
    elif Game["var_num"] == 2:
        s.add(v1 < 100, v2 < 100)
        for i in TerminatePosition:
            s.add(Or(v1 != i[0], v2 != i[1]))
        if s.check() == sat:
            m = s.model()
            a = m[v1].as_long()
            b = m[v2].as_long()
            TerminatePosition.append([a, b])
            if (Game["type"] == "normal"):
                position[a][b] = True
            else:
                position[a][b] = False
        else:
            break
    elif Game["var_num"] == 3:
        s.add(v1 < 100, v2 < 100, v3 < 100)
        for i in TerminatePosition:
            s.add(Or(v1 != i[0], v2 != i[1], v3 != i[2]))
        if s.check() == sat:
            m = s.model()
            a = m[v1].as_long()
            b = m[v2].as_long()
            c = m[v3].as_long()
            TerminatePosition.append([a, b, c])
            if (Game["type"] == "normal"):
                position[a][b][c] = True
            else:
                position[a][b][c] = False
        else:
            break
print("All terminate position:\n\t", TerminatePosition)

"""Determine whether state is a winning state"""


def isLossingState(v):
    if termination_sign:
        print("Time out,about to exit the program")
        sheet1.write(row, 2, "time-out-1200s")
        newwb.save(resultFile)
        sys.exit(0)
    # print("Insert",v," into isLossingstate:")
    if len(v) == 1:
        if v[0] >= 200:
            return 'illegal'
    else:
        for i in v:
            if i >= 100:
                return 'illegal'
    if len(v) == 1:
        if position[v[0]] != 'illegal':
            return position[v[0]]
        for x in range(0, v[0] + 1):
            if (position[x] != 'illegal'):
                continue
            temp = []
            while (True):
                s = Solver()
                s.add(global_transition_formula)
                s.add(Game["Constraint"])
                s.add(v1 == x)
                for i in temp:
                    s.add(Or(v1_next != i[0]))
                if (s.check() == sat):
                    m = s.model()
                    temp.append([m[v1_next].as_long()])
                else:
                    break
            is_losing = True
            s = Solver()
            s.add(Game["Constraint"])
            s.add(v1 == x)
            if (s.check() == unsat):
                continue
            for i in temp:
                if (position[i[0]] == 'illegal'):
                    position[i[0]] = isLossingState(i)
            for i in temp:
                is_losing = is_losing and not position[i[0]]
            if (is_losing):
                position[x] = True
            else:
                position[x] = False
        return position[v[0]]
    elif len(v) == 2:
        if position[v[0]][v[1]] != 'illegal':
            return position[v[0]][v[1]]
        for x in range(0, v[0] + 1):
            for y in range(0, v[1] + 1):
                if (position[x][y] != 'illegal'):
                    continue
                temp = []
                while (True):
                    s = Solver()
                    s.add(global_transition_formula)
                    s.add(Game["Constraint"])
                    s.add(v1 == x, v2 == y)

                    for i in temp:
                        s.add(Or(v1_next != i[0], v2_next != i[1]))

                    if (s.check() == sat):
                        m = s.model()
                        temp.append([m[v1_next].as_long(), m[v2_next].as_long()])
                    else:
                        break
                # print('Transilate 773 of',x,y,":\t",temp) #[[2, 1], [2, 0], [1, 1]]
                is_losing = True
                s = Solver()
                s.add(Game["Constraint"])
                s.add(v1 == x, v2 == y)
                if (s.check() == unsat):
                    continue
                for i in temp:
                    if (position[i[0]][i[1]] == 'illegal'):
                        position[i[0]][i[1]] = isLossingState(i)
                for i in temp:
                    is_losing = is_losing and not position[i[0]][i[1]]
                if (is_losing):
                    position[x][y] = True
                else:
                    position[x][y] = False
        # print("state：",v,"is",position[v[0]][v[1]])
        return position[v[0]][v[1]]
    elif len(v) == 3:
        if position[v[0]][v[1]][v[2]] != 'illegal':
            return position[v[0]][v[1]][v[2]]
        for x in range(0, v[0] + 1):
            for y in range(0, v[1] + 1):
                for z in range(0, v[2] + 1):
                    if (position[x][y][z] != 'illegal'):
                        continue
                    temp = []
                    while (True):
                        s = Solver()
                        s.add(global_transition_formula)
                        s.add(Game["Constraint"])
                        s.add(v1 == x, v2 == y, v3 == z)
                        for i in temp:
                            s.add(Or(v1_next != i[0], v2_next != i[1], v3_next != i[2]))
                        if s.check() == sat:
                            m = s.model()
                            temp.append(
                                [m[v1_next].as_long(), m[v2_next].as_long(), m[v3_next].as_long()])
                        else:
                            break
                    is_losing = True
                    s = Solver()
                    s.add(Game["Constraint"])
                    s.add(v1 == x, v2 == y, v3 == z)
                    if (s.check() == unsat):
                        continue
                    for i in temp:
                        if (position[i[0]][i[1]][i[2]] == 'illegal'):
                            position[i[0]][i[1]][i[2]] = isLossingState(i)
                    for i in temp:
                        is_losing = is_losing and not position[i[0]][i[1]][i[2]]
                    if (is_losing):
                        position[x][y][z] = True
                    else:
                        position[x][y][z] = False
        return position[v[0]][v[1]][v[2]]


#  ptList=[[pt1],[pt2],[pt3]]
def FindCountExample(ptList):
    if Game["var_num"] == 1:
        i = 1
        while (True):
            if i > 100:
                global example_run_out_sign
                example_run_out_sign = True
                return 'illegal'
            for r1 in range(0, i):
                if [r1] not in ptList and [r1] not in pts:
                    s = Solver()
                    s.add(Game["Constraint"])
                    s.add(v1 == r1)
                    if (s.check() == sat):
                        return [r1]
                        # Strict counterexample
                        # boolTemp = isLossingState(r1)
                        # boolTemp2 = eval(str(e).replace(str(v1), str(r1)))
                        # s = Solver()
                        # if boolTemp == False:
                        #     s.add(True, boolTemp2)
                        #     if(s.check() == sat):
                        #         return [r1]
                        # elif boolTemp == True:
                        #     s.add(True, boolTemp2)
                        #     if(s.check() == unsat):
                        #         return [r1]
                    else:
                        continue
            i += 1
    elif Game["var_num"] == 2:
        i = 1
        if i > 100:
            example_run_out_sign = True
            return 'illegal'
        while (True):
            for r1 in range(0, i + 1):
                r2 = i - r1
                # print("828",r1,r2)
                if [r1, r2] not in ptList and [r1, r2] not in pts:
                    s = Solver()
                    s.add(Game["Constraint"])
                    s.add(v1 == r1, v2 == r2)
                    if s.check() == sat:
                        # print("find example:", r1, r2)
                        return [r1, r2]
                        # Strict counterexample
                        # boolTemp = isLossingState(r1, r2)
                        # boolTemp2 = eval(str(e).replace(
                        #     str(v2), str(r2)).replace(str(v1), str(r1)))
                        # s = Solver()
                        # if boolTemp == False:
                        #     s.add(True, boolTemp2)
                        #     if(s.check() == sat):
                        #         return [r1, r2]
                        # elif boolTemp == True:
                        #     s.add(True, boolTemp2)
                        #     if(s.check() == unsat):
                        #         return [r1, r2]
                    else:
                        continue
            i = i + 1
    elif Game["var_num"] == 3:
        i = 1
        while True:
            if i > 100:
                example_run_out_sign = True
                return 'illegal'
            for r1 in range(0, i + 1):
                for r2 in range(0, i - r1 + 1):
                    r3 = i - r1 - r2
                    if [r1, r2, r3] not in ptList and [r1, r2, r3] not in pts:
                        s = Solver()
                        s.add(Game["Constraint"])
                        s.add(v1 == r1, v2 == r2, v3 == r3)
                        if s.check() == sat:
                            return [r1, r2, r3]
                            # Strict counterexample
                            # boolTemp = isLossingState(r1, r2, r3)
                            # boolTemp2 = eval(str(e).replace(
                            #     str(v2), str(r2)).replace(str(v3), str(r3)).replace(str(v1), str(r1)))
                            # s = Solver()
                            # if boolTemp == False:
                            #     s.add(True, boolTemp2)
                            #     if(s.check() == sat):
                            #         return [r1, r2, r3]
                            # elif boolTemp == True:
                            #     s.add(True, boolTemp2)
                            #     if(s.check() == unsat):
                            #         return [r1, r2, r3]
                        else:
                            continue
            i = i + 1


def isCoverAll():
    coverAll = []
    for term in terms:
        for i in cover[term]:
            coverAll.append(i)
    # print("cover included",coverAll)
    for pt in pts:
        if pt not in coverAll:
            return False
    return True


def outRange(v):
    if len(v) == 1:
        if v[0] >=200 or v[0] < 0:
            return 'illegal'
    else:
        for i in v:  # default position < 100
            if i >= 100 or i < 0:
                return 'illegal'


def satfindstate(ptk):
    ptK = ptk
    ptList = []
    m = s.model()
    value = []
    for i in Game["varList"]:
        value.append(m[i].as_long())
    if outRange(value) != 'illegal':
        # print("countexample：",value)
        ptK -= 1
        ptList.append(value)
        if (ptK == 0):
            return ptList
    # while ptK > 0:
    #     if len(value) == 1:
    #         s.add(v1!=value[0])
    #     elif len(value) == 2:
    #         s.add(Or(v1!=value[0],v2!=value[1]))
    #     elif len(value) == 3:
    #         s.add(Or(v1!=value[0],v2!=value[1],v3!=value[2]))
    #     if s.check() == sat:
    #         m = s.model()
    #         value =[]
    #         for i in Game['varList']:
    #             value.append(m[i].as_long())
    #         print("not sat ,countexample is:",value)
    #         ptK = ptK - 1
    #         ptList.append(value)
    #     else:
    #         print("no many countexample")
    #         break
    while ptK > 0:
        if termination_sign:
            print("Time out,about to exit the program")
            sheet1.write(row, 2, "time-out-1200s")
            newwb.save(resultFile)
            sys.exit(0)
        pt = FindCountExample(ptList)
        if pt == 'illegal':
            return ptList
        if outRange(pt) == 'illegal':
            continue
        else:
            ptK -= 1
            ptList.append(pt)
    print("Generate", ptk, "countexamples:\t", ptList)
    return ptList


def unkownfindstate(ptk):
    ptK = ptk
    ptList = []
    while True:
        pt = FindCountExample(ptList)
        if pt == 'illegal':
            return ptList
        if outRange(pt) == 'illegal':
            continue
        else:
            ptK -= 1
            ptList.append(pt)
            if (ptK == 0):
                print("InitializeStates", ptk, "example generate:\t", ptList)
                return ptList


def countSize(var, varpool):
    if is_number(var):
        var = float(var)
    if type(var) != type(1.0):
        return 1
    elif var in varpool:
        return 1
    else:
        return 1 + countSize(var, expandpool(varpool))


def expandpool(varpool):
    p = []
    for i in varpool:
        p.append(i)
    # while i < len(varpool):
    i = 0
    j = 0

    while i < len(varpool):

        while j < len(varpool):

            if varpool[i] + varpool[j] not in p:
                p.append(varpool[i] + varpool[j])
            j += 1
        i += 1
        j = i
    # print(p)
    return p


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


def Size(expression, varpool=[0, 1]):
    count1 = 0
    str1 = expression.replace(' ', '').replace('\n', '')
    while str1.find('Not') >= 0:
        count1 += 1
        str1 = str1.replace('Not', '', 1)
    while str1.find('Or') >= 0:
        count1 += 1
        str1 = str1.replace('Or', '', 1)
    while str1.find('And') >= 0:
        count1 += 1
        str1 = str1.replace('And', '', 1)
    str1 = str1.replace('*', '-').replace(',', '-').replace('+', '-').replace('<=', '-').replace('>=', '-').replace('<',
                                                                                                                    '-').replace(
        '>', '-').replace('==', '-').replace('%', '-').replace('(', '').replace(')', '')
    while True:
        if len(str1) == 0:
            break
        if len(str1) == 1:
            count1 += countSize(str1, varpool)
            break
        if len(str1) == 2 and is_number(str1[0]):
            count1 += countSize(str1, varpool)
            break
        if len(str1) == 2:
            count1 += countSize(str1, varpool)
            break
        tempvar = str1[0:str1.find('-')]
        # print(tempvar,'size is',countSize(tempvar,varpool))
        # print(count1)
        count1 += countSize(str1[0:str1.find('-')], varpool)
        str1 = str1[str1.find('-') + 1:len(str1)]
    return count1


def Getvarpool(pddl):
    num = re.findall('\d+', pddl)
    num = list(set(num))
    num = list(map(int, num))
    if not (0 in num):
        num.append(0)
    if not (1 in num):
        num.append(1)
    if not (2 in num):
        num.append(2)
    return num


def GetSize(gamename, winningformula):
    if winningformula == "False" or winningformula == "True" or winningformula == "true":
        return 1
    varpool = Getvarpool(gamename)
    size = Size(winningformula, varpool)
    return size


start_winning_formula_time = time.time()

# The time thread determines whether it timed out
termination_sign = False


def programTimeOut():
    global termination_sign
    termination_sign = True
    Thread1.cancel()


Thread1 = threading.Timer(time_out1, programTimeOut)
Thread1.start()

pts = []
ptsGoal = []

Maxsize = 1
preds = []
# unknownNum = 1
newwb = copy(oldwb)
sheet1 = newwb.get_sheet(0)
sheet1.write(row, 0, gameName)
newwb.save(resultFile)

print("\n")
print("####################################################################")
print("################# Learning winning formula #########################")
print("####################################################################")
print("\n")

while (True):
    if termination_sign:
        print("Time out,about to exit the program")
        sheet1.write(row, 2, "time-out-1200s")
        newwb.save(resultFile)
        sys.exit(0)
    terms = [True, False]
    cover = {}
    cover[True] = []
    cover[False] = []
    for num in range(len(pts)):
        cover[ptsGoal[num]].append(pts[num])
    print("Labels set: \t", str(cover).replace('True', 'temp').replace('False', 'True').replace('temp', 'False'))
    DT = None
    e = v1 == v1  # Default formula
    last_e = e
    DTTime = time.time()
    global DTflag
    DTflag = True
    flagAdd = True
    while pts != [] and (DT == None or DTflag == False):
        if termination_sign:
            print("Time out,about to exit the program")
            sheet1.write(row, 2, "time-out-1200s")
            newwb.save(resultFile)
            sys.exit(0)
        enumPredsTime = time.time()
        enumeratePredicate(Maxsize, DTflag)  # DTflag- Continue enumerating predicates in the last place
        print("the set of atoms:", preds)
        print("Number of data points:  ", len(pts))
        calculateIGTime = time.time()
        DTflag = True
        # *********************************************************************************************************
        if choice_method == "ID3":
            DT = learn_DT(pts, preds)
        elif choice_method == "Incre":
            DT = learn(pts, preds)
        elif choice_method == "DT1":
            DT = learn_sat_DT1(pts, preds)
        elif choice_method == "DTEP":
            DT = learn_sat_DTEP(pts, preds)
        #*********************************************************************************************************
        # print("Information gain time ：",time.time()-calculateIGTime)
        if (DTflag == False):
            Maxsize += 1
            flagAdd = False
            print('Cannot solve,need more atoms, increase Maxsize', Maxsize)
    # print("Time of learn DT：", time.time()-DTTime)
    if DT != None:
        e = eval(tree2Expr(DT))
    print("\n-------------------------- Learn decision tree -------------------------\n\t",
          str(e).replace('True', 'temp').replace('False', 'True').replace('temp', 'False'))
    try:
        e1 = eval(str(e).replace("v2", "v2_next").replace("v3", "v3_next").replace("v1", "v1_next"))
    except:
        Thread1.cancel()
        print("Time out,about to exit the program")
        sheet1.write(row, 2, str(time_out1))
        newwb.save(resultFile)
        sys.exit(0)

    print("\n----------------------------- Verification  ----------------------------\n")

    if str(e) != str(last_e):
        if Game["type"] == "normal":
            # e is losing formula
            # con1 = Not(Implies(Game['Terminal_Condition'],e))
            con1 = And(Game["Constraint"], Game["Terminal_Condition"], Not(e))
            # con2 = And(Game["Constraint"], Not(e), ForAll(varListY, Or(Not(global_transition_formula), Not(e1))))
            con3 = And(Game["Constraint"], e, Not(Game["Terminal_Condition"]),
                       Exists(varListY, And(global_transition_formula, e1)))
            # con3 =Not(Implies(And(Game["Constraint"],e),ForAll(varListY, Implies(global_transition_formula, Not(e1)))))
            con2 = Not(Implies(And(Game["Constraint"], Not(e)), Exists(varListY, And(global_transition_formula, e1))))
        else:
            # con1 = Not(Implies(Game['Terminal_Condition'],Not(e)))
            con1 = And(Game["Constraint"], Game["Terminal_Condition"], e)
            # con2 = And(Game["Constraint"], Not(e), Not(Game["Terminal_Condition"]), ForAll(varListY, Implies(global_transition_formula, Not(e1))))
            con2 = Not(Implies(And(Game["Constraint"], Not(e), Not(Game["Terminal_Condition"])), Exists(
                varListY, And(global_transition_formula, e1))))
            # con3 = Not(Implies(And(Game["Constraint"],e),ForAll(varListY, Implies(global_transition_formula, Not(e1)))))
            con3 = And(Game["Constraint"], e), Exists(varListY, And(global_transition_formula, e1))

        s = Solver()
        s.set('timeout', 60000)
        s.add(con1)
        check1 = s.check()
        # print("con1 check:",check1)
        if check1 == sat:
            # print("unsat con1")
            print(
                "The constraint of winning formula is not valid and add countexamples, go to the next round of the learning process.")
            examples = satfindstate(ptk)
        else:
            # print("sat con1")
            s = Solver()
            s.set('timeout', 60000)
            s.add(con2)
            check2 = s.check()
            # print("con2 check:",check2)
            if check2 == sat:
                # print("unsat con2")
                print(
                    "The constraint of winning formula is not valid and add countexamples, go to the next round of the learning process.")
                examples = satfindstate(ptk)
            else:
                # print("sat con2")
                s = Solver()
                s.set('timeout', 60000)
                s.add(con3)
                check3 = s.check()
                # print("con3 check:",check3)
                if check3 == sat:
                    # print("unsat con3")
                    print(
                        "The constraint of winning formula is not valid and add countexamples, go to the next round of the learning process.")
                    examples = satfindstate(ptk)
                else:
                    # print("sat con3")
                    print("The constraints of wwinning formula is valid")
                    # if unknownNum > 0 and (check1 == unknown or check2 ==unknown or check3 == unknown):

                    #         unknownNum -= 1
                    #         print("have a result unknown")
                    # losing_formula = e
                    # print("decision tree formula：",tree2LossingFormula(DT))
                    # else:
                    resultDT = deepcopy(DT)
                    losing_formula = eval(tree2LossingFormula(DT))

                    print("\n---------------------------- Winning formula  --------------------------\n")

                    print("Losing formula：", losing_formula)
                    losing_formula_Y = e1
                    winning_formula = simplify(Not(losing_formula))
                    sizeFormula = GetSize(gameName, str(winning_formula))
                    winning_formula_time = time.time() - start_winning_formula_time
                    print("Winning Fromula：", winning_formula)
                    print("The total running time：", round(winning_formula_time, 2))
                    print("The size: ", sizeFormula)
                    winning_formula_time = str(round(winning_formula_time, 2))

                    sheet1.write(row, 1, str(winning_formula))
                    sheet1.write(row, 2, winning_formula_time)
                    sheet1.write(row, 3, sizeFormula)
                    # sheet1.write(row, 5, str(check1)+str(check2)+str(check3))
                    newwb.save(resultFile)
                    # newwb.save(resultFile)
                    # fp = open(resultFile, 'a')
                    # fp.write(pddlFile.split('\\')[-1]+"\t")
                    # fp.write(str(simplify(Not(losing_formula))) +
                    #          "\t"+winning_formula_time+"\n")
                    Thread1.cancel()  # Cancel thread
                    break
    else:
        print("Repeat expression")
        examples = unkownfindstate(ptk)
    if Game["var_num"] == 1:
        for i in examples:
            if i not in pts and outRange(i) != 'illegal':
                pts.append(i)
                ptsGoal.append(isLossingState(i))
    elif Game["var_num"] == 2:
        for i in examples:
            if i not in pts and outRange(i) != 'illegal':
                pts.append(i)
                ptsGoal.append(isLossingState(i))
    elif Game["var_num"] == 3:
        for i in examples:
            if i not in pts and outRange(i) != 'illegal':
                pts.append(i)
                ptsGoal.append(isLossingState(i))
# print("=======================================================================")
# print(winning_formula)
winning_formula_Y = eval(str(winning_formula).replace("v2", "v2_next")
                         .replace("v3", "v3_next").replace("v1", "v1_next"))
# print(losing_formula)
losing_formula_Y = eval(str(losing_formula).replace("v2", "v2_next")
                        .replace("v3", "v3_next").replace("v1", "v1_next"))
# print(winning_formula_Y)
# print("losing_formula_Y:",losing_formula_Y)

if losing_formula == False or losing_formula == True:
    print("The winning formula is true or false")
    sheet1.write(row, 4, "Fasle/True")
    newwb.save(resultFile)
    sys.exit(0)

# print(actions)
# print(actions[0]['action_name'])
# [{'action_name': 'eat1', 'action_parameter': [k], 'precondition':
# And(v1 >= k, k > 1), 'transition_formula': And(And(v1 >= k, k > 1),
#     And(v1_next == -1 + k, If(v2 >= k, v2_next == -1 + k, v2_next == v2)))}]
lenActs = len(actions)


def genOutput(pt):
    print("Generate ground action for datapoint", pt)
    outputList = []
    for i in range(0, lenActs):
        action = actions[i]
        while True:
            s = Solver()
            for output in outputList:
                parasLen = len(action["action_parameter"])
                if i == output[0] and parasLen == len(output) - 1:
                    if parasLen == 1:
                        s.add(k != output[1])
                    else:
                        con = "Or("
                        for num in range(0, parasLen):
                            con = con + str(action["action_parameter"][num]) + "!=" + str(output[num + 1]) + ","
                        con = con[:-1]
                        con = con + ")"
                        s.add(eval(con))
            if Game['var_num'] == 1:
                s.add(v1 == pt[0])
            elif Game["var_num"] == 2:
                s.add(v1 == pt[0], v2 == pt[1])
            elif Game["var_num"] == 3:
                s.add(v1 == pt[0], v2 == pt[1], v3 == pt[2])
            s.add(actions[i]['precondition'])
            s.add(actions[i]['transition_formula'])
            s.add(losing_formula_Y)
            if s.check() == sat:
                m = s.model()
                ans = [i]
                for para in action["action_parameter"]:
                    ans.append(m[para].as_long())  # addk
                printGroundAction(ans)
                # action = actions[ans[0]]
                # print("exist ground action:" + action["action_name"]+ "("+str(ans)[4:-1]+")")
                # print(" [act,para] ",ans)
                outputList.append(ans)
            else:
                break
    return outputList


def genPtSatFormula(pathformula, ptList):
    if Game['var_num'] == 1:
        i = 1
        while True:
            if i > 150: return False
            for r1 in range(0, i + 1):
                if [r1] not in ptList and [r1] not in pts:
                    s = Solver()
                    s.add(Game['Constraint'])
                    s.add(Not(Game["Terminal_Condition"]))
                    # s.add(winning_formula)
                    s.add(pathformula)
                    s.add(v1 == r1)
                    if s.check() == sat:
                        # print("find state:",r1)
                        return [r1]
            i = i + 1
    elif Game['var_num'] == 2:
        i = 1
        while True:
            if i > 100: return False
            for r1 in range(0, i + 1):
                r2 = i - r1
                if [r1, r2] not in ptList and [r1, r2] not in pts:
                    s = Solver()
                    s.add(Game['Constraint'])
                    s.add(Not(Game["Terminal_Condition"]))
                    # s.add(winning_formula)
                    s.add(pathformula)
                    s.add(v1 == r1, v2 == r2)
                    if s.check() == sat:
                        # print("find state:",r1,r2)
                        return [r1, r2]
            i = i + 1
    elif Game['var_num'] == 3:
        i = 1
        while True:
            if i > 250: return False
            for r1 in range(0, i + 1):
                for r2 in range(0, i - r1 + 1):
                    r3 = i - r1 - r2
                    if [r1, r2, r3] not in ptList and [r1, r2, r3] not in pts:
                        s = Solver()
                        s.add(Game['Constraint'])
                        s.add(Not(Game["Terminal_Condition"]))
                        # s.add(winning_formula)
                        s.add(pathformula)
                        s.add(v1 == r1, v2 == r2, v3 == r3)
                        if s.check() == sat:
                            # print("find state:",r1,r2,r3)
                            return [r1, r2, r3]
            i = i + 1


def printGroundAction(termlist):
    action = actions[termlist[0]]
    print("Find a ground action:" + action["action_name"] + "(" + str(termlist)[4:-1] + ")")


def printAction(termlist):
    action = actions[termlist[0]]
    print("Find action:" + action["action_name"] + "(" + str(termlist)[4:-1] + ")")


# [str,str...]

def pathOfWF(DT):
    paths = []
    stack = []
    p = DT
    pre = None
    while p != None or len(stack) != 0:
        while (p != None and type(p.val) != type("term")):
            stack.append(p)
            p = p.left
        if p != None and p.val == "False":
            # print("1806",p.val)
            if len(stack) == 1:
                paths.append(str(stack[0].val))
            else:
                arr = []
                for i in stack[0:-1]:
                    if type(i.left.val) == type("term") and i.left.val == "False":
                        continue
                    if type(i.right.val) == type("term") and i.right.val == "False":
                        continue
                    arr.append(i)
                # print("1819",arr)
                if arr == []:
                    paths.append(str(stack[-1].val))
                else:
                    expr = "And("
                    for i in arr:
                        expr = expr + str(i.val) + ","
                    expr = expr + str(stack[-1].val) + ")"
                    paths.append(expr)
        p = stack.pop()  # p.left is term
        # If it is a leaf node and has not been accessed
        if (type(p.right.val) == type("term") or p.right == pre):
            if (type(p.right.val) == type("term") and p.right.val == "False"):
                p.val = Not(p.val)
                stack.append(p)
                if len(stack) == 1:
                    paths.append(str(stack[0].val))
                else:
                    arr = []
                    for i in stack[0:-1]:
                        if type(i.left.val) == type("term") and i.left.val == "False":
                            continue
                        if type(i.right.val) == type("term") and i.right.val == "False":
                            continue
                        arr.append(i)
                    if arr == []:
                        paths.append(str(stack[-1].val))
                    else:
                        expr = "And("
                        for i in arr:
                            expr = expr + str(i.val) + ","
                        expr = expr + str(stack[-1].val) + ")"
                        paths.append(expr)
                stack = stack[:-1]
            pre = p
            p = None
        else:
            # Non leaf node
            p.val = Not(p.val)
            stack.append(p)
            p = p.right
    return paths


# print("Decision tree2:",tree2Expr(resultDT))

# all path
def pathOfAct(DT):
    if type(DT.val) == type("term"):
        return [["", eval(DT.val)]]
    paths = []
    stack = []
    p = DT
    pre = None
    while p != None or len(stack) != 0:
        while (p != None and type(p.val) != type("str")):
            stack.append(p)
            p = p.left
        if p != None:
            if len(stack) == 1:
                paths.append([stack[0].val, eval(p.val)])
            else:
                expr = "And("
                for i in stack:
                    expr = expr + str(i.val) + ","
                expr = expr[0:len(expr) - 1] + ")"
                paths.append([eval(expr), eval(p.val)])
        p = stack.pop()
        if (type(p.right.val) == type("term") or p.right == pre):
            if type(p.right.val) == type("term"):
                p.val = Not(p.val)
                stack.append(p)
                if len(stack) == 1:
                    paths.append([stack[0].val, eval(p.right.val)])
                else:
                    expr = "And("
                    for i in stack:
                        # print(i.val)
                        expr = expr + str(i.val) + ","
                    expr = expr[0:len(expr) - 1] + ")"
                    paths.append([eval(expr), eval(p.right.val)])
                stack = stack[:-1]
            pre = p
            p = None
        else:
            p.val = Not(p.val)
            stack.append(p)
            p = p.right
    return paths


# THIS term = [act.id parameter]
def isTermSatExample(term, pt, output):
    if output[0] != term[0] or len(output) != len(term):
        return False
    if Game["var_num"] == 2:
        for i in range(1, len(term)):  # term [0,v1], [0,v1,v1_next]
            if eval(str(term[i]).replace('v2', str(pt[1])).replace('v1', str(pt[0]))) != output[i]:
                return False
        return True
    elif Game['var_num'] == 3:  # [0,5,1] [0,v1-v3,v2-v3]
        for i in range(1, len(term)):
            if eval(str(term[i]).replace('v2', str(pt[1])).replace('v3', str(pt[2])).replace('v1', str(pt[0]))) != \
                    output[i]:
                return False
        return True
    elif Game["var_num"] == 1:
        for i in range(1, len(term)):
            if eval(str(term[i]).replace('v1', str(pt[0]))) != output[i]:
                return False
        return True


# Ensure that pt-outputs all output have term cover
def ptsAllCover():
    print("Ensure each data point have label cover:")
    for num in range(len(pts)):
        pt = pts[num]
        ptOutput = ptsOutput[num]
        for output in ptOutput:
            flag_cover = False
            for term in terms:
                if isTermSatExample(term, pt, output):
                    flag_cover = True
                    break
            if flag_cover == False:
                print(pt, "no label cover:", )
                if len(output) == 2:
                    term = (output[0], enumerateTerm(pt, output[1]))
                elif len(output) == 3:
                    term = (output[0], enumerateTerm(pt, output[1]), enumerateTerm(pt, output[2]))
                elif len(output) == 4:
                    term = (
                    output[0], enumerateTerm(pt, output[1]), enumerateTerm(pt, output[2]), enumerateTerm(pt, output[3]))
                printAction(term)
                # print("find term",term,"cover")
                if term not in cover:
                    terms.append(term)
                    cover[term] = []
                cover[term].append(pt)


# Update the relationship between all terms and PTS
def updateCover():
    # print("update cover.........")
    for term in terms:
        for num in range(0, len(pts)):
            pt = pts[num]
            ptOutput = ptsOutput[num]
            if pt not in cover[term]:
                for output in ptOutput:
                    if isTermSatExample(term, pt, output):
                        cover[term].append(pt)
                        break


"""convert tree to winning strategy formula::  leaf node -- action"""


def tree2WinningStrategy(DT) -> str:
    expr = ""
    if type(DT.val) == type("str"):
        term = eval(DT.val)
        action = actions[term[0]]
        action = eval(str(action).replace("k", '(' + str(term[1]) + ')'))
        return str(action["transition_formula"])
    if (type(DT.val) == type(v1 == v2)):
        expr = "If(" + str(DT.val) + "," + tree2WinningStrategy(DT.left) + "," + tree2WinningStrategy(DT.right) + ")"
    return expr


def tree2Act(DT):
    if DT == None: return "None"
    expr = ""
    if type(DT.val) == type("term"):
        term = eval(DT.val)
        # print(term)
        action = actions[term[0]]
        return str(action["action_name"]) + "(" + str(term)[4:]
    if (type(DT.val) == type(v1 == v2)):
        expr = "If(" + str(DT.val) + "," + tree2Act(DT.left) + "," + tree2Act(DT.right) + ")"
    return expr


def defaultAction():
    S1 = Solver()
    S1.add(Game["Constraint"])
    S1.add(Game["actions"][0]["precondition"])
    if S1.check() == sat:
        m = S1.model()
        para = m[k].as_long()
        return [["", (0, para)]]
    return


def defaultPreds(pathFormula):
    str1 = str(pathFormula)
    str1 = str1.replace(' ', '').replace("\n", "")
    arr1 = []
    if "And" in str1:  # And(f1, f2, f3 ,f4)
        str1 = str1[4:-1]
        arr = str1.split(",")
    else:  # f1
        arr = [str1]
    for s in arr:
        if "Not" in s:
            s = s[4:-1]
            if "%" in s:  # a%b==c
                b = s[s.find('%') + 1:s.find("==")]
                c = s[s.find("==") + 2:]
                for i in range(0, eval(b)):
                    if str(i) != c:
                        arr1.append(s[:s.find("==") + 2] + str(i))
            elif "==" in s:  # ==
                arr1.append(s.replace("==", ">"))
                arr1.append(s.replace("==", "<"))
        else:
            if ">=" in s:
                arr1.append(s.replace(">=", ">"))
                arr1.append(s.replace(">=", "=="))
            elif "<=" in s:
                arr1.append(s.replace("<=", "<"))
                arr1.append(s.replace("<=", "=="))
    preds = []
    for i in arr1:
        i = eval(i)
        preds.append(i)
    return preds


def isPtSatForm(pt, form):
    s1 = Solver()
    s1.add(form)
    if Game['var_num'] == 1:
        s1.add(v1 == pt[0])
        if s1.check() == sat:
            return True
        else:
            return False
    elif Game['var_num'] == 2:
        s1.add(v1 == pt[0], v2 == pt[1])
        if s1.check() == sat:
            return True
        else:
            return False
    elif Game['var_num'] == 3:
        s1.add(v1 == pt[0], v2 == pt[1], v3 == pt[2])
        if s1.check() == sat:
            return True
        else:
            return False


def splitPaths(pathFormula):  # And(Not(v1 + v2 == 1), Not(x%5=1) ,v1 < v2) Not(v1 + v2 == 1)
    ans = []
    str1 = str(pathFormula)
    str1 = str1.replace(' ', '').replace("\n", "")
    if "And" in str1:
        arr2 = str1[4:-1].split(",")
    else:
        arr2 = [str1]

    arr = []
    for str2 in arr2:
        arr1 = []
        if "Not" in str2:
            if "%" in str2:  # a%b==c
                str2 = str2[4:-1]
                b = str2[str2.find('%') + 1:str2.find("==")]
                c = str2[str2.find("==") + 2:]
                for i in range(0, eval(b)):
                    if str(i) != c:
                        arr1.append(str2[:str2.find("==") + 2] + str(i))
            elif "==" in str2:  # ==
                str2 = str2[4:-1]
                arr1.append(str2.replace("==", ">"))
                arr1.append(str2.replace("==", "<"))
            elif ">=" in str2:
                str2 = str2[4:-1]
                arr1.append(str2.replace(">=", "<"))
        else:
            if ">=" in str2:
                arr1.append(str2.replace(">=", ">"))
                arr1.append(str2.replace(">=", "=="))
            elif "<=" in str2:
                arr1.append(str2.replace("<=", "<"))
                arr1.append(str2.replace("<=", "=="))
        if arr1 == []:
            arr1.append(str2)
        arr3 = []
        # print(arr1)
        for i in arr1:
            s = Solver()
            s.add(eval(i))
            s.add(Game['Constraint'])
            s.add(Not(Game['Terminal_Condition']))
            s.add(winning_formula)
            # print(s.check)
            if s.check() == sat:
                arr3.append(i)
        arr.append(arr3)

    for f in product(*arr):
        ans.append(list(f))
    # print("refinement path :",ans)
    return ans


def extractNum(str):
    str = str.replace(" ", '')
    ans = []
    i = 0
    while i < len(str):
        if str[i] <= '9' and str[i] >= "0":
            ch = str[i]
            while (i < len(str) - 1 and str[i + 1] <= '9' and str[i + 1] >= '0'):
                i = i + 1
                ch = ch + str[i]
            ans.append(ch)  # Game['appeal_constants']
        i += 1
    return ans


for i in extractNum(str(losing_formula)):
    Game['appeal_constants'].append(i)

print("\n")
print("#####################################################################")
print("################# Learning winning strategy #########################")
print("#####################################################################")
print("\n")

ptsOld = cover[False]

# print("winning formula used pts:",ptsOld)
# print("Decision tree1:",tree2Expr(resultDT))
formulaPaths = pathOfWF(deepcopy(resultDT))
print("All T-label paths:\n\t", formulaPaths)


def programTimeOut2():
    global termination_sign
    termination_sign = True
    Thread2.cancel()


termination_sign = False  # Timeout flag
Thread2 = threading.Timer(time_out2, programTimeOut2)
Thread2.start()

startWinningStrategyTime = time.time()
winningStrategy = []
exitFlag = False

# splitFormulaPaths = []
# for pathFormula in formulaPaths:
#     for f in splitPaths(pathFormula):
#         if len(f) > 1: #f = ["",""]
#             str1 = "And("
#             for i in f:
#                 str1 = str1 + i + ","
#             str1 = str1[:-1]+")"
#             s = Solver()
#             s.add(eval(str1))
#             s.add(Game['Constraint'])
#             s.add(Not(Game['Terminal_Condition']))
#             s.add(winning_formula)
#             if s.check() == sat:
#                 splitFormulaPaths.append(str1)
#         else:
#             splitFormulaPaths.append(f[0])

# print("Splitting formula path:\n\t",splitFormulaPaths)

for pathFormula in formulaPaths:
    if exitFlag: break

    print("\n******************** One of T-label path formula:", pathFormula, "**********************\n")

    # print("one T-label path formula:",pathFormula,)
    # print("---------------------------------------------------------------------")

    pathFormula = eval(pathFormula)  # str --> z3
    pts = []
    for pt in ptsOld:
        if isPtSatForm(pt, pathFormula) and pt not in TerminatePosition:
            pts.append(pt)
    ptsOutput = []
    for pt in pts:
        outputs = genOutput(pt)
        ptsOutput.append(outputs)
    preds = defaultPreds(pathFormula)
    print("defaultPreds:\n",preds)
    terms = []
    cover = {}
    maxSizePred = 1
    maxSizeTerm = 0
    while True:
        if termination_sign:
            print("Time out,about to exit the program")
            sheet1.write(row, 4, "time-out-1200s")
            newwb.save(resultFile)
            sys.exit(0)
        print("The set of data points:", pts)
        ptsAllCover()
        updateCover()

        # for key,val in cover.items():
        #     print(key,":",val)
        # cycleNum = 2
        DTflag = True
        DT = None
        # while cycleNum != 0 and pts !=[] and (DT == None or DTflag == False):
        while pts != [] and (DT == None or DTflag == False):
            if termination_sign:
                print("Time out, about to exit the program")
                sheet1.write(row, 4, "time-out-1200s")
                newwb.save(resultFile)
                sys.exit(0)
            # flagAdd = False
            maxSizeTerm += 1
            # if maxSizePred <=3:
            #     maxSizePred += 1
            nextSizeTerm(maxSizeTerm, DTflag)
            print("The set of label:")
            print("\t", end="")
            for i in terms:
                action = actions[i[0]]
                print(action["action_name"] + "(" + str(i)[4:-1] + ")" + "  ", end="")
            print("\n")
            # print("terms\n",terms)

            enumeratePredicate(maxSizePred, DTflag)
            updateCover()

            print("The set of atoms\n\t", preds)
            print("The set of data poins\n\t", pts)
            # print("ptsOutput\n",ptsOutput)
            print("The label of data points:")
            for key, val in cover.items():
                action = actions[key[0]]
                print("\t", action["action_name"] + "(" + str(key)[4:-1] + ")", ":", val)
                # print(key,":",val)
            DTflag = True
            # *********************************************************************************************************
            if choice_method == "ID3":
                DT = learn_DT(pts, preds)
            elif choice_method == "Incre":
                DT = learn(pts, preds)
            elif choice_method == "DT1":
                DT = learn_sat_DT1(pts, preds)
            elif choice_method == "DTEP":
                DT = learn_sat_DTEP(pts, preds)
            #*********************************************************************************************************
            if DTflag == False:
                maxSizePred += 1
                DT = None
                print('Cannot solve ,need bigger atom szie:', maxSizePred, " and more label")
        print("\n---------------------------- Learn decision tree --------------------------")
        print("\t" + tree2Act(DT) + "\n")
        # print("candidate tree",tree2Act(DT))

        print("------------------------------- Verification  -----------------------------\n\t")
        # ActPaths = defaultAction()
        if DT != None:
            ActPaths = pathOfAct(DT)
            print("Path:", pathFormula, ", all canditate strategy:", ActPaths)  # [["", (0, 1, 1)]]
            isSAT = True
            winningStrategyTemp = []
            for path in ActPaths:
                concreteAct = path[1]  # (0,1,1)
                action = deepcopy(actions[concreteAct[0]])
                ActExe = action['action_name'] + '(' + str(concreteAct)[4:]
                for i in range(1, len(concreteAct)):
                    # print(str(action["precondition"]).replace(str(action["action_parameter"][i-1]),"("+str(concreteAct[i])+")"))
                    action["precondition"] = str(action["precondition"]).replace(str(action["action_parameter"][i - 1]),
                                                            "(" + str(concreteAct[i]) + ")")
                    action["transition_formula"] = str(action["transition_formula"]).replace(str(action["action_parameter"][i - 1]),
                                                                  "(" + str(concreteAct[i]) + ")")
                action["precondition"] = eval(action["precondition"])
                action["transition_formula"] = eval(action["transition_formula"])
                preAct = action["precondition"]
                transitionFormula = action["transition_formula"]
                if type(path[0]) != type(""):
                    winningStrategyPath = And(pathFormula, path[0])
                    con = Not(Implies(And(Game["Constraint"], pathFormula, path[0], Not(Game["Terminal_Condition"])),
                                      And(preAct, ForAll(varListY, Implies(transitionFormula, losing_formula_Y)))))
                else:
                    winningStrategyPath = pathFormula
                    con = Not(Implies(And(Game["Constraint"], pathFormula, Not(Game["Terminal_Condition"])),
                                      And(preAct, ForAll(varListY, Implies(transitionFormula, losing_formula_Y)))))

                print("Verify this path:", winningStrategyPath, "execute action:", ActExe)

                s = Solver()
                s.set('timeout', 60000)
                s.add(con)
                if s.check() == sat:
                    print(
                        "The constraint of winning strategy is not valid and add countexamples, go to the next round of the learning process.")
                    print("=========== generate countexample =========")
                    ptK = ptk2
                    ptList = []
                    value = []
                    m = s.model()
                    for i in Game['varList']:
                        value.append(m[i].as_long())
                    # print("strategy not sat, countexample is:",value)
                    ptK = ptK - 1
                    ptList.append(value)
                    # while ptK>0:
                    #     if len(value) == 1:
                    #         s.add(v1!=value[0])
                    #     elif len(value) == 2:
                    #         s.add(Or(v1!=value[0],v2!=value[1]))
                    #     elif len(value) ==3:
                    #         s.add(Or(v1!=value[0],v2!=value[1],v3!=value[2]))
                    #     if s.check() == sat:
                    #         m = s.model()
                    #         value =[]
                    #         for i in Game['varList']:
                    #             value.append(m[i].as_long())
                    #         print("not sat, countexample is:",value)
                    #         ptK = ptK - 1
                    #         ptList.append(value)
                    #     else:
                    #         print("There are no more counterexamples")
                    #         break
                    while ptK > 0:
                        pt = genPtSatFormula(pathFormula, ptList)
                        if pt == False:  # no more counterexamples
                            break
                        ptList.append(pt)
                        ptK = ptK - 1
                    print("Generate", ptk2, "countexamples:", ptList)
                    for pt in ptList:
                        pts.append(pt)
                        ptsOutput.append(genOutput(pt))
                    isSAT = False
                    print("==============================================\n")
                    break
                else:
                    winningStrategyTemp.append([winningStrategyPath, ActExe])
                    print("\t", path, "is a winning rule")
        elif DT == None:
            print("========== Generate countexamples ========")
            ptK = ptk2  # Number of counterexamples generated per round
            ptList = []
            while ptK > 0:
                pt = genPtSatFormula(pathFormula, ptList)
                if pt == False:  # There are no examples to generate
                    break
                ptList.append(pt)
                ptK = ptK - 1
            print(ptk2, " countexamples have generate:", ptList)
            for pt in ptList:
                pts.append(pt)
                ptsOutput.append(genOutput(pt))
            isSAT = False
            print("====================================")
        if pts == []:
            print("Misere terminal formula or generate winning formula may error")
            break
        if isSAT == True:
            print("\nThe T-label path formula", pathFormula, "can find partial winning strategy：")
            print("\t", tree2Act(DT))
            for i in winningStrategyTemp:
                winningStrategy.append(i)
            break

if exitFlag == False:
    winningStrategyTime = time.time() - startWinningStrategyTime
    print("\n---------------------------- Winning strategy  ---------------------------\n")
    for i in winningStrategy:
        print(i)
    print("The total running time:", round(winningStrategyTime, 2))
    sheet1.write(row, 4, str(winningStrategy))
    sheet1.write(row, 5, round(winningStrategyTime, 2))
    newwb.save(resultFile)
Thread1.cancel()
Thread2.cancel()

