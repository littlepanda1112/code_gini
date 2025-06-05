import sys
from antlr4 import *
import xlrd
from subfile.PDDLGrammarLexer import PDDLGrammarLexer
from subfile.PDDLGrammarParser import PDDLGrammarParser
from z3 import *
from MyVisitor import MyVisitor
from MyVisitor import game
from z3 import *
from opera import *
from xlutils.copy import copy
from copy import deepcopy as deepcopy
import time
import eventlet
import threading
import re


# ptk -- number of countexample in each round
# time_out1 -- Timeout interrupt
ptk = 3
time_out1 = 1200


pddlFile = sys.argv[1]
resultFile = sys.argv[2]
game_type = sys.argv[3]


# pddlFile = r"domain\1.Sub\1.1 Take-away\Take-away-5.pddl"
# resultFile=r"result.txt"
# game_type=r"normal"


gameName = pddlFile.split('\\')[-1][:-5]

print("#################################################################")
print("######################### Formalization #########################")
print("#################################################################")

print("gameName:\n\t", gameName)

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

v1 = Int("v1")
v2 = Int("v2")
v3 = Int("v3")
v1_next = Int("v1_next")
v2_next = Int("v2_next")
v3_next = Int("v3_next")


k = Int('k')
l = Int('l')
(k1, k2, k3) = Ints('k1 k2 k3')

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
           "transition_formula": eval(str(i[3]).replace('v1\'', 'v1_next').replace('v2\'', 'v2_next').replace('v3\'', 'v3_next'))}
    actions.append(one)

Game = {"Terminal_Condition": Terminal_Condition,
        "varList": varList,
        "actions": actions,
        "Constraint": Constarint,
        "var_num": game.objectsCount,
        "type": game_type,
        "appeal_constants": game.constantList}

print("Var List:", varList)
varListY = eval(str(varList).replace('v3', 'v3_next').replace(
    'v2', 'v2_next').replace('v1', 'v1_next'))
print("Var next list", varListY)


print("appeal constant", Game['appeal_constants'])

FunExg = {'Add': Add, 'Sub': Sub, 'Inc': Inc, 'Dec': Dec, 'Ge': Ge, 'ITE': ITE,
          'Gt': Gt, 'OR': OR, 'AND': AND, 'NOT': NOT, 'Equal': Equal, 'Mod': Mod,
          'Unequal': Unequal, 'v1': v1, 'v1_next': v1_next, 'Zero': Zero, 'One': One, 'ModTest': ModTest}
Z3FunExg = {'OR': z3OR, 'AND': z3AND}

p_vocabulary = [
    {'Input': ['Int', 'Int'], 'Output': 'Bool',
        'Function_name': 'Equal', 'arity': 2},
    {'Input': ['Int', 'Int'], 'Output': 'Bool',
     'Function_name': 'Unequal', 'arity': 2},
    {'Input': ['Int', 'Int'], 'Output': 'Bool',
     'Function_name': 'Ge', 'arity':2},
    {'Input': ['Int', 'Int'], 'Output': 'Bool',
     'Function_name': 'Gt', 'arity':2},
    {'Input': ['Int', 'Int', 'Int'], 'Output':'Bool', 'Function_name':'ModTest', 'arity':3}]
t_vocabulary = [
    {'Input': ['Int', 'Int'], 'Output':'Int',
        'Function_name':'Add', 'arity':2},
    {'Input': ['Int', 'Int'], 'Output': 'Int',
        'Function_name': 'Sub', 'arity':2},
]

ao_vocabulary = [{'Input': ['Bool', 'Bool'], 'Output': 'Bool', 'Function_name': 'OR', 'arity': 2},
                 {'Input': ['Bool', 'Bool'], 'Output': 'Bool', 'Function_name': 'AND', 'arity': 2}, ]


