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
# 读取命令行参数
# 读取 PDDL 文件路径
pddlFile = sys.argv[1]
# 结果文件路径
resultFile = sys.argv[2]
# 游戏类型
game_type = sys.argv[3]

# 默认启发式方法：信息增益
heuristical_way = "InfoGain"
# 默认最小节点选择策略
choice_minnode = "n"

# 学习方法
choice_method = sys.argv[4]
if choice_method == "ID3":  # ID3方法的具体启发式（InfoGain/Gini）
    heuristical_way = sys.argv[5]
elif choice_method == "Incre":
    choice_minnode = sys.argv[5]    # 增量学习的最小节点策略


# print(sys.argv[2])

# pddlFile = r"domain\1.Sub\1.1 Take-away\Take-away-30.pddl"
# resultFile = r".\result.xls"
# game_type = "normal" #normal, misere
# heuristical_way = "Gini"  # InfoGain, Gini

# Game variable set
# 状态变量（当前状态）
v1 = Int("v1")
v2 = Int("v2")
v3 = Int("v3")
# 状态变量（下一状态）
v1_next = Int("v1_next")
v2_next = Int("v2_next")
v3_next = Int("v3_next")
# Action parameters
# 动作参数（如取子游戏中的取子数量）
k = Int('k')
l = Int('l')
(k1, k2, k3) = Ints('k1 k2 k3')

# ptk ptk2 -- number of countexample in each round
# time_out -- Timeout interrupt
# 每轮生成的反例数量
ptk = 3
# 第二轮反例数量
ptk2 = 
# 第一阶段超时时间（秒）
time_out1 = 1200
# 第二阶段超时时间（秒）
time_out2 = 1200

# # 从路径提取游戏名称
gameName = pddlFile.split('\\')[-1][:-5]
print("use method:",choice_method,"game type:",game_type)
print("#################################################################")
print("######################### Formalization #########################")
print("#################################################################")
print("  ")
print("GameName:\n\t", gameName)
# 读取结果Excel文件
oldwb = xlrd.open_workbook(resultFile, encoding_override='utf-8')
sheet1 = oldwb.sheet_by_index(0)
row = sheet1.nrows  # 获取已有行数

# 4. 读取 PDDL 文件并解析
# 使用 ANTLR 库对 PDDL 文件进行词法和语法分析，并通过自定义的MyVisitor类遍历语法树，提取游戏信息。
# ANTLR 解析：将 PDDL 文本转换为结构化数据（如状态变量、动作列表）。
# MyVisitor：自定义类，用于从语法树中提取博弈规则（如终止条件、动作效果）。

input_stream = FileStream(pddlFile)
# 词法分析
lexer = PDDLGrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# 语法分析
parser = PDDLGrammarParser(token_stream)
# 生成语法树
tree = parser.domain()
# 自定义访问器
visitor = MyVisitor()
# 遍历语法树，提取游戏信息
visitor.visit(tree)

# 5. 构建游戏描述字典
# 将解析得到的游戏信息存储在Game字典中
# 终止条件（如"所有堆为空"）
Terminal_Condition = game.tercondition
# 状态约束（如"筹码数≥0"）
Constarint = game.constraint
# 状态变量列表
varList = []
for i in game.var_list:
    varList.append(i)
actions = []

# 动作表示：每个动作包含名称、参数、前置条件和转移公式（如执行动作后状态如何变化）。
# 状态转移：将 PDDL 中的v1'（下一状态）替换为v1_next，便于符号计算。
# 解析每个动作（如"从堆中取k个筹码"）
for i in game.action_list:
    one = {"action_name": i[0],     # 动作名称 
           "action_parameter": i[1],        # 动作参数（如k）
           "precondition": i[2],        # 前置条件（如"堆中筹码数≥k"）
           "transition_formula": eval(      # 状态转移公式
               str(i[3]).replace('v1\'', 'v1_next').replace('v2\'', 'v2_next').replace('v3\'', 'v3_next'))}
    actions.append(one)

# 构建完整的游戏描述
Game = {"Terminal_Condition": Terminal_Condition,
        "varList": varList,
        "actions": actions,
        "Constraint": Constarint,
        "var_num": game.objectsCount,        # 状态变量数量
        "type": game_type,      # 游戏类型
        "appeal_constants": game.constantList}      # 常量列表（如最大取子数）

print("Var List:", varList)
varListY = eval(str(varList).replace('v3', 'v3_next').replace('v2', 'v2_next').replace('v1', 'v1_next'))
print("Var next list", varListY)

print("Appeal constant", Game['appeal_constants'])

"""=============================================================================="""

# 6. 定义词汇表和函数映射
# 谓词：用于构建条件表达式（如Equal(v1, 0)表示 "v1 等于 0"）。
# 项：用于构建算术表达式（如Add(v1, k)表示 "v1 加 k"）。
# FunExg：将字符串函数名映射到实际的计算函数，便于动态调用。

# 定义谓词和项的词汇表，以及函数名到实际函数的映射。
# 定义了谓词（关系）的词汇表，包括相等 (Equal)、大于等于 (Ge)、大于 (Gt) 等关系。
p_vocabulary = [{'Input': ['Int', 'Int'], 'Function_name': 'Equal', 'arity': 2},
                {'Input': ['Int', 'Int'], 'Function_name': 'Ge', 'arity': 2},
                {'Input': ['Int', 'Int'], 'Function_name': 'Gt', 'arity': 2},
                {'Input': ['Int', 'Int', 'Int'], 'Function_name': 'ModTest', 'arity': 3}]

# 定义了项（函数）的词汇表，包括加法 (Add)、减法 (Sub) 等函数
t_vocabulary = [{'Input': ['Int', 'Int'], 'Function_name': 'Add', 'arity': 2},
                {'Input': ['Int', 'Int'], 'Function_name': 'Sub', 'arity': 2}, ]

# 函数名到实际函数的映射（如"Add"映射到Add函数）
FunExg = {'Add': Add, 'Sub': Sub, 'Inc': Inc, 'Dec': Dec, 'Ge': Ge, 'ITE': ITE,
          'Gt': Gt, 'OR': OR, 'AND': AND, 'NOT': NOT, 'Equal': Equal, 'Mod': Mod,
          'Unequal': Unequal, 'v1': v1, 'v1_nwxt': v1_next, 'Zero': Zero, 'One': One, 'ModTest': ModTest}


# Cache interResult of enumerat
# 缓存枚举过程中的中间结果
class InterResult:
    def __init__(self, expSet, sigSet) -> None:
        self.SigSet = sigSet    # 签名集合
        self.ExpSet = expSet    # 表达式集合


interResultPred = InterResult("", "")   # 谓词中间结果
interResultTerm = InterResult("", "")   # 项中间结果

# 决策树节点定义
class TreeNode:
    def __init__(self, x):
        self.val = x    # 节点值（如谓词表达式）
        self.left = None     # 左子树
        self.right = None   # 右子树

# 枚举参数（控制表达式生成的复杂度）
nextTermAdd = 5     # 加法项的最大复杂度
nextTermSub = 5     # 减法项的最大复杂度
predAdd = 4     # 谓词中加法的最大复杂度
preSub = 4      # 谓词中减法的最大复杂度
predSize = 7        # 谓词的最大大小

