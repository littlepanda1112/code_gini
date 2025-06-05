from Incremental import Infer
import math


class increlearn:
    def __init__(self, data, numFeature, numClass):

        self.data = data
        self.datanumfeature = numFeature
        self.datanumclass = numClass

   
    def findOptimalTree(self, minNumberForK, doNodeMinimization, terms):
        
        while True:
            
            if minNumberForK > math.ceil(math.log2(self.datanumfeature+1)):
                return False, False
            
            tree, root = self.inferTree(
                minNumberForK, doNodeMinimization, terms)
            
            if tree:
               
                break
            minNumberForK += 1
          
        return tree, root
   

    def minimizeNode(self, infer, tree1):

        tree = tree1
       
        infer.addConstraints_MaxLeaves()
        FMin = 1
        FMax = pow(2, infer.k)
        
        while FMin != FMax:
            nombreMaxFeuille = (int)((FMax + FMin) / 2)
            if infer.inferModel(nombreMaxFeuille):
                tmp = infer.getModel()
                element = self.distinguish(tmp)
                if len(element) == 0:
                  
                    tree = tmp
                    FMax = nombreMaxFeuille
                else:
                    
                    infer.add(element)
            else:
                FMin = nombreMaxFeuille + 1
        
        return tree
    

    def inferTree(self, k, doNodeMinimization, terms):
        
        infer = Infer.Mysolver(k, self.datanumfeature,
                               self.datanumclass, self.data, terms)
        
        while infer.inferModel(0):
           
            tree = infer.getModel()
            
            element = self.distinguish(tree)
            
            if len(element) == 0:
                
                if doNodeMinimization:
                    tree = self.minimizeNode(infer, tree)
                infer.simplifyTree(tree)
                root = infer.tree_root(tree)
               
                return tree, root
           
            infer.add(element)
       
        return False, False


    def inferTree1(self, k, doNodeMinimization, terms):
        root = False
        tree = False
       
        infer = Infer.Mysolver(k, self.datanumfeature,
                               self.datanumclass, self.data, terms)
        infer.addConstraints_MaxLeaves()
        
        FMin = 1
        FMax = pow(2, infer.k)
        while FMin != FMax:
            sign = False
            nombreMaxFeuille = (int)((FMax + FMin) / 2)
           
            while infer.inferModel(nombreMaxFeuille):
                tree = infer.getModel()
                
                element = self.distinguish(tree)
               
                if len(element) == 0:
                    tree = infer.getModel()
                    
                    infer.simplifyTree(tree)
                    root = infer.tree_root(tree)
                    FMax = nombreMaxFeuille
                    sign = True
                    break
                
                else:
                    tree = False
                    root = False
                   
                    infer.add(element)
            
            if sign is False:
               
                FMin = nombreMaxFeuille + 1
       
        return tree, root


    def distinguish(self, tree):
       
        for elem in self.data[1:]:
           
            pos = 1
            while True:
                feature = tree[pos]
                if feature < 0:
                  
                    if -feature-1 not in elem[-1]:
                        return elem
                    break
                if elem[0][feature] == 1:
                    pos = pos * 2 + 1
                else:
                    pos = pos * 2
        return []

    def Ptree(self, node):
       
        if node.left is None:
            return

        self.Ptree(node.left)

        self.Ptree(node.right)