def enumerate():
    SigSet = []
    ExpSet = []
    SizeOneExps = []
    ItemsNum = []
    ItemsVar = []

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
    SigSetP = []
    ExpSetP = []
    while True:
        # print("size",li)
        for i in t_vocabulary:
            for size1 in range(1, li):
                for choose1 in ExpSet:
                    if choose1['size'] == size1:
                        for choose2 in ExpSet:
                            if choose2['size'] == li-size1:
                                if termination_sign:
                                    Thread1.cancel()
                                    print("Time out,about to exit the program")
                                    sheet1.write(
                                        row, 2, "time-out-")
                                    newwb.save(resultFile)
                                    sys.exit(0)
                                term = FunExg[i['Function_name']](
                                    choose1['Expression'], choose2['Expression'])
                                Goal1 = []
                                for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                    Goal1.append(
                                        FunExg[i['Function_name']](k1, h))
                                if Goal1 not in SigSet:
                                    SigSet.append(Goal1)
                                    i['outputData'] = Goal1
                                    ExpSet.append(
                                        {'Expression': term, 'Isnum': choose1['Isnum'] and choose2['Isnum'], 'outputData': Goal1, 'size': li})

        for i in p_vocabulary:
            if i['arity'] == 2:
                for size1 in range(1, li):
                    for choose1 in ExpSet:
                        if choose1['size'] == size1:
                            for choose2 in ExpSet:
                                if choose2['size'] == li-size1:
                                    if termination_sign:
                                        Thread1.cancel()
                                        print(
                                            "Time out,about to exit the program")
                                        sheet1.write(
                                            row, 2, "time-out-")
                                        newwb.save(resultFile)
                                        sys.exit(0)
                                    pred = FunExg[i['Function_name']](
                                        choose1['Expression'], choose2['Expression'])
                                    
                                    Goal1 = []
                                    for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                        Goal1.append(
                                            FunExg[i['Function_name']](k1, h))

                                    if Goal1 == ptsGoal:
                                        print(i['Function_name'],choose1['Expression'],choose2['Expression'],"li",li)
                                        return pred
                                    if Goal1 not in SigSetP:
                                        SigSetP.append(Goal1)
                                        i['outputData'] = Goal1
                                        ExpSetP.append(
                                            {'Expression': pred, 'outputData': Goal1, 'size': li})
            if i['arity'] == 3 and li >= 3:  # %=
                for size1 in range(1, li):
                    for choose1 in ExpSet:
                        if choose1['size'] == size1 and choose1['Isnum'] == False:
                            for size2 in range(1, li):
                                for choose2 in ExpSet:
                                    if choose2['size'] == size2 and choose2['Isnum'] and choose2['Expression'] > 0:
                                        for choose3 in ExpSet:
                                            if choose3['size'] == li-size1-size2 and choose3['Isnum'] and choose3['Expression'] < choose2['Expression']:
                                                try:
                                                    if termination_sign:
                                                        Thread1.cancel()
                                                        print(
                                                            "Time out,about to exit the program")
                                                        sheet1.write(
                                                            row, 2, "time-out-")
                                                        newwb.save(resultFile)
                                                        sys.exit(0)
                                                    pred = FunExg[i['Function_name']](
                                                        choose1["Expression"], choose2["Expression"], choose3["Expression"])
                                                    Goal1 = []
                                                    for k1, h, m in zip(choose1['outputData'], choose2['outputData'], choose3['outputData']):
                                                        Goal1.append(
                                                            FunExg[i['Function_name']](k1, h, m))
                                                    if Goal1 == ptsGoal:
                                                        print(i['Function_name'],choose1['Expression'],choose2['Expression'])
                                                        return pred
                                                    if Goal1 not in SigSetP:
                                                        SigSetP.append(Goal1)
                                                        i['outputData'] = Goal1

                                                        ExpSetP.append(
                                                            {'Expression': pred, 'outputData': Goal1, 'size': li})
                                                except ZeroDivisionError:
                                                    pass
        if li >= 4:
            for i in ao_vocabulary:
                for size1 in range(1, li):
                    for choose1 in ExpSetP:
                        if choose1["size"] == size1:
                            for choose2 in ExpSetP:
                                if choose2["size"] == li+1-size1 and choose1 != choose2:
                                    if termination_sign:
                                        Thread1.cancel()
                                        print(
                                            "Time out,about to exit the program")
                                        sheet1.write(
                                            row, 2, "time-out-")
                                        newwb.save(resultFile)
                                        sys.exit(0)
                                    pred = Z3FunExg[i['Function_name']](
                                        choose1['Expression'], choose2['Expression'])

                                    Goal1 = []
                                    for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                        Goal1.append(
                                            FunExg[i['Function_name']](k1, h))
                                    if Goal1 == ptsGoal:
                                        print(i['Function_name'],choose1['Expression'],choose2['Expression'],"li",li)
                                        return pred
                                    if Goal1 not in SigSetP:
                                        SigSetP.append(Goal1)
                                        i['outputData'] = Goal1
                                        ExpSetP.append(
                                            {'Expression': pred, 'outputData': Goal1, 'size': li})
        li += 1