"""Enumerate atomic formulas by size"""
# 定义枚举函数
# 枚举原子公式，根据不同的大小和标志位生成谓词集合。
# 函数生成最大规模为 MaxSize 的所有谓词
def enumeratePredicate(MaxSize, DTFlag):
    global interResultPred
    # 存储表达式的输出数据（对每个点的计算结果）
    SigSet = []
    # 存储生成的表达式及其属性
    ExpSet = []
    # 存储大小为1的表达式（基础元素）
    SizeOneExps = []
    # 存储所有表达式
    Items = []
    # 存储数值类型的表达式
    ItemsNum = []
    # 存储变量类型的表达式
    ItemsVar = []

    # 决策树模式下，初始化基础表达式
    # DTFlag：若为 True，从头生成基础表达式；否则复用缓存结果。
    if DTFlag:
        # SizeOneExps：包含常数（0、1）、变量（v1、v2、v3）和游戏中的常量（如最大取子数）。
        # SigSet：存储表达式的输出模式（如 [1,1,1] 表示对所有点输出 1），用于去重。
        SizeOneExps.append({'Expression': 0, 'Isnum': True, 'size': 1})
        SizeOneExps.append({'Expression': 1, 'Isnum': True, 'size': 1})
        SizeOneExps.append({'Expression': v1, 'Isnum': False, 'size': 1})
        
        # # 添加游戏中的常量（如最大取子数）
        for i in Game["appeal_constants"]:
            SizeOneExps.append({'Expression': eval(i), 'Isnum': True, 'size': 1})
        
        # 根据游戏变量数量添加v2、v3
        if Game["var_num"] == 2:
            SizeOneExps.append({'Expression': v2, 'Isnum': False, 'size': 1})
        elif Game["var_num"] == 3:
            SizeOneExps.append({'Expression': v2, 'Isnum': False, 'size': 1})
            SizeOneExps.append({'Expression': v3, 'Isnum': False, 'size': 1})
        
        # 为每个基础表达式计算在所有点上的输出数据
        for i in SizeOneExps:
            # 存储表达式在每个点上的输出
            Goal1 = []
            # 数值类型（如常数）
            if (i['Isnum']):
                for num in range(len(pts)):
                    Goal1.append(i['Expression'])
                if Goal1 not in SigSet:
                    SigSet.append(Goal1)
                    i['outputData'] = Goal1
                    ExpSet.append(i)
            # 变量类型（如v1、v2）
            else:
                if i['Expression'] == v1:
                    for pt in pts:
                        Goal1.append(pt[0])
                    # 去重：若输出数据未出现过，则添加到集合中
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

    # 初始表达式大小               
    li = 2
    # 非决策树模式，复用缓存结果
    if DTFlag == False:
        SigSet = interResultPred.SigSet
        ExpSet = interResultPred.ExpSet
        li = MaxSize
    # print("The maximum number of predicate items enumerated",MaxSize)
    # 逐层生成更大规模的表达式
    while li <= MaxSize:
        # 检查超时标志
        if termination_sign:
            print("Time out,about to exit the program")
            sheet1.write(row, 2, "time-out-1200s")
            newwb.save(resultFile)
            sys.exit(0)
        
        # # 遍历项词汇表（如Add、Sub）生成新表达式
        for i in t_vocabulary:
            # 处理加法表达式
            if i['Function_name'] == 'Add':
                # 限制加法表达式的最大复杂度
                if li <= predAdd:
                    # 第一个操作数的大小
                    # 生成 var + var 或 var + num 形式的表达式
                    for size1 in range(1, li):
                        for choose1 in ExpSet:
                            if choose1['size'] == size1 and choose1['Isnum'] == False:
                                for choose2 in ExpSet:
                                    if choose2['size'] == li - size1:
                                        term = FunExg[i['Function_name']](
                                            choose1['Expression'], choose2['Expression'])
                                        
                                        # 计算表达式在所有点上的输出
                                        Goal = []
                                        for k1, h in zip(choose1['outputData'], choose2['outputData']):
                                            Goal.append(
                                                FunExg[i['Function_name']](k1, h))
                                        # 去重：若输出模式未出现过，则添加
                                        if Goal not in SigSet:
                                            SigSet.append(Goal)
                                            i['outputData'] = Goal
                                            ExpSet.append(
                                                {'Expression': term, 'Isnum': False, 'outputData': Goal, 'size': li})
                # 生成 num + num 形式的表达式
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
            # 处理减法表达式
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
        # 增加表达式大小，继续生成
        li += 1 

    # 缓存结果，便于下次复用
    interResultPred = InterResult(ExpSet, SigSet)

    # 按类型分类表达式
    for i in ExpSet:
        Items.append(i['Expression'])
        if i['Isnum']:
            ItemsNum.append(i)      # 数值类型
        else:
            ItemsVar.append(i)      # 变量类型
    # print("Items set generate atom formula:\n\t", Items)

    # 谓词公式生成（原子条件）
    # 存储谓词的输出模式
    predGoal = []
    # # 遍历谓词词汇表（如Equal、Ge、Gt、ModTest）
    for i in p_vocabulary:
        # 二元谓词（如v1 > v2）
        if i['arity'] == 2:
            # 生成 var op var 形式的谓词
            # 第一个操作数为变量
            for choose1 in ItemsVar:
                # 第二个操作数为变量
                for choose2 in ItemsVar:
                    # 避免重复（如不生成 v1 > v1）
                    if choose2 != choose1 and choose2["size"] + choose1["size"] <= predSize:
                        # if choose2["size"] <= MaxSize+1-choose1["size"]:#var1+var2 <= maxsize+1
                        tempPredicate = FunExg[i['Function_name']](
                            choose1['Expression'], choose2['Expression'])
                        # 过滤无效谓词（如恒为True或False的表达式）
                        if str(tempPredicate) != 'False' and str(tempPredicate) != 'True':
                            # 计算谓词在所有点上的输出（True/False）
                            goal = []
                            for pt in pts:
                                # 调用 ptSatPred 判断点是否满足谓词
                                goal.append(ptSatPred(pt, tempPredicate))
                             # 去重：若输出模式未出现过，则添加 
                            if goal not in predGoal:
                                predGoal.append(goal)
                                if tempPredicate not in preds:# 全局谓词集合，避免重复添加
                                    preds.append(tempPredicate)
                                    if len(preds) == pow(2, len(pts)):# 若谓词数量已达上限（2^点数），提前返回
                                        return

                # 生成 var op num 形式的谓词
                # 第二个操作数为数值
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
        
        # 三元谓词（如ModTest，用于模运算检查）
        if i['arity'] == 3:
            # 变量
            for choose1 in ItemsVar:
                # 数值（模数）
                for choose2 in ItemsNum:
                    # 数值（余数）
                    for choose3 in ItemsNum:
                        # if choose1["size"]+choose2["size"]+choose3["size"]<=MaxSize+1
                        # 确保模数 > 余数（避免无效模运算）
                        if choose3["Expression"] < choose2["Expression"]:
                            try:
                                # 生成模运算谓词（如 v1 % 3 == 0）
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
                                pass    # 忽略除以零的情况


"""Enumerate term """
# 枚举项，尝试找到满足特定目标的项。
# 函数生成项，尝试找到满足特定目标的项，使用 nextSizeTerm 逐步增加项的复杂度
def enumerateTerm(pt, ptGoal):
    # 存储生成的表达式及其属性
    ExpSet = []
    # 存储表达式在所有点上的输出值（去重）
    SigSet = []
    # 初始化大小为1的基础表达式
    sizeOneExps = []
    # 基础表达式：常数（0,1）和变量（v1,v2,v3）
    sizeOneExps.append({'Expression': 0, 'arity': 0, 'size': 1})
    sizeOneExps.append({'Expression': 1, 'arity': 0, 'size': 1})
    sizeOneExps.append({'Expression': v1, 'arity': 1, 'size': 1})
    if Game["var_num"] == 2:
        sizeOneExps.append({'Expression': v2, 'arity': 1, 'size': 1})
    if Game["var_num"] == 3:
        sizeOneExps.append({'Expression': v2, 'arity': 1, 'size': 1})
        sizeOneExps.append({'Expression': v3, 'arity': 1, 'size': 1})
    
    # 检查基础表达式是否满足目标值
    for i in sizeOneExps:
        if i['arity'] == 0:     # 常数（0,1）
            term = i['Expression']
            if term not in SigSet:
                SigSet.append(term)
                i['outputData'] = term
                ExpSet.append(i)
                if term == ptGoal:      # 若常数等于目标值，直接返回
                    return term
        if i['Expression'] == v1:   # 变量v1
            term = v1
            Goal = pt[0]        # 取状态点pt的第一个坐标值
            if Goal not in SigSet:
                SigSet.append(Goal)
                i['outputData'] = Goal
                ExpSet.append(i)
                if Goal == ptGoal:      # 若v1的值等于目标值，返回v1
                    return term
        # 同理处理v2和v3
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

    # 从大小2开始生成复杂表达式
    sizeT = 2
    while True:

        for i in t_vocabulary:# 遍历项词汇表（Add, Sub）
            if termination_sign:# 超时检查
                print("Time out,about to exit the program")
                sheet1.write(row, 2, "time-out-1200s")
                newwb.save(resultFile)
                sys.exit(0)
            for size1 in range(1, sizeT):
                for choose1 in ExpSet:
                    if choose1['size'] == size1:
                        for choose2 in ExpSet:
                            if choose2['size'] == sizeT - size1:
                                # 组合生成新表达式（如v1 + v2, v1 - 1）
                                term = FunExg[i['Function_name']](choose1['Expression'],
                                                                  choose2['Expression'])
                                # 计算表达式在pt处的值
                                Goal = FunExg[i['Function_name']](choose1['outputData'],
                                                                  choose2['outputData'])
                                if Goal == ptGoal: # 若等于目标值，返回表达式
                                    return term
                                if Goal not in SigSet:# 去重
                                    SigSet.append(Goal)
                                    i['outputData'] = Goal
                                    ExpSet.append(
                                        {'Expression': term, 'arity': i['arity'], 'outputData': Goal, 'size': sizeT})
        sizeT += 1

