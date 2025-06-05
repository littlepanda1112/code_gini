import os

def generate(k1,v3max):
    filename = os.path.dirname(__file__)+'\Three-piled-%s-slow-nim-v3le%s.pddl'%(k1,v3max)
    print(filename)
    content='''(define (domain three-piled-nim)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (= ?v1 0) (= ?v2 0) (= ?v3 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v3 0) (<= ?v3 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (<= ?k %s))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (<= ?k %s))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v3 ?k) (> ?k 0) (<= ?k %s))
        :effect (assign ?v3 (- ?v3 ?k)))
)
    '''%(v3max,k1,k1,k1)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return








for v3max in range (1,6):
    for k in range (1,31):
        generate(k,v3max)