def enumerateK():
    SigSet = []
    ExpSet = []
    SizeOneExps = []
    ItemsNum = []
    ItemsVar = []

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
            if Goal1 == ptsGoal:
                return i['Expression']
            if Goal1 not in SigSet:
                SigSet.append(Goal1)
                i['outputData'] = Goal1
                ExpSet.append(i)

        else:
            if i['Expression'] == v1:
                for pt in pts:
                    Goal1.append(pt[0])
                if Goal1 == ptsGoal:
                    return i['Expression']
                if Goal1 not in SigSet:
                    SigSet.append(Goal1)
                    i['outputData'] = Goal1
                    ExpSet.append(i)
                    if Goal1 == ptsGoal:
                        return i['Expression']
            if i['Expression'] == v2:
                for pt in pts:
                    Goal1.append(pt[1])
                if Goal1 == ptsGoal:
                    return i['Expression']
                if Goal1 not in SigSet:
                    SigSet.append(Goal1)
                    i['outputData'] = Goal1
                    ExpSet.append(i)
            if i['Expression'] == v3:
                for pt in pts:
                    Goal1.append(pt[2])
                if Goal1 == ptsGoal:
                    return i['Expression']
                if Goal1 not in SigSet:
                    SigSet.append(Goal1)
                    i['outputData'] = Goal1
                    ExpSet.append(i)
    li = 2
    while True:
        # print("size",li)
        for i in t_vocabulary:
            for size1 in range(1, li):  # add(num,num)
                for choose1 in ExpSet:
                    if choose1['size'] == size1:
                        for choose2 in ExpSet:
                            if choose2['size'] == li-size1:
                                if termination_sign:
                                    Thread1.cancel()
                                    print("Time out,about to exit the program")
                                    sheet1.write(
                                        row, 4, "time-out")
                                    newwb.save(resultFile)
                                    sys.exit(0)
                                term = FunExg[i['Function_name']](
                                    choose1['Expression'], choose2['Expression'])
                                Goal1 = []
                                for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                    Goal1.append(
                                        FunExg[i['Function_name']](k1, h))
                                if Goal1 == ptsGoal:
                                    return term
                                if Goal1 not in SigSet:
                                    SigSet.append(Goal1)
                                    i['outputData'] = Goal1
                                    ExpSet.append(
                                        {'Expression': term, 'Isnum': choose1['Isnum'] and choose2['Isnum'], 'outputData': Goal1, 'size': li})

        li += 1


"""global transition formula"""
global_transition_formula = "Or("
for i in Game["actions"]:
    if i['action_parameter'] != []:
        temp = "["
        for j in i['action_parameter']:
            temp = temp+str(j)+","
        temp = temp[:-1]
        temp += "],"
        global_transition_formula = global_transition_formula + \
            "Exists("+temp+str(i["transition_formula"])+"),"
    else:
        global_transition_formula = global_transition_formula + \
            str(i["transition_formula"])+","

global_transition_formula = global_transition_formula[:-1]
global_transition_formula = global_transition_formula+")"

print("Global transition formula:\n\t", global_transition_formula)
global_transition_formula = simplify(eval(global_transition_formula))