# 生成下一个大小的项集合，并根据覆盖情况筛选出有用的项。
def nextSizeTerm(termMaxSize, DTFlag):  # return [actNum,paraNum,paraTerm]
    # print("next size of term:",termMaxSize)
    global interResultTerm
    ExpSet = []
    SigSet = []
    if DTFlag:# 决策树模式：重新生成基础表达式
        sizeOneExps = []
        sizeOneExps.append({'Expression': 0, 'Isnum': True, 'arity': 0, 'size': 1})
        sizeOneExps.append({'Expression': 1, 'Isnum': True, 'arity': 0, 'size': 1})
        sizeOneExps.append({'Expression': v1, 'Isnum': False, 'arity': 1, 'size': 1})
        if Game["var_num"] == 2:
            sizeOneExps.append({'Expression': v2, 'Isnum': False, 'arity': 1, 'size': 1})
        elif Game["var_num"] == 3:
            sizeOneExps.append({'Expression': v2, 'Isnum': False, 'size': 1})
            sizeOneExps.append({'Expression': v3, 'Isnum': False, 'size': 1})
        # 添加游戏中的常数（如最大取子数）
        for i in Game["appeal_constants"]:
            sizeOneExps.append({'Expression': eval(i), 'Isnum': True, 'size': 1})
        # 初始化基础表达式的输出值
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
            else:# 变量型表达式输出状态点的值
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
            if i['Function_name'] == 'Add':# 处理加法表达式
                if li <= nextTermAdd:# 限制加法复杂度
                 # 生成 var + var 或 var + num
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
                # 生成 num + num
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
            elif i['Function_name'] == 'Sub':# 处理减法表达式
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
    interResultTerm = InterResult(ExpSet, SigSet)# 缓存结果

    # 将项与动作参数关联，筛选有效组合
    for actNum in range(len(actions)):
        action = actions[actNum]
        if len(action["action_parameter"]) == 1:# 单参数动作（如take(k)）
            for item in ExpSet:
                term = item['Expression']
                Goal = item["outputData"]
                Term = (actNum, term)
                if Term not in cover:
                    coverTemp = []
                    # 检查项是否覆盖某些状态点
                    for num in range(len(pts)):
                        pt = pts[num]
                        ptOutput = ptsOutput[num]
                        for output in ptOutput:
                             # 若动作参数输出等于项的输出，记录该状态点
                            if output[0] == actNum and Goal[num] == output[1] and len(output) == 2:
                                coverTemp.append(pt)
                                break
                    if coverTemp != []:# 若有覆盖的状态点
                     # 去重：避免重复的覆盖集合
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
        if len(action["action_parameter"]) == 2:# 双参数动作（如move(x,y)）
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
                                # 双参数匹配
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
# ForLabelCopy 函数：状态点转特征集
# pts：状态点列表，例如 [[0], [1], [2], [3]]（表示有 0-3 个石子的状态）。
# preds：谓词列表，例如 [v1 == 0, v1 % 2 == 0, v1 > 1]（用于描述状态的属性）。
# terms：动作项列表，例如 [(0, 1), (0, 2), (0, 3)]（表示取 1-3 个石子的动作）。
# cover：状态 - 动作覆盖关系，例如 {(0, 1): [[1], [2], [3]], (0, 2): [[2], [3]], ...}。
def ForLabelCopy(pts, preds):
    FeatureSet = []
    FeatureSet.append(preds)# 第一行存储所有谓词
    for pt in pts:
        OnePoint = []
        # 1. 计算Frontset：状态点是否满足每个谓词（0/1编码）
        Frontset = []
        # 计算当前点满足哪些谓词（1表示满足，0表示不满足）
        for pred in preds:
            if ptSatPred(pt, pred):
                Frontset.append(1)
            else:
                Frontset.append(0)
        OnePoint.append(Frontset)# 前半部分：谓词特征
        # 2. 计算Backset：状态点被哪些动作项覆盖（存储动作项索引）
        Backset = []
        # 查找当前点被哪些项-动作对覆盖
        for term in terms:
            index = terms.index(term)
            if pt in cover[term]:
                Backset.append(index)   # 记录项的索引
        OnePoint.append(Backset)    # 后半部分：动作特征
        # 3. 将Frontset和Backset组合，添加到FeatureSet
        FeatureSet.append(OnePoint)     # 添加当前点的特征
    return FeatureSet

# First Method
# 使用增量学习方法学习决策树。
def learn(pts, preds):
    if pts == []:
        return TreeNode(v1 == v1)# 空集返回恒真节点

    # 检查是否所有点都被某个项-动作对覆盖
    for term in terms:
        if not [True for i in pts if i not in cover[term]]:
            # print("leaf node ：",term)
            return TreeNode(str(term))       # 全覆盖则返回叶节点（动作）
    if preds == [] or preds == None:
        return None     # 无可用谓词，返回失败
    FeatureSet = ForLabelCopy(pts, preds)        # 转换为特征集
    infer = Incrementallearn.increlearn(FeatureSet, len(preds), len(terms))
    choose = False
    # 根据参数决定是否选择最小节点数
    if choice_minnode == 'y':
        choose = True
    if choice_minnode == 'n':
        choose = False
    # 调用增量学习算法生成最优树
    tree, root = infer.findOptimalTree(1, choose, terms)
    if root is False:       # 学习失败
        global DTflag
        DTflag = False
        global RedundantPts
        RedundantPts = pts      # 记录无法分类的点
        return None
    # print("\n===========tree print===========\n")
    return root     # 返回决策树根节点

# Second Method
# 使用DT1方法学习决策树。
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
# 使用DTEP方法学习决策树。
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

# 使用 ID3 算法学习决策树，根据信息增益或基尼指数选择最佳谓词进行划分。
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
# 该函数将决策树转换为逻辑公式，表示失败状态的条件，核心使用栈遍历树结构，生成路径表达式。
def tree2LossingFormula(DT) -> str:
    if DT == True:
        return "True"   # 若树为真，直接返回"True"
    if (type(DT.val) == type("False")):
        # print(DT.val)
        return DT.val       # 若节点值为"False"，直接返回
    # t2ftime = time.time()
    paths = []  # Store path And(,,,)# 存储路径的合取表达式（如 And(pred1, pred2)）
    stack = []      # 用于栈遍历
    p = DT  # 当前节点
    pre = None  # 前一个节点
    while (p != None or len(stack) != 0):
        # 向左子树遍历，直到叶节点（类型为"term"）
        while (p != None and type(p.val) != type("term")):
            stack.append(p)
            p = p.left
        # 处理叶节点为"True"的情况
        if p != None and p.val == "True":
            if len(stack) == 1:
                paths.append(stack[0].val)       # 单节点路径
            else:
                arr = []
                # 过滤掉子树中已为"True"的节点
                for i in stack[0:-1]:
                    if type(i.left.val) == type("term") and i.left.val == "True":
                        continue
                    if type(i.right.val) == type("term") and i.right.val == "True":
                        continue
                    arr.append(i)
                if arr == []:
                    paths.append(stack[-1].val)
                else:
                    # 构建合取表达式 And(pred1, pred2, ...)
                    expr = "And("
                    for i in arr:
                        expr = expr + str(i.val) + ","
                    expr = expr + str(stack[-1].val) + ")"
                    paths.append(expr)
        # 回溯处理右子树
        p = stack.pop()
        if (type(p.right.val) == type("term") or p.right == pre):
            if (type(p.right.val) == type("term") and p.right.val == "True"):
                p.val = Not(p.val)      # 取反当前节点值
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
                stack = stack[:-1]   # 弹出栈顶元素
            pre = p
            p = None
        else:
            p.val = Not(p.val)      # 取反当前节点值
            stack.append(p)
            p = p.right     # 转向右子树
    
    # 合并所有路径为析取表达式 Or(path1, path2, ...)
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
# 将所有动作的转移公式合并为一个全局公式，格式为：
# Or(
#     Exists([k] transition_formula1),
#     Exists([l, m] transition_formula2),
#     ...
# )
# Exists 表示存在参数使得动作可执行，transition_formula 描述状态转移逻辑。
# 使用 Z3 的 simplify 函数简化逻辑表达式。
global_transition_formula = "Or("
for i in Game["actions"]:
    if i['action_parameter'] != []:
        temp = "["
        for j in i['action_parameter']:
            temp = temp + str(j) + ","
        temp = temp[:-1]
        temp += "],"    # 格式化为参数列表 [k]
        global_transition_formula = global_transition_formula + \
                                    "Exists(" + temp + str(i["transition_formula"]) + "),"
    else:
        global_transition_formula = global_transition_formula + \
                                    str(i["transition_formula"]) + ","

