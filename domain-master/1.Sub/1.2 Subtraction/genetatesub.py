import os

def generateSub1(a):
    a=str(a)
    filename = 'pddl1\Subtraction_game\OneValue\Subtraction-('+a+').pddl'
    fp = open(filename,'w') 
    fp.write('(define (domain Subtraction_game)'+'\n')
    fp.write('\t'+'(:objects ?v1)'+'\n')
    fp.write('\t'+'(:tercondition (and (>= ?v1 0) (< ?v1 '+a+') ))'+'\n')
    fp.write('\t'+'(:constraint (>= ?v1 0))'+'\n')
    fp.write('\t'+'(:action take'+'\n')
    fp.write('\t'+'\t'+':parameters (?k)'+'\n')
    fp.write('\t'+'\t'+':precondition (and (>= ?v1 ?k) (= ?k '+a+'))'+'\n')
    fp.write('\t'+'\t'+':effect (assign ?v1 (- ?v1 ?k)))'+'\n')
    fp.write(')')
    fp.close()
    return
def generateSub2(a,b):
    a=str(a)
    b=str(b)
    filename = 'pddl1\Subtraction_game\TwoValue\Subtraction-('+a+','+b+').pddl'
    fp = open(filename,'w') 
    fp.write('(define (domain Subtraction_game)'+'\n')
    fp.write('\t'+'(:objects ?v1)'+'\n')
    fp.write('\t'+'(:tercondition (and (>= ?v1 0) (< ?v1 '+a+') ))'+'\n')
    fp.write('\t'+'(:constraint (>= ?v1 0))'+'\n')
    fp.write('\t'+'(:action take'+'\n')
    fp.write('\t'+'\t'+':parameters (?k)'+'\n')
    fp.write('\t'+'\t'+':precondition (and (>= ?v1 ?k) (or (= ?k '+a+') (= ?k '+b+')))'+'\n')
    fp.write('\t'+'\t'+':effect (assign ?v1 (- ?v1 ?k)))'+'\n')
    fp.write(')')
    fp.close()
    return

def generateSub3(a,b,c):
    a=str(a)
    b=str(b)
    c=str(c)
    filename = 'pddl/Subtraction-('+a+','+b+','+c+').pddl'
    fp = open(filename,'w') 
    fp.write('(define (domain Subtraction_game)'+'\n')
    fp.write('\t'+'(:objects ?v1)'+'\n')
    fp.write('\t'+'(:tercondition (and (>= ?v1 0) (< ?v1 '+a+') ))'+'\n')
    fp.write('\t'+'(:constraint (>= ?v1 0))'+'\n')
    fp.write('\t'+'(:action take'+'\n')
    fp.write('\t'+'\t'+':parameters (?k)'+'\n')
    fp.write('\t'+'\t'+':precondition (and (>= ?v1 ?k) (or (= ?k '+a+') (= ?k '+b+') (= ?k '+c+')))'+'\n')
    fp.write('\t'+'\t'+':effect (assign ?v1 (- ?v1 ?k)))'+'\n')
    fp.write(')')
    fp.close()
    return

def generateSub4(a,b,c,d):
    a=str(a)
    b=str(b)
    c=str(c)
    d=str(d)
    filename = r'pddl1/Subtraction_game/Four10/Subtraction-('+a+','+b+','+c+','+d+').pddl'
    filename = r'pddl/Subtraction-('+a+','+b+','+c+','+d+').pddl'
    fp = open(filename,'w') 
    fp.write('(define (domain Subtraction_game)'+'\n')
    fp.write('\t'+'(:objects ?v1)'+'\n')
    fp.write('\t'+'(:tercondition (and (>= ?v1 0) (< ?v1 '+a+') ))'+'\n')
    fp.write('\t'+'(:constraint (>= ?v1 0))'+'\n')
    fp.write('\t'+'(:action take'+'\n')
    fp.write('\t'+'\t'+':parameters (?k)'+'\n')
    fp.write('\t'+'\t'+':precondition (and (>= ?v1 ?k) (or (= ?k '+a+') (= ?k '+b+') (= ?k '+c+') (= ?k '+d+')))'+'\n')
    fp.write('\t'+'\t'+':effect (assign ?v1 (- ?v1 ?k)))'+'\n')
    fp.write(')')
    fp.close()
    return


# for i in range (1,16):
#     generateSub1(i)

# for i in range(1,16):
#     for j in range (1,16):
#         if i < j:
#             generateSub2(i, j)


# for i in range(1,11):
#     for j in range (1,11):
#         for k in range (1,11):
#             if i < j < k:
#                 generateSub3(i, j, k)

for i in range(1,11):
    for j in range (1,11):
        for k in range (1,11):
            for l in range (1,11):
                if i < j < k < l:
                        generateSub4(i, j, k, l)