position = []
if Game['var_num'] == 1:
    for i in range(0, 100):
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
elif Game['var_num'] == 4:
    for i in range(0, 100):
        position.append([])
        for i1 in range(0, 100):
            position[i].append([])
            for i2 in range(0, 100):
                position[i][i1].append([])
                for i3 in range(0, 100):
                    position[i][i1][i2].append("illegal")

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
                position[a] = True  # normal
            else:
                position[a] = False  # misere
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


def isLossingState(*v):
    if termination_sign:
        Thread1.cancel()
        print("Time out,about to exit the program")
        sheet1.write(row, 2, "time-out-")
        newwb.save(resultFile)
        sys.exit(0)
    # print("Insert",v," into isLossingstate:")
    for i in v:  # default position < 100
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
                    position[i[0]] = isLossingState(i[0])
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
        for x in range(0, v[0]+1):
            for y in range(0, v[1]+1):
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
                        temp.append(
                            [m[v1_next].as_long(), m[v2_next].as_long()])
                    else:
                        break
                # print('Transilate 773 of',x,y,":\t",temp) # 438 [[2, 1], [2, 0], [1, 1]]
                is_losing = True
                s = Solver()
                s.add(Game["Constraint"])
                s.add(v1 == x, v2 == y)
                if (s.check() == unsat):
                    continue
                for i in temp:
                    if (position[i[0]][i[1]] == 'illegal'):
                        position[i[0]][i[1]] = isLossingState(i[0], i[1])
                for i in temp:
                    is_losing = is_losing and not position[i[0]][i[1]]
                if (is_losing):
                    position[x][y] = True
                else:
                    position[x][y] = False
        # print("the state ：",v,"is",position[v[0]][v[1]])
        return position[v[0]][v[1]]
    elif len(v) == 3:
        if position[v[0]][v[1]][v[2]] != 'illegal':  #
            return position[v[0]][v[1]][v[2]]
        for x in range(0, v[0]+1):
            for y in range(0, v[1]+1):
                for z in range(0, v[2]+1):
                    if (position[x][y][z] != 'illegal'):
                        continue
                    temp = []
                    while (True):
                        s = Solver()
                        s.add(global_transition_formula)
                        s.add(Game["Constraint"])
                        s.add(v1 == x, v2 == y, v3 == z)
                        for i in temp:
                            s.add(
                                Or(v1_next != i[0], v2_next != i[1], v3_next != i[2]))
                        if s.check() == sat:
                            m = s.model()
                            temp.append(
                                [m[v1_next].as_long(), m[v2_next].as_long(), m[v3_next].as_long()])
                        else:
                            break
                    # print('438',temp)
                    is_losing = True
                    s = Solver()
                    s.add(Game["Constraint"])
                    s.add(v1 == x, v2 == y, v3 == z)
                    if (s.check() == unsat):
                        continue
                    for i in temp:
                        if (position[i[0]][i[1]][i[2]] == 'illegal'):
                            position[i[0]][i[1]][i[2]] = isLossingState(
                                i[0], i[1], i[2])
                    for i in temp:
                        is_losing = is_losing and not position[i[0]
                                                               ][i[1]][i[2]]
                    if (is_losing):
                        position[x][y][z] = True
                    else:
                        position[x][y][z] = False
        return position[v[0]][v[1]][v[2]]


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

                        boolTemp = isLossingState(r1)
                        boolTemp2 = eval(str(e).replace(
                            str(v1), str(r1)))
                        s = Solver()
                        if boolTemp == False:
                            s.add(True, boolTemp2)
                            if (s.check() == sat):
                                return [r1]
                        elif boolTemp == True:
                            s.add(True, boolTemp2)
                            if (s.check() == unsat):
                                return [r1]
                    else:
                        continue
            i += 1
    elif Game["var_num"] == 2:
        i = 1
        if i > 100:
            example_run_out_sign = True
            return 'illegal'
        while (True):
            for r1 in range(0, i+1):
                r2 = i-r1  #
                # print("828",r1,r2)
                if [r1, r2] not in ptList and [r1, r2] not in pts:
                    s = Solver()
                    s.add(Game["Constraint"])
                    s.add(v1 == r1, v2 == r2)
                    if s.check() == sat:
                        # print("find example:", r1, r2)
                        return [r1, r2]
                        # print(expr)
                        # print(r1, r2)
                        boolTemp = isLossingState(r1, r2)
                        boolTemp2 = eval(str(e).replace(
                            str(v2), str(r2)).replace(str(v1), str(r1)))
                        s = Solver()
                        if boolTemp == False:
                            s.add(True, boolTemp2)
                            if (s.check() == sat):
                                return [r1, r2]
                        elif boolTemp == True:
                            s.add(True, boolTemp2)
                            if (s.check() == unsat):
                                return [r1, r2]
                    else:
                        continue
            i = i+1
    elif Game["var_num"] == 3:
        i = 1
        while True:
            if i > 100:
                example_run_out_sign = True
                return 'illegal'
            for r1 in range(0, i+1):
                for r2 in range(0, i-r1+1):
                    r3 = i-r1-r2
                    if [r1, r2, r3] not in ptList and [r1, r2, r3]not in pts:
                        s = Solver()
                        s.add(Game["Constraint"])
                        s.add(v1 == r1, v2 == r2, v3 == r3)
                        if s.check() == sat:
                            return [r1, r2, r3]
                            boolTemp = isLossingState(r1, r2, r3)
                            boolTemp2 = eval(str(e).replace(
                                str(v2), str(r2)).replace(str(v3), str(r3)).replace(str(v1), str(r1)))
                            s = Solver()
                            if boolTemp == False:
                                s.add(True, boolTemp2)
                                if (s.check() == sat):
                                    return [r1, r2, r3]
                            elif boolTemp == True:
                                s.add(True, boolTemp2)
                                if (s.check() == unsat):
                                    return [r1, r2, r3]
                        else:
                            continue
            i = i+1