global_transition_formula = global_transition_formula[:-1]
global_transition_formula = global_transition_formula + ")"# 移除最后一个逗号

print("Global transition formula:\n\t", global_transition_formula)
global_transition_formula = simplify(eval(global_transition_formula))# 用Z3简化公式

"""
default state 
"""
# 默认状态初始化
# 根据变量数量创建多维数组，存储状态是否为失败态或非法态：
# 1 维：position[v1] 表示单变量状态。
# 2 维：position[v1][v2] 表示两变量状态。
# 3 维：position[v1][v2][v3] 表示三变量状态。
# 初始值为 'illegal'，后续通过 isLossingState 函数填充为 True（失败态）或 False（获胜态）。
position = []
if Game['var_num'] == 1:
    # 1维状态：长度200的列表，初始为'illegal'
    for i in range(0, 200):
        position.append('illegal')
elif Game['var_num'] == 2:
    # 2维状态：100x100矩阵
    for i in range(0, 100):
        position.append([])
        for j in range(0, 100):
            position[i].append('illegal')
elif Game['var_num'] == 3:
    # 3维状态：100x100x100矩阵
    for i in range(0, 100):
        position.append([])
        for i1 in range(0, 100):
            position[i].append([])
            for i2 in range(0, 100):
                position[i][i1].append("illegal")

"""
set all terminate state position  
"""
# 存储所有终止状态点
TerminatePosition = []
while (True):
    s = Solver()    # 创建z3求解器示例
    s.add(Game["Terminal_Condition"])   # 添加终止条件约束
    s.add(Game["Constraint"])   # 添加游戏通用约束

    # 根据变量数量添加不同的范围约束和去重约束
    if Game["var_num"] == 1:
        s.add(v1 < 200) # 一维状态的范围约束
        for i in TerminatePosition:
            s.add(v1 != i[0])   # 去重：排除已找到的终止位置
        # 检查是否训在满足条件的状态
        if (s.check() == sat): # 存在解
            m = s.model()   # 获取模型（即满足条件的状态点）
            a = m[v1].as_long()     # 获取变量v1的具体值
            TerminatePosition.append([a])    # 保存状态点

            # 根据游戏类型标注胜负
            if Game["type"] == "normal":   
                position[a] = True
            else:       # 反常游戏规则：无法行动者赢
                position[a] = False     # 终止状态是获胜态
        else:
            break        # 没有更多终止位置，退出循环

    # 二维和三维状态的逻辑类似，只是约束和状态表示更复杂
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
# 状态胜负判定函数 isLossingState

def isLossingState(v):# v 是一个状态点，表示游戏中的一个位置。
    # 超时处理
    if termination_sign:
        print("Time out,about to exit the program")
        sheet1.write(row, 2, "time-out-1200s")
        newwb.save(resultFile)
        sys.exit(0)
    # print("Insert",v," into isLossingstate:")
    # 边界检查：超出预定义范围的状态视为非法
    if len(v) == 1:# 单变量游戏
        if v[0] >= 200:
            return 'illegal'
    else:
        for i in v:
            if i >= 100:
                return 'illegal'
    # 已计算状态直接返回结果（记忆化）
    if len(v) == 1:
        if position[v[0]] != 'illegal':# 检查状态是否已计算过
            return position[v[0]]# 已计算过，直接返回结果
        # 递归计算从0到v[0]的所有状态
        for x in range(0, v[0] + 1):# x 表示可能的动作（取子数量）
            if (position[x] != 'illegal'):
                continue

            # 计算当前状态的所有可能后继状态
            temp = []
            # 使用Z3求解器计算后继状态
            while (True):
                s = Solver()
                s.add(global_transition_formula) # 添加全局转移公式
                s.add(Game["Constraint"])# 添加游戏约束
                s.add(v1 == x) # 当前状态
                for i in temp:
                    s.add(Or(v1_next != i[0]))# 去重：排除已找到的后继
                if (s.check() == sat):# 检查是否存在后继状态
                    m = s.model()
                    temp.append([m[v1_next].as_long()])
                else:
                    break

            # 判断当前状态是否为失败态
            is_losing = True
            s = Solver()
            s.add(Game["Constraint"])
            s.add(v1 == x)
            if (s.check() == unsat):
                continue# 非法状态跳过

            # 递归计算所有后继状态的胜负属性
            for i in temp: # 遍历所有后继状态
                if (position[i[0]] == 'illegal'):# 如果后继状态未计算过
                    position[i[0]] = isLossingState(i) # 递归计算后继状态
            
            # 当前状态是失败态，当且仅当所有后继状态都是获胜态
            for i in temp:
                is_losing = is_losing and not position[i[0]]

             # 更新当前状态的胜负属性
            if (is_losing):
                position[x] = True
            else:
                position[x] = False
        return position[v[0]]

    # 二维和三维状态的逻辑类似，只是状态表示和递归计算更复杂
    elif len(v) == 2:
        if position[v[0]][v[1]] != 'illegal':
            return position[v[0]][v[1]]
        for x in range(0, v[0] + 1):
            for y in range(0, v[1] + 1):
                if (position[x][y] != 'illegal'):
                    continue
                # 计算所有可能后继状态
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
                # 判断当前状态是否为失败态
                is_losing = True
                s = Solver()
                s.add(Game["Constraint"])
                s.add(v1 == x, v2 == y)
                if (s.check() == unsat):
                    continue
                # 递归计算后继状态
                for i in temp:
                    if (position[i[0]][i[1]] == 'illegal'):
                        position[i[0]][i[1]] = isLossingState(i)
                for i in temp:
                    is_losing = is_losing and not position[i[0]][i[1]]
                if (is_losing):
                    position[x][y] = True
                else:/
                    position[x][y] = False
        # print("state：",v,"is",position[v[0]][v[1]])
        return position[v[0]][v[1]]
    
    # 三维状态逻辑与二维类似
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

# 反例生成函数 
# 搜索策略：
# 曼哈顿距离搜索：从原点开始，按距离递增的方式搜索状态空间
# 去重：排除已经在 ptList 和 pts 中的状态点
# 合法性验证：使用 Z3 求解器验证状态是否满足游戏约束
# 范围限制：搜索范围限制在 100 以内，避免无限搜索
# 整体工作流程
# 终止位置识别：找出所有终止状态并标记胜负属性
# 状态胜负判定：递归计算任意状态的胜负属性，基于记忆化搜索和 Z3 求解器
# 反例生成：在学习过程中寻找未覆盖的合法状态点，用于完善决策树
#  ptList=[[pt1],[pt2],[pt3]]
def FindCountExample(ptList):
    if Game["var_num"] == 1:
        i = 1
        while (True):
            if i > 100:     # 搜索范围限制
                global example_run_out_sign
                example_run_out_sign = True
                return 'illegal'
            
            # 按距离原点的曼哈顿距离搜索状态
            for r1 in range(0, i):
                if [r1] not in ptList and [r1] not in pts:  # 排除已有的状态点
                    s = Solver()
                    s.add(Game["Constraint"])
                    s.add(v1 == r1)
                    if (s.check() == sat):      # 检查状态是否合法
                        return [r1]     # 返回找到的合法状态点
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

    # 二维状态的搜索逻辑
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
    # 三维状态的搜索逻辑
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

