from pysat.formula import CNF
from pysat.solvers import Solver
from z3 import *
# myslover = Solver(name='m22') #g3
# myslover.add_clause([1])
# myslover.add_clause([-1])
# print(myslover.solve())
# print(myslover.get_core())
# print(int(3/2))
from DTEP import DTEP
from DTEP import DTEP_Infer
# from Incremental import Infer
# from Incremental import Incrementallearn

# from z3 import *
# # class Node:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# # def bfsTE(numNodeSize,d,p,s,t,g,toward):
# #     if numNodeSize==0:
# #         return p
# #     g[(p,s-1)] = toward
# #     if numNodeSize == 1:
# #         t[(p,s)] = 1
# #         if p==int((7+1)/2):
# #             # print("结束一次模板")
# #             print("t",t)
# #             print("g",g)
# #             print("**********")
# #         return p
# #     else:
# #         t[(p,s)] = 0
# #     t2 = copy.deepcopy(t)
# #     g2 = copy.deepcopy(g)
# #     for i in range(1,numNodeSize): 
# #         t = copy.deepcopy(t2)
# #         g = copy.deepcopy(g2)
# #         print("左边节点个数",i)
# #         bfsTE(i,d-1,p,s+1,t,g,0)
# #         print("左边结束",i)
# #         print("右边节点个数",numNodeSize-i-1)
# #         bfsTE(numNodeSize-i-1,d-1,p+1,s+1,t,g,1)
# #         print("右边结束",numNodeSize-i-1)
# # # def bfsTE1(numNodeSize,d):
# # #     # print(numNodeSize,p,s)
# # #     if numNodeSize == 1:
# # #         return Node()
# # #     if d ==0:
# # #         return 
# # #     for i in range(1,numNodeSize): 
# # #         left = bfsTE1(i,d-1)
# # #         right = bfsTE1(numNodeSize-i-1,d-1)
# # #         node = Node()
# # #         node.left = left
# # #         node.right = right

# #     # print(numNodeSize,toward,"结束该循环")
# #     # print("t1:",t,"g1：",g)
# # t ={}
# # g = {}
# # bfsTE(7,2,1,1,t,g,0)
# # print("t")
# # print(t)
# # print("g")
# # print(g)
        
# def printTree(node,toward):
#     if node is None:
#         return
#     # print("----------")
#     print(node.val,toward)
#     # print(node.left.val,toward)
#     # print(node.right.val,toward)
#     # print("----------")
#     printTree(node.left,0)
#     printTree(node.right,1)

v1 = Int("v1")
v2 = Int("v2")
v3 = Int("v3")
# def tree2Expr(DT) -> str:
#     if not DT:
#         return "False"
#     if DT == True:
#         return "True"
#     expr = ""
#     # 'NoneType' object has no attribute 'val'
#     if (type(DT.val) == type("False")):
#         return DT.val
#     if (type(DT.val) == type(v1 == v2)):
#         expr = "If(" + str(DT.val) + "," + tree2Expr(DT.left) + \
#                "," + tree2Expr(DT.right) + ")"
#     if (type(DT.val) == type(v1) or type(DT.val) == type(0)):
#         expr = str(DT.val)
#     return expr
# # {False: [[0, 0, 0], [0, 1, 1]], True: [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 2, 0]]}
# # FeatureSet = [[v1 == v2, v1 == v3, v1 == 0, v1 == 1, v2 == 0, v3 == 0, v1 >= 0, v1 > 1, v2 == v3, v2 == 1, v3 == 1, v2 >= v3, v2 >= 1, v3 >= v2, v2 > v3, v2 > 1, v3 > v2], 
# #               [[1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1], [1]], 
# #               [[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0], [1]], 
# #               [[0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0], [1]], 
# #               [[1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0], [0]], 
# #               [[0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0]], 
# #               [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0], [1]]]
# FeatureSet = [[v1 == 1,v2 == v3], 
#               [[0, 0], [1]], 
#               [[1, 1], [1]],  
#               [[0, 1], [0]],  
#               ]

# preds = [v1 == 1, v2 == v3]
# infer = DTEP.learnSatDT(FeatureSet, len(preds), 2, [True,False])
# # infer = Incrementallearn.increlearn(FeatureSet, len(preds), 2)
# root = infer.findOptimalTree(3)
# printTree(root,-1)
# # infer = Incrementallearn.increlearn(FeatureSet, len(preds), 2)
# # tree, root = infer.findOptimalTree(1, "y", [True,False])
# # e = eval(tree2Expr(root))
# # print(e)

# # def constructTree(n):
# #     if n == 0:
# #         return None
# #     root = TreeNode(n)
# #     for i in range(n):
# #         left_subtrees = constructTree(i)
# #         right_subtrees = constructTree(n - i - 1)
# #         for left in left_subtrees:
# #             for right in right_subtrees:
# #                 node = TreeNode(n)
# #                 node.left = left
# #                 node.right = right
# #                 root = node
# #     return root

# # 列举所有二叉树的情况
# # n = 7
# # d = 2
# # trees = DTEP.learnSatDT.TE(1,n, d)

# # # 打印所有二叉树的情况
# print("打印结果")
def printTree(node,toward):
    if node is None:
        return
    # print("----------")
    print(node.val,toward)
    # print(node.left.val,toward)
    # print(node.right.val,toward)
    # print("----------")
    printTree(node.left,1)
    printTree(node.right,0)

data = [[v1%4 == 1, v1%4 == 2, v1%4 == 3, v1 == 0, v1 == 1, v1 == 3, v1 >= 0, v1 >= 3, v1 >= 4, v1 > 1, v1%3 == 0, v1%3 == 1], 
        [[1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [0, 1]], 
        [[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [1, 2]], 
        [[0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0], [1, 3]], 
        [[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0]], 
        [[0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0], [2]], 
        [[0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [3]]]
# data = [[v1%4 == 1, v1%4 == 2], 
#         [[1, 0], [0, 1]], 
#         [[0, 1], [2]], 
#         [[0, 0], [1, 3]],
#         [[0, 0], [3]]]
terms = [(0, 1), (0,v1), (0, 2), (0, 3)]

T = {(1, 1): 0, (1, 2): 1, (2, 2): 0, (2, 3): 1, (3, 3): 1, (3, 2): 0, (2, 1): 0, (3, 1): 0}
S = {1: 2, 2: 3, 3: 3}
G = {(1, 0): 0, (1, 1): 0, (1, 2): 1, (2, 1): 1, (2, 2): 0, (2, 3): 1, (3, 2): 1, (3, 3): 1, (3, 1): 1, (2, 0): 0, (3, 0): 0}
E = {(1, 2): 0, (2, 3): 0, (3, 3): 0, (3, 2): 1, (2, 2): 0, (2, 1): 1, (3, 1): 1, (1, 1): 0}

infer = DTEP_Infer.Mysolver(data,12,4,terms,5)
infer.addConstraints_sample(T,G,S)
if infer.myslover.solve():
    print("有解！！！打印model: ")
    model = infer.myslover.get_model()
    # print(model)
    root = infer.getTreeModel(model,S,G,E)
    printTree(root,1)
    # return root