def countSize(var, varpool):
    if is_number(var):
        var = float(var)
    if type(var) != type(1.0):
        return 1
    elif var in varpool:
        return 1
    else:
        return 1+countSize(var, expandpool(varpool))


def expandpool(varpool):
    p = []
    for i in varpool:
        p.append(i)
    # while i < len(varpool):
    i = 0
    j = 0

    while i < len(varpool):

        while j < len(varpool):

            if varpool[i]+varpool[j] not in p:
                p.append(varpool[i]+varpool[j])
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
    str1 = str1.replace('*', '-').replace(',', '-').replace('+', '-').replace('<=', '-').replace('>=', '-').replace(
        '<', '-').replace('>', '-').replace('==', '-').replace('%', '-').replace('(', '').replace(')', '')
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
        str1 = str1[str1.find('-')+1:len(str1)]
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


def outRange(*v):
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
    if outRange(*value) != 'illegal':
        print("countexample：", value)
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
    #         print("not sat countexample is:",value)
    #         ptK = ptK - 1
    #         ptList.append(value)
    #     else:
    #         print("no more countexxample")
    #         break
    while ptK > 0:
        pt = FindCountExample(ptList)
        # print("find countExample:",pt)
        if pt == 'illegal':
            return ptList
        if outRange(*pt) == 'illegal':
            continue
        else:
            ptK -= 1
            ptList.append(pt)
    print(ptk, "example generate:\t", ptList)
    return ptList


def unkownfindstate(ptk):
    ptK = ptk
    ptList = []
    while True:
        pt = FindCountExample(ptList)
        if pt == 'illegal':
            return ptList
        if outRange(*pt) == 'illegal':
            continue
        else:
            ptK -= 1
            ptList.append(pt)
            if (ptK == 0):
                print("InitializeStates", ptk, "example generate:\t", ptList)
                return ptList


newwb = copy(oldwb)
sheet1 = newwb.get_sheet(0)
sheet1.write(row, 0, gameName)
newwb.save(resultFile)
2
print("\n")
print("####################################################################")
print("################# Learning winning formula #########################")
print("####################################################################")
print("\n")

start_winning_formula_time = time.time()
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