# 检查状态点覆盖情况
# 验证当前所有项（terms）是否覆盖了所有训练状态点（pts）
def isCoverAll():
    coverAll = []
    for term in terms:
        for i in cover[term]:
            coverAll.append(i)
    # print("cover included",coverAll)
    # 检查每个训练状态点是否都被覆盖
    for pt in pts:
        if pt not in coverAll:
            return False
    return True

# outRange函数：检查状态是否超出范围
# 范围规则：
# 1 维状态：v [0] 必须在 0~199 之间
# 多维状态：每个维度必须在 0~99 之间
# 返回值：
# 'illegal'：状态超出范围
# 无返回：状态合法（隐式返回 None）
# 作用：防止访问越界或处理非法状态
def outRange(v):
    if len(v) == 1:
        if v[0] >=200 or v[0] < 0:
            return 'illegal'
    else:
        for i in v:  # default position < 100
            if i >= 100 or i < 0:
                return 'illegal'

# 生成反例状态点
def satfindstate(ptk):
    ptK = ptk       # 要生成的反例数量
    ptList = []     # 存储生成的反例
    # 获取当前模型中的状态值
    m = s.model()
    value = []
    for i in Game["varList"]:
        value.append(m[i].as_long())
    # 检查状态是否合法并加入反例列表
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
    # 循环生成剩余反例
    while ptK > 0:
        if termination_sign:# 超时处理
            print("Time out,about to exit the program")
            sheet1.write(row, 2, "time-out-1200s")
            newwb.save(resultFile)
            sys.exit(0)
        # 调用FindCountExample生成新反例
        pt = FindCountExample(ptList)
        if pt == 'illegal':             # 无合法反例可生成
            return ptList
        if outRange(pt) == 'illegal':   # 跳过非法状态
            continue
        else:
            ptK -= 1
            ptList.append(pt)
    print("Generate", ptk, "countexamples:\t", ptList)
    return ptList

# 生成未知状态点
# 循环调用FindCountExample生成指定数量的合法状态点，用于初始化训练集
def unkownfindstate(ptk):
    ptK = ptk # 要生成的状态点数量
    ptList = []# 存储生成的状态点
    while True:
        pt = FindCountExample(ptList) # 调用FindCountExample生成状态点
        if pt == 'illegal': # 无合法状态可生成
            return ptList
        if outRange(pt) == 'illegal':# 过滤非法状态
            continue
        else:
            ptK -= 1
            ptList.append(pt)# 添加合法状态到列表
            if (ptK == 0):# 达到目标数量时返回
                print("InitializeStates", ptk, "example generate:\t", ptList)
                return ptList

# 计算表达式中变量的复杂度
def countSize(var, varpool):
    if is_number(var):# 若为数字，转换为浮点数
        var = float(var)
    if type(var) != type(1.0):  # 非数值类型（如变量名v1）
        return 1
    elif var in varpool:        # 变量在变量池中
        return 1
    else:                       # 递归计算变量复杂度（考虑变量组合）
        return 1 + countSize(var, expandpool(varpool))

# 扩展变量池
# 通过累加现有变量生成新的变量池
# 遍历变量池，将每对变量的和添加到新池
# 例如：输入 [0,1]，扩展后为 [0,1,2]
# 用于处理表达式中可能出现的变量组合
def expandpool(varpool):
    p = []
    for i in varpool:
        p.append(i)
    # while i < len(varpool):
    i = 0
    j = 0

    while i < len(varpool):

        while j < len(varpool):
            # 计算变量和并添加到池（避免重复）
            if varpool[i] + varpool[j] not in p:
                p.append(varpool[i] + varpool[j])
            j += 1
        i += 1
        j = i   # 避免重复计算i+j和j+i
    # print(p)
    return p

#  判断字符串是否为数字
def is_number(s):
    try:
        float(s)# 尝试转换为浮点数
        return True
    except ValueError:
        pass

# 计算表达式复杂度
# 统计逻辑运算符（Not, Or, And）数量
# 简化表达式，替换运算符和括号
# 递归计算剩余表达式部分的复杂度
# 结合countSize和expandpool处理变量组合
def Size(expression, varpool=[0, 1]):
    count1 = 0
    str1 = expression.replace(' ', '').replace('\n', '')# 清理表达式
    # 统计逻辑运算符数量
    while str1.find('Not') >= 0:
        count1 += 1
        str1 = str1.replace('Not', '', 1)
    while str1.find('Or') >= 0:
        count1 += 1
        str1 = str1.replace('Or', '', 1)
    while str1.find('And') >= 0:
        count1 += 1
        str1 = str1.replace('And', '', 1)
    # 简化表达式（替换运算符和括号）
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
         # 按分隔符分割并递归计算
        tempvar = str1[0:str1.find('-')]
        # print(tempvar,'size is',countSize(tempvar,varpool))
        # print(count1)
        count1 += countSize(str1[0:str1.find('-')], varpool)
        str1 = str1[str1.find('-') + 1:len(str1)]
    return count1

# 从 PDDL 文件中提取数字常量，构成基础变量池
# 使用正则表达式提取所有数字
# 去重并转换为整数列表
# 确保包含 0,1,2 以覆盖基础情况
def Getvarpool(pddl):
    num = re.findall('\d+', pddl)   # 提取所有数字
    num = list(set(num))            # 去重
    num = list(map(int, num))       # 转换为整数
    # 确保包含0,1,2
    if not (0 in num):
        num.append(0)
    if not (1 in num):
        num.append(1)
    if not (2 in num):
        num.append(2)
    return num

# 获取获胜公式大小
def GetSize(gamename, winningformula):
    if winningformula == "False" or winningformula == "True" or winningformula == "true":
        return 1        # 简单公式大小为1
    varpool = Getvarpool(gamename)      # 获取变量池
    size = Size(winningformula, varpool)# 计算公式复杂度
    return size

# 记录获胜公式学习的开始时间，用于计时
# 初始化超时标志，控制程序运行时间
start_winning_formula_time = time.time()# 记录开始时间

# The time thread determines whether it timed out
termination_sign = False        # 初始化终止标志（默认为False）


def programTimeOut():
    global termination_sign
    termination_sign = True# 设置终止标志为True
    Thread1.cancel()# 取消计时器线程

# 创建计时器线程，time_out1秒后调用programTimeOut
Thread1 = threading.Timer(time_out1, programTimeOut)
Thread1.start()

# 初始化训练数据和参数
pts = []        # 状态点列表
ptsGoal = []    # 状态点对应的目标值（True/False）

