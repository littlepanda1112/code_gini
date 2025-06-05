import os

def generateTakeAway(i):
    i=str(i)
    filename = 'pddl1\Take-away\Take-away-'+i+'.pddl'
    fp = open(filename,'w') 
    fp.write('(define (domain Take-away-' +i+')'+'\n')
    fp.write('\t'+'(:objects ?v1)'+'\n')
    fp.write('\t'+'(:tercondition (= ?v1 0))'+'\n')
    fp.write('\t'+'(:constraint (>= ?v1 0))'+'\n')
    fp.write('\t'+'(:action take'+'\n')
    fp.write('\t'+'\t'+':parameters (?k)'+'\n')
    fp.write('\t'+'\t'+':precondition (and (>= ?k 1) (<= ?k '+i+') (>= ?v1 ?k))'+'\n')
    fp.write('\t'+'\t'+':effect (assign ?v1 (- ?v1 ?k)))'+'\n')
    fp.write(')')
    fp.close()
    return

for i in range (1,31):
    generateTakeAway(i)