e = v1 == v1
while True:
    if termination_sign:
        Thread1.cancel()
        print("Time out,about to exit the program")
        sheet1.write(row, 2, "time-out-")
        newwb.save(resultFile)
        sys.exit(0)
    print("the set of states", pts)
    # print("the label of states",ptsGoal)
    last_e = e
    e = enumerate()
    print("Enumerate formula", e)
    e1 = eval(str(e).replace("v2", "v2_next").replace(
        "v3", "v3_next").replace("v1", "v1_next"))
    if (Game["type"] == "normal"):
        con1 = And(Game["Terminal_Condition"], Not(e))
        con2 = And(Game["Constraint"], Not(e), ForAll(
            varListY, Or(Not(global_transition_formula), Not(e1))))
        con3 = And(Game["Constraint"], e, Exists(
            varListY, And(global_transition_formula, e1)))
    elif (Game["type"] == "misere"):
        con1 = And(Game["Terminal_Condition"], e)
        con2 = And(Game["Constraint"], Not(e), Not(Game["Terminal_Condition"]), ForAll(
            varListY, Implies(global_transition_formula, Not(e1))))
        con3 = And(Game["Constraint"], e, Exists(
            varListY, And(global_transition_formula, e1)))
    s = Solver()
    s.add(con1)
    s.set('timeout', 60000)
    if (s.check() == sat):
        print("verify the formula not sat the constraint of winning formula")
        examples = satfindstate(ptk)
    else:
        # print("condition1 sat")
        s = Solver()
        s.add(con2)
        s.set('timeout', 60000)
        if (s.check() == sat):
            print("verify the formula not sat the constraint of winning formula")
            examples = satfindstate(ptk)
        else:
            # print("condition2 sat")
            s = Solver()
            s.add(con3)
            s.set('timeout', 60000)
            if (s.check() == sat):
                print("verify the formula not sat the constraint of winning formula")
                examples = satfindstate(ptk)
            else:
                # print("condition3 sat")
                losing_formula = e
                print("the formula sat the constraint of winning formula")
                print(
                    '-----------------------------------------------------------------------------')
                winning_formula = simplify(Not(losing_formula))
                print("The Winning formula of this game is:", winning_formula)
                sizeFormula = GetSize(gameName, str(winning_formula))
                generate_winning_formula_time = (
                    time.time() - start_winning_formula_time)
                print("Time to generate the winning formula:",
                      generate_winning_formula_time)
                generate_winning_formula_time = str(
                    round(generate_winning_formula_time, 2))

                sheet1.write(row, 1, str(simplify(Not(losing_formula))))
                sheet1.write(row, 2, generate_winning_formula_time)
                sheet1.write(row, 3, sizeFormula)
                newwb.save(resultFile)

                break
    if Game["var_num"] == 1:
        for i in examples:
            if i[0] not in pts:
                pts.append([i[0]])
                ptsGoal.append(isLossingState(i[0]))
    elif Game["var_num"] == 2:
        for i in examples:
            if [i[0], i[1]] not in pts:
                pts.append([i[0], i[1]])
                ptsGoal.append(isLossingState(i[0], i[1]))
    elif Game["var_num"] == 3:
        for i in examples:
            if [i[0], i[1], i[2]] not in pts:
                pts.append([i[0], i[1], i[2]])
                ptsGoal.append(isLossingState(i[0], i[1], i[2]))
    elif Game["var_num"] == 4:
        for i in examples:
            if [i[0], i[1], i[2], i[3]] not in pts:
                pts.append([i[0], i[1], i[2], i[3]])
                ptsGoal.append(isLossingState(i[0], i[1], i[2], i[3]))

flag_para = True
for i in actions:
    if len(i["action_parameter"]) > 1 or len(i["action_parameter"]) == 0:
        flag_para == False

if flag_para == False:
    sheet1.write(row, 4, "cannot solve")
    newwb.save(resultFile)
    Thread1.cancel()
    sys.exit()

winning_formula = Not(losing_formula)
winning_formula_Y = eval(str(winning_formula).replace(
    "v2", "v2_next").replace("v3", "v3_next").replace("v1", "v1_next"))