Maxsize = 1     # 最大谓词大小，用于限制枚举复杂度
preds = []      # 谓词集合
# unknownNum = 1
newwb = copy(oldwb) # 复制Excel工作簿
sheet1 = newwb.get_sheet(0)# 获取第一个工作表
sheet1.write(row, 0, gameName)# 写入游戏名称
newwb.save(resultFile) # 保存文件

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
    # 初始化条件和覆盖信息
    terms = [True, False]   # 初始条件为真和假
    cover = {}
    cover[True] = []
    cover[False] = []
    for num in range(len(pts)):
        cover[ptsGoal[num]].append(pts[num])    # 记录每个条件覆盖的状态点
    print("Labels set: \t", str(cover).replace('True', 'temp').replace('False', 'True').replace('temp', 'False'))
    
    # 初始化决策树和公式
    DT = None
    e = v1 == v1  # Default formula # 默认公式（永远为真）
    last_e = e      # 记录上一轮公式
    DTTime = time.time()    # 记录决策树学习开始时间
    global DTflag
    DTflag = True
    flagAdd = True
    # 学习决策树
    while pts != [] and (DT == None or DTflag == False):
        if termination_sign:
            print("Time out,about to exit the program")
            sheet1.write(row, 2, "time-out-1200s")
            newwb.save(resultFile)
            sys.exit(0)
        # 枚举谓词
        enumPredsTime = time.time()
        enumeratePredicate(Maxsize, DTflag)  # DTflag- Continue enumerating predicates in the last place# 枚举最大复杂度为Maxsize的谓词
        print("the set of atoms:", preds)
        print("Number of data points:  ", len(pts))

        # 计算信息增益并学习决策树
        calculateIGTime = time.time()
        DTflag = True
        # *********************************************************************************************************
        # 根据选择的方法学习决策树
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
        # 如果决策树学习失败，增加最大谓词复杂度
        if (DTflag == False):
            Maxsize += 1
            flagAdd = False
            print('Cannot solve,need more atoms, increase Maxsize', Maxsize)
    # print("Time of learn DT：", time.time()-DTTime)

    # 将决策树转换为逻辑公式
    if DT != None:
        e = eval(tree2Expr(DT))
    print("\n-------------------------- Learn decision tree -------------------------\n\t",
          str(e).replace('True', 'temp').replace('False', 'True').replace('temp', 'False'))
    # 处理公式中的变量（将v1,v2,v3替换为v1_next,v2_next,v3_next）
    try:
        e1 = eval(str(e).replace("v2", "v2_next").replace("v3", "v3_next").replace("v1", "v1_next"))
    except:
        Thread1.cancel()
        print("Time out,about to exit the program")
        sheet1.write(row, 2, str(time_out1))
        newwb.save(resultFile)
        sys.exit(0)

    print("\n----------------------------- Verification  ----------------------------\n")

    # 检查公式是否与上一轮相同
    if str(e) != str(last_e):
        # 根据游戏类型设置验证条件
        if Game["type"] == "normal":
            # e is losing formula
            # con1 = Not(Implies(Game['Terminal_Condition'],e))
            # 正常游戏规则下的验证条件
            # con1: 终止状态不能是失败态
            con1 = And(Game["Constraint"], Game["Terminal_Condition"], Not(e))
            # con2 = And(Game["Constraint"], Not(e), ForAll(varListY, Or(Not(global_transition_formula), Not(e1))))
            # con3: 失败态的所有动作必须导致非失败态
            con3 = And(Game["Constraint"], e, Not(Game["Terminal_Condition"]),
                       Exists(varListY, And(global_transition_formula, e1)))
            # con3 =Not(Implies(And(Game["Constraint"],e),ForAll(varListY, Implies(global_transition_formula, Not(e1)))))
            # con2: 非失败态必须有至少一个动作导致失败态
            con2 = Not(Implies(And(Game["Constraint"], Not(e)), Exists(varListY, And(global_transition_formula, e1))))
        else:
            # 反常游戏规则下的验证条件（逻辑相反）
            # con1 = Not(Implies(Game['Terminal_Condition'],Not(e)))
            con1 = And(Game["Constraint"], Game["Terminal_Condition"], e)
            # con2 = And(Game["Constraint"], Not(e), Not(Game["Terminal_Condition"]), ForAll(varListY, Implies(global_transition_formula, Not(e1))))
            con2 = Not(Implies(And(Game["Constraint"], Not(e), Not(Game["Terminal_Condition"])), Exists(
                varListY, And(global_transition_formula, e1))))
            # con3 = Not(Implies(And(Game["Constraint"],e),ForAll(varListY, Implies(global_transition_formula, Not(e1)))))
            con3 = And(Game["Constraint"], e), Exists(varListY, And(global_transition_formula, e1))

        # 使用Z3求解器验证条件
        s = Solver()
        s.set('timeout', 60000)# 设置超时时间为60秒
        # 验证条件1
        s.add(con1)
        check1 = s.check()
        # print("con1 check:",check1)
        if check1 == sat:
            # print("unsat con1")
            print(
                "The constraint of winning formula is not valid and add countexamples, go to the next round of the learning process.")
            examples = satfindstate(ptk)# 生成反例
        else:
            # print("sat con1")
            # 验证条件2
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
                # 验证条件3
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
                    # 所有条件都满足，公式验证成功
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
                    # 输出获胜公式并保存结果
                    print("\n---------------------------- Winning formula  --------------------------\n")

                    print("Losing formula：", losing_formula)
                    losing_formula_Y = e1
                    winning_formula = simplify(Not(losing_formula))# 获胜公式是失败公式的否定
                    sizeFormula = GetSize(gameName, str(winning_formula))# 计算公式大小
                    winning_formula_time = time.time() - start_winning_formula_time# 计算学习耗时
                    print("Winning Fromula：", winning_formula)
                    print("The total running time：", round(winning_formula_time, 2))
                    print("The size: ", sizeFormula)
                    winning_formula_time = str(round(winning_formula_time, 2))
                    
                    # 保存结果到Excel
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
        # 公式重复，生成未知状态点
        print("Repeat expression")
        examples = unkownfindstate(ptk)
    # 将生成的反例添加到训练数据中
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
# 处理获胜公式和失败公式
winning_formula_Y = eval(str(winning_formula).replace("v2", "v2_next")
                         .replace("v3", "v3_next").replace("v1", "v1_next"))
# print(losing_formula)
losing_formula_Y = eval(str(losing_formula).replace("v2", "v2_next")
                        .replace("v3", "v3_next").replace("v1", "v1_next"))
# print(winning_formula_Y)
# print("losing_formula_Y:",losing_formula_Y)

# 处理特殊情况：失败公式为True或False
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
# 计算动作数量
lenActs = len(actions)

# 为给定状态点生成满足条件的具体动作
def genOutput(pt):
    print("Generate ground action for datapoint", pt)
    outputList = []
    # 遍历所有可能的动作
    for i in range(0, lenActs):
        action = actions[i]
        # 尝试生成该动作的具体参数值
        while True:
            s = Solver()
            # 避免生成重复的动作实例
            for output in outputList:
                parasLen = len(action["action_parameter"])
                if i == output[0] and parasLen == len(output) - 1:
                    if parasLen == 1:
                        s.add(k != output[1])# 单个参数的情况
                    else:
                        # 多个参数的情况，构建逻辑表达式
                        con = "Or("
                        for num in range(0, parasLen):
                            con = con + str(action["action_parameter"][num]) + "!=" + str(output[num + 1]) + ","
                        con = con[:-1]
                        con = con + ")"
                        s.add(eval(con))
            # 设置当前状态
            if Game['var_num'] == 1:
                s.add(v1 == pt[0])
            elif Game["var_num"] == 2:
                s.add(v1 == pt[0], v2 == pt[1])
            elif Game["var_num"] == 3:
                s.add(v1 == pt[0], v2 == pt[1], v3 == pt[2])
            
            # 添加动作的前置条件、转换公式和失败状态约束
            s.add(actions[i]['precondition'])
            s.add(actions[i]['transition_formula'])
            s.add(losing_formula_Y)

            # 检查是否存在满足条件的动作
            if s.check() == sat:
                m = s.model()
                ans = [i]# 动作索引
                
                # 获取动作参数值
                for para in action["action_parameter"]:
                    ans.append(m[para].as_long())  # addk# 添加参数值
                
                printGroundAction(ans)# 打印找到的动作
                # action = actions[ans[0]]
                # print("exist ground action:" + action["action_name"]+ "("+str(ans)[4:-1]+")")
                # print(" [act,para] ",ans)
                outputList.append(ans)# 添加到输出列表
            else:
                break# 没有更多满足条件的动作，退出循环
    return outputList

# 寻找满足路径公式的新状态点
def genPtSatFormula(pathformula, ptList):
    if Game['var_num'] == 1:
        i = 1
        while True:
            if i > 150: return False# 搜索范围限制

            # 遍历可能的状态值
            for r1 in range(0, i + 1):
                if [r1] not in ptList and [r1] not in pts:# 确保状态点未被使用
                    s = Solver()
                    s.add(Game['Constraint'])# 添加游戏约束
                    s.add(Not(Game["Terminal_Condition"]))# 非终止状态
                    # s.add(winning_formula)
                    s.add(pathformula)# 添加路径公式
                    s.add(v1 == r1)# 设置当前状态
                    if s.check() == sat:
                        # print("find state:",r1)
                        return [r1]# 找到满足条件的状态点
            i = i + 1
    # 类似逻辑处理2维和3维状态空间
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

# 打印具体动作信息
def printGroundAction(termlist):
    action = actions[termlist[0]]
    print("Find a ground action:" + action["action_name"] + "(" + str(termlist)[4:-1] + ")")

# 打印动作信息（简化版）
def printAction(termlist):
    action = actions[termlist[0]]
    print("Find action:" + action["action_name"] + "(" + str(termlist)[4:-1] + ")")


# [str,str...]