def refine_the_winning_formula(Losing_formula):
    try:
        C = str(Losing_formula)
        # print('612',C)    v1 == v2 + 1
        C = C.replace(' ', '')  # v1==v2+1
        Ct = []
        # gou'zhao
        if (C.find('And') == -1 and C.find('Or') == -1):
            if (C.find('==') != -1 and (type(eval(C[(C.find('==') + 2):])) == type(1)) and C.find('%') == -1):
                Ct = []
                Ct.append(C.replace('==', '<'))
                Ct.append(C.replace('==', '>'))
            elif (C.find('==') != -1 and (type(eval(C[(C.find('==') + 2):])) == type(v1)) and C.find('%') == -1):
                Ct = []
                Ct.append(C.replace('==', '<'))
                Ct.append(C.replace('==', '>'))
            # a%b==c
            elif (C.find('%') != -1 and (type(eval(C[(C.find('==') + 2):])) == type(1))):
                Ct = []
                num = eval(C[(C.find('%') + 1):C.find('==')]) - 1  # b
                num_original = eval(C[(C.find('==') + 2):])  # c
                while (num >= 0):
                    if (num != num_original):  # b!=c and b>=0
                        C = C[:C.find('==') + 2]
                        C = C + str(num)     # a+b
                        Ct.append(C)
                        # Ct.append(C.replace(C[(C.find('==') + 2):], str(num)))
                    num = num - 1
        else:
            if ((C.find('v1') != -1 and C.find('v2') == -1) or (C.find('v1') == -1 and C.find('v2') != -1)):
                if (C.find('%') != -1 and (type(eval(C[(C.find('==') + 2):C.find(',')])) == type(1)) and C.find(
                        'Or') != -1):
                    Ct = []
                    num = eval(C[(C.find('%') + 1):C.find('==')]) - 1
                    prnum = []
                    pre = C.find('==')
                    while (pre != -1):
                        prnum.append(eval(C[pre + 2]))
                        pre = C.find('==', pre + 1)
                    # print(prnum)
                    while (num >= 0):
                        if (num not in prnum):
                            Ct.append(C[C.find('v1'):C.find(',')].replace(
                                C[C.find('==') + 2], str(num)))
                        num = num - 1
            else:
                if (C.find('And') != -1):
                    C1 = C
                    C1 = C1.replace('And', 'Or')
                    C1 = C1.replace('==', '!=')
                    C1 = C1.replace('Or(', '')
                    C1 = C1.replace(')', '')
                    Ct = C1.split(',')
        # print("Covers of this game:", Ct)
        refinement = []
        for i in Ct:
            i = eval(i)
            refinement.append(i)
        return refinement
    except:
        sheet1.write(row, 4, "split error")
        newwb.save(resultFile)
        Thread1.cancel()
        sys.exit()


def generatePt(cover, pts, action_constraint):
    s = Solver()
    s.add(cover)
    s.add(action_constraint)
    if (Game["var_num"] == 1):
        for pt in pts:
            s.add(Or(v1 != pt[0]))
    if (Game["var_num"] == 2):
        for pt in pts:
            s.add(Or(v1 != pt[0], v2 != pt[1]))
    if (Game["var_num"] == 3):
        for pt in pts:
            s.add(Or(v1 != pt[0], v2 != pt[1], v3 != pt[2]))

    s.check()
    m = s.model()
    if (Game["var_num"] == 1):
        return [m[v1].as_long()]
    if (Game["var_num"] == 2):
        return [m[v1].as_long(), m[v2].as_long()]
    if (Game["var_num"] == 3):
        return [m[v1].as_long(), m[v2].as_long(), m[v3].as_long()]


def findK(action_precondition, action_transition_formula, action_constraint, pt):
    s = Solver()
    s.add(Not(winning_formula_Y))
    s.add(action_precondition)
    s.add(action_transition_formula)
    s.add(action_constraint)
    s.add(v1 == pt[0])
    if (Game["var_num"] == 2):
        s.add(v2 == pt[1])
    if (Game["var_num"] == 3):
        s.add(v2 == pt[1])
        s.add(v3 == pt[2])

    if (s.check() == sat):
        m = s.model()
        return m[k].as_long()
    else:
        return "no suitable k"