# 提取决策树中表示失败状态的所有路径公式
def WF(DT):
    paths = []
    stack = []
    p = DT
    pre = None
    # 非递归遍历决策树
    while p != None or len(stack) != 0:
        # 向左遍历直到叶子节点或终止条件
        while (p != None and type(p.val) != type("term")):
            stack.append(p)
            p = p.left
        
        # 处理叶子节点为False的情况（表示失败状态）
        if p != None and p.val == "False":
            # print("1806",p.val)
            if len(stack) == 1:
                paths.append(str(stack[0].val))# 单节点路径
            else:
                # 构建多节点路径公式
                arr = []
                for i in stack[0:-1]:
                    # 过滤无效路径
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
        # 处理右子树
        if (type(p.right.val) == type("term") or p.right == pre):
            if (type(p.right.val) == type("term") and p.right.val == "False"):
                p.val = Not(p.val)# 取反条件
                stack.append(p)
                # 构建路径公式（类似左侧处理）
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
# 提取决策树中表示动作的所有路径
def pathOfAct(DT):
    if type(DT.val) == type("term"):
        return [["", eval(DT.val)]]# 单节点决策树
    paths = []
    stack = []
    p = DT
    pre = None
     # 非递归遍历决策树
    while p != None or len(stack) != 0:
        while (p != None and type(p.val) != type("str")):
            stack.append(p)
            p = p.left
        if p != None:
            # 构建路径条件和对应动作
            if len(stack) == 1:
                paths.append([stack[0].val, eval(p.val)])
            else:
                expr = "And("
                for i in stack:
                    expr = expr + str(i.val) + ","
                expr = expr[0:len(expr) - 1] + ")"
                paths.append([eval(expr), eval(p.val)])
        p = stack.pop()
        # 处理右子树
        if (type(p.right.val) == type("term") or p.right == pre):
            if type(p.right.val) == type("term"):
                p.val = Not(p.val)
                stack.append(p)
                # 构建路径条件和对应动作
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
# 检查给定的动作项是否匹配特定状态和输出
def isTermSatExample(term, pt, output):
    # 检查动作索引和参数数量是否匹配
    if output[0] != term[0] or len(output) != len(term):
        return False
    # 根据状态维度检查参数值是否匹配
    if Game["var_num"] == 2:
        for i in range(1, len(term)):  # term [0,v1], [0,v1,v1_next]
        # 替换变量为实际状态值并比较
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
# 确保每个状态点的输出都有对应的动作项覆盖
def ptsAllCover():
    print("Ensure each data point have label cover:")
    # 遍历所有状态点
    for num in range(len(pts)):
        pt = pts[num]
        ptOutput = ptsOutput[num]
        # 检查每个输出动作
        for output in ptOutput:
            flag_cover = False
             # 查找匹配的动作项
            for term in terms:
                if isTermSatExample(term, pt, output):
                    flag_cover = True
                    break
            # 如果没有找到匹配项，生成新的动作项
            if flag_cover == False:
                print(pt, "no label cover:", )
                # 根据输出参数数量生成新的动作项
                if len(output) == 2:
                    term = (output[0], enumerateTerm(pt, output[1]))
                elif len(output) == 3:
                    term = (output[0], enumerateTerm(pt, output[1]), enumerateTerm(pt, output[2]))
                elif len(output) == 4:
                    term = (
                    output[0], enumerateTerm(pt, output[1]), enumerateTerm(pt, output[2]), enumerateTerm(pt, output[3]))
                printAction(term)
                # print("find term",term,"cover")
                # 添加新的动作项到覆盖关系中
                if term not in cover:
                    terms.append(term)
                    cover[term] = []
                cover[term].append(pt)


# Update the relationship between all terms and PTS
# 更新所有动作项与状态点之间的覆盖关系
def updateCover():
    # print("update cover.........")
    # 遍历所有动作项
    for term in terms:
        for num in range(0, len(pts)):
            pt = pts[num]
            ptOutput = ptsOutput[num]
            # 如果状态点未被当前动作项覆盖
            if pt not in cover[term]:
                # 检查是否有匹配的输出动作
                for output in ptOutput:
                    if isTermSatExample(term, pt, output):
                        cover[term].append(pt)
                        break


"""convert tree to winning strategy formula::  leaf node -- action"""

# 决策树转获胜策略公式
def tree2WinningStrategy(DT) -> str:
    expr = ""
    if type(DT.val) == type("str"):
        term = eval(DT.val)# 将字符串转换为元组（动作索引+参数）
        action = actions[term[0]]# 获取动作定义
        action = eval(str(action).replace("k", '(' + str(term[1]) + ')'))# 替换参数
        return str(action["transition_formula"])# 返回动作的转换公式
    if (type(DT.val) == type(v1 == v2)):
         # 递归构建条件表达式：If(条件, 左子树策略, 右子树策略)
        expr = "If(" + str(DT.val) + "," + tree2WinningStrategy(DT.left) + "," + tree2WinningStrategy(DT.right) + ")"
    return expr


def tree2Act(DT):
    if DT == None: return "None"
    expr = ""
    if type(DT.val) == type("term"):
        term = eval(DT.val)# 解析动作项
        # print(term)
        action = actions[term[0]]# 获取动作定义
        return str(action["action_name"]) + "(" + str(term)[4:]# 返回动作名称和参数
    if (type(DT.val) == type(v1 == v2)):
        # 构建条件动作序列
        expr = "If(" + str(DT.val) + "," + tree2Act(DT.left) + "," + tree2Act(DT.right) + ")"
    return expr

# 生成默认动作
def defaultAction():
    S1 = Solver()
    S1.add(Game["Constraint"])# 添加游戏约束
    S1.add(Game["actions"][0]["precondition"])# 添加第一个动作的前置条件
    if S1.check() == sat:
        m = S1.model()
        para = m[k].as_long()# 获取参数值
        return [["", (0, para)]]# 返回动作（索引0，参数para）
    return

# 生成默认谓词集合
def defaultPreds(pathFormula):
    str1 = str(pathFormula)
    str1 = str1.replace(' ', '').replace("\n", "")# 清理公式字符串
    arr1 = []
    if "And" in str1:  # And(f1, f2, f3 ,f4)# 处理合取式，如 And(f1, f2, f3)
        str1 = str1[4:-1]# 去除"And("和")"
        arr = str1.split(",") # 拆分为子公式
    else:  # f1 # 单个公式
        arr = [str1]
    for s in arr:
        if "Not" in s:# 处理否定式
            s = s[4:-1]# 去除"Not("和")"
            if "%" in s:  # a%b==c# 处理模运算，如 a%b==c
                b = s[s.find('%') + 1:s.find("==")]
                c = s[s.find("==") + 2:]
                # 生成所有可能的余数情况
                for i in range(0, eval(b)):
                    if str(i) != c:
                        arr1.append(s[:s.find("==") + 2] + str(i))
            elif "==" in s:  # ==# 处理等于关系
                arr1.append(s.replace("==", ">"))# 生成大于
                arr1.append(s.replace("==", "<"))#生成小于
        else:# 处理非否定式
            if ">=" in s:
                arr1.append(s.replace(">=", ">"))
                arr1.append(s.replace(">=", "=="))
            elif "<=" in s:
                arr1.append(s.replace("<=", "<"))
                arr1.append(s.replace("<=", "=="))
     # 将字符串转换为Z3表达式
    preds = []
    for i in arr1:
        i = eval(i)
        preds.append(i)
    return preds


def isPtSatForm(pt, form):
    s1 = Solver()
    s1.add(form)# 添加待验证公式

    # 根据状态维度添加状态约束
    if Game['var_num'] == 1:
        s1.add(v1 == pt[0])
         # 检查可满足性
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

# 将复杂路径公式拆分为基本条件的所有可能组合
def splitPaths(pathFormula):  # And(Not(v1 + v2 == 1), Not(x%5=1) ,v1 < v2) Not(v1 + v2 == 1)
    ans = []
    str1 = str(pathFormula)
    str1 = str1.replace(' ', '').replace("\n", "")

    # 拆分合取式
    if "And" in str1:
        arr2 = str1[4:-1].split(",")
    else:
        arr2 = [str1]

    arr = []
    for str2 in arr2:
        arr1 = []
        if "Not" in str2:
            # 处理否定表达式
            if "%" in str2:  # a%b==c
                str2 = str2[4:-1]# 移除Not括号
                b = str2[str2.find('%') + 1:str2.find("==")]# 获取模数
                c = str2[str2.find("==") + 2:]# 获取比较值
                for i in range(0, eval(b)):# 枚举余数
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
            # 处理肯定表达式
            if ">=" in str2:
                arr1.append(str2.replace(">=", ">"))
                arr1.append(str2.replace(">=", "=="))
            elif "<=" in str2:
                arr1.append(str2.replace("<=", "<"))
                arr1.append(str2.replace("<=", "=="))

        # 若未生成变体，保留原表达式
        if arr1 == []:
            arr1.append(str2)

        # 过滤掉不满足游戏约束的表达式
        arr3 = []
        # print(arr1)
        for i in arr1:
            s = Solver()
            s.add(eval(i))
            s.add(Game['Constraint'])
            s.add(Not(Game['Terminal_Condition']))# 非终止状态
            s.add(winning_formula)# 满足获胜公式
            # print(s.check)
            if s.check() == sat:
                arr3.append(i)
        arr.append(arr3)

    # 生成所有可能的组合
    for f in product(*arr):
        ans.append(list(f))
    # print("refinement path :",ans)
    return ans