print("\n")
print("#####################################################################")
print("################# Learning winning strategy #########################")
print("#####################################################################")
print("\n")

start_refine = time.time()
winningStrategy = []
refinement = refine_the_winning_formula(losing_formula)
flag_strategy = True
print("the splitting of winningformula", refinement)

for cover in refinement:
    print("----------------------test the splitting :",
          cover, "--------------------")
    s = Solver()
    s.add(cover)
    s.add(Game["Constraint"])
    if (s.check() == unsat):
        continue
    flagAct = False
    for action in actions:
        pts.clear()
        ptsGoal.clear()
        print("enumerate expression of:", action["action_name"])
        while (True):
            if termination_sign:
                Thread1.cancel()
                print("Time out,about to exit the program")
                sheet1.write(row, 4, "time-out-")
                newwb.save(resultFile)
                sys.exit(0)
            print("the set of states:", pts)
            # print(ptsGoal)
            e = enumerateK()
            print("enumerate the expression:", e)
            s = Solver()
            # if (str(e) != str(last_e)):
            action_temp = deepcopy(action)
            if (str(action_temp).find("k") != -1):
                action_temp = eval(
                    str(action_temp).replace("k", '('+str(e)+')'))
            if Game["type"] == "normal":
                s.add(Not(Implies(And(cover, Game["Constraint"]), And(action_temp["precondition"],
                                                                      ForAll(varListY, Implies(action_temp["transition_formula"], Not(winning_formula_Y)))))))
            else:
                s.add(Not(Implies(And(cover, Game["Constraint"], Not(Game["Terminal_Condition"])), And(action_temp["precondition"],
                                                                                                       ForAll(varListY, Implies(action_temp["transition_formula"], Not(winning_formula_Y)))))))

            if (s.check() == unsat):
                print("the semi ground acton",
                      action["action_name"]+"("+str(e)+")", "sat the splitting")
                winningStrategy.append(
                    [cover, action["action_name"]+"("+str(e)+")"])
                flagAct = True
                break
            else:
                num1 = 0
                num2 = 0
                m = s.model()
                pt = [m[v1].as_long()]
                if (Game["var_num"] == 2):
                    pt = [m[v1].as_long(), m[v2].as_long()]
                if Game["var_num"] == 3:
                    pt = [m[v1].as_long(), m[v2].as_long(), m[v3].as_long()]

                # print("the countexample",pt)
                s_tem = Solver()
                s_tem.add(cover)
                s_tem.add(v1 == pt[0])
                if (Game["var_num"] == 2):
                    s_tem.add(v2 == pt[1])
                if (Game["var_num"] == 3):
                    s_tem.add(v2 == pt[1])
                    s_tem.add(v3 == pt[2])

                # print(s_tem.check())
                if (s_tem.check() != sat):
                    pt = generatePt(cover, pts, Game["Constraint"])
                result = findK(
                    action["precondition"], action["transition_formula"], Game["Constraint"], pt)
                if result == "no suitable k":
                    print("794no suitable k")
                    break
            # else:
            #     print('two expresion equal')
            #     pt = generatePt(cover, pts, Game["Constraint"])
            #     result = findK(action["precondition"], action["transition_formula"], Game["Constraint"], pt)
            #     if result == "no suitable k":
            #         print("794no suitable k")
            #         break
            if pt not in pts:
                pts.append(pt)
                ptsGoal.append(result)
    if flagAct == False:
        flag_strategy = False
        break
winningStrategyTime = (time.time() - start_refine)
print("--------------------------------------------------------------------------")
print("the winning strategy:", winningStrategy)
print("time use:", winningStrategyTime)
if flag_strategy:
    sheet1.write(row, 4, str(winningStrategy))
    sheet1.write(row, 5, str(round(winningStrategyTime, 2)))
    newwb.save(resultFile)
else:
    sheet1.write(row, 4, "have split cannot find action")
    newwb.save(resultFile)
Thread1.cancel()