# 提取字符串中的数字，从字符串中提取所有数字子串
def extractNum(str):
    str = str.replace(" ", '')# 移除空格
    ans = []
    i = 0
    while i < len(str):
        if str[i] <= '9' and str[i] >= "0": # 检查是否为数字
            ch = str[i]
            while (i < len(str) - 1 and str[i + 1] <= '9' and str[i + 1] >= '0'):# 提取连续数字
                i = i + 1
                ch = ch + str[i]
            ans.append(ch)  # Game['appeal_constants']
        i += 1
    return ans


# 将失败公式中的数字添加到游戏常量集合
for i in extractNum(str(losing_formula)):
    Game['appeal_constants'].append(i)
# 打印策略学习开始信息
print("\n")
print("#####################################################################")
print("################# Learning winning strategy #########################")
print("#####################################################################")
print("\n")
# 获取失败状态的状态点
ptsOld = cover[False]

# print("winning formula used pts:",ptsOld)
# print("Decision tree1:",tree2Expr(resultDT))
# 提取决策树中表示失败状态的所有路径公式
formulaPaths = pathOfWF(deepcopy(resultDT))
print("All T-label paths:\n\t", formulaPaths)

# 设置超时控制（第二次超时，针对策略学习）
def programTimeOut2():
    global termination_sign
    termination_sign = True
    Thread2.cancel()


termination_sign = False  # Timeout flag# 重置终止标志
Thread2 = threading.Timer(time_out2, programTimeOut2)
Thread2.start()# 启动超时计时器

# 记录策略学习开始时间
startWinningStrategyTime = time.time()
winningStrategy = []# 初始化获胜策略列表
exitFlag = False # 初始化退出标志

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

#  路径公式遍历与状态筛选
for pathFormula in formulaPaths:
    if exitFlag: break# 退出标志，用于提前终止

    print("\n******************** One of T-label path formula:", pathFormula, "**********************\n")

    # print("one T-label path formula:",pathFormula,)
    # print("---------------------------------------------------------------------")

    pathFormula = eval(pathFormula)  # str --> z3# 将字符串转换为Z3逻辑表达式
     # 筛选满足当前路径公式且非终止状态的点
    pts = []
    for pt in ptsOld:
        if isPtSatForm(pt, pathFormula) and pt not in TerminatePosition:
            pts.append(pt)
    # 为每个状态点生成可执行动作
    ptsOutput = []
    for pt in pts:
        outputs = genOutput(pt)
        ptsOutput.append(outputs)
    # 生成默认谓词集合（用于决策树学习）
    preds = defaultPreds(pathFormula)
    print("defaultPreds:\n",preds)


    terms = []
    cover = {}
    maxSizePred = 1
    maxSizeTerm = 0
    while True:
        if termination_sign:# 超时检查
            print("Time out,about to exit the program")
            sheet1.write(row, 4, "time-out-1200s")
            newwb.save(resultFile)
            sys.exit(0)
        print("The set of data points:", pts)
        ptsAllCover()# 确保每个状态点的动作被覆盖
        updateCover()# 更新动作-状态覆盖关系

        # for key,val in cover.items():
        #     print(key,":",val)
        # cycleNum = 2
        DTflag = True
        DT = None
        # 循环学习决策树，直到成功或达到最大复杂度
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
            nextSizeTerm(maxSizeTerm, DTflag) # 生成指定大小的项
            print("The set of label:")
            print("\t", end="")
            for i in terms:
                action = actions[i[0]]
                print(action["action_name"] + "(" + str(i)[4:-1] + ")" + "  ", end="")
            print("\n")
            # print("terms\n",terms)

            enumeratePredicate(maxSizePred, DTflag)# 枚举谓词
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
            # 根据选择的方法学习决策树
            if choice_method == "ID3":
                DT = learn_DT(pts, preds)
            elif choice_method == "Incre":
                DT = learn(pts, preds)
            elif choice_method == "DT1":
                DT = learn_sat_DT1(pts, preds)
            elif choice_method == "DTEP":
                DT = learn_sat_DTEP(pts, preds)
            #*********************************************************************************************************
            if DTflag == False: # 学习失败，增加谓词复杂度
                maxSizePred += 1
                DT = None
                print('Cannot solve ,need bigger atom szie:', maxSizePred, " and more label")
        
        # 输出学习到的决策树动作序列
        print("\n---------------------------- Learn decision tree --------------------------")
        print("\t" + tree2Act(DT) + "\n")
        # print("candidate tree",tree2Act(DT))

        print("------------------------------- Verification  -----------------------------\n\t")
        # ActPaths = defaultAction()
        if DT != None:
            ActPaths = pathOfAct(DT)# 提取动作路径
            print("Path:", pathFormula, ", all canditate strategy:", ActPaths)  # [["", (0, 1, 1)]]
            isSAT = True
            winningStrategyTemp = []
            for path in ActPaths:
                concreteAct = path[1]  # (0,1,1)# 具体动作（如(0,1)表示动作0，参数1）
                action = deepcopy(actions[concreteAct[0]])
                ActExe = action['action_name'] + '(' + str(concreteAct)[4:]

                # 替换动作参数为具体值
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

                # 构建验证条件
                if type(path[0]) != type(""):
                    winningStrategyPath = And(pathFormula, path[0])
                    con = Not(Implies(And(Game["Constraint"], pathFormula, path[0], Not(Game["Terminal_Condition"])),
                                      And(preAct, ForAll(varListY, Implies(transitionFormula, losing_formula_Y)))))
                else:
                    winningStrategyPath = pathFormula
                    con = Not(Implies(And(Game["Constraint"], pathFormula, Not(Game["Terminal_Condition"])),
                                      And(preAct, ForAll(varListY, Implies(transitionFormula, losing_formula_Y)))))

                print("Verify this path:", winningStrategyPath, "execute action:", ActExe)

                # 使用Z3验证策略正确性
                s = Solver()
                s.set('timeout', 60000)
                s.add(con)
                if s.check() == sat:
                    # 验证失败，生成反例
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
                     # 验证通过，记录策略
                    winningStrategyTemp.append([winningStrategyPath, ActExe])
                    print("\t", path, "is a winning rule")
        elif DT == None:
             # 决策树生成失败，生成反例
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
            # 策略验证通过，记录结果
            print("\nThe T-label path formula", pathFormula, "can find partial winning strategy：")
            print("\t", tree2Act(DT))
            for i in winningStrategyTemp:
                winningStrategy.append(i)
            break

# 结果汇总与保存
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


#************************************Learn RL Method **************************
class RLEnumState:
    def __init__(self, positive_states, negative_states, used_atoms, candidate_atoms):
        self.positive = positive_states  # 正例状态集合（满足获胜条件）
        self.negative = negative_states  # 反例状态集合（不满足获胜条件）
        self.used_atoms = used_atoms    # 已使用的原子列表
        self.candidate_atoms = candidate_atoms  # 待选原子列表
        
    def to_feature(self):
        # 将状态转换为RL可处理的特征（无需图嵌入，直接使用原子统计特征）
        # 1. 原子区分度：每个原子在正/负例中的True比例
        atom_discrimination = []
        for atom in self.candidate_atoms:
            pos_true = sum(eval_atom(atom, s) for s in self.positive) / len(self.positive)
            neg_true = sum(eval_atom(atom, s) for s in self.negative) / len(self.negative)
            atom_discrimination.append(pos_true - neg_true)  # 区分度指标
        
        # 2. 反例数量特征
        return np.array([
            len(self.positive), len(self.negative),
            *atom_discrimination
        ])
