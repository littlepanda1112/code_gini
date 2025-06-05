import os

def generate_normal(k1):
    k1=str(k1)
    
    
    filename = os.path.dirname(__file__)+'\Wythoff-with-set-{%s}.pddl'%(k1)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (= ?k %s))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%(k1)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_odd(k1):
    k1=str(k1)
    

    filename = os.path.dirname(__file__)+'\Odd-Odd-Wythoff-with-set-{%s}.pddl'%(k1)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) ))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (%s= ?k 2 1))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (%s= ?k 2 1))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (%s= ?k 2 1)(>= ?v2 ?k) (= ?k %s))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%('%','%','%',k1)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_even(k1,v2max):
    k1=str(k1)
    
    
    filename = os.path.dirname(__file__)+'\Odd-Even-Wythoff-with-set-{%s}-v2-le-%s.pddl'%(k1,v2max)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (<= ?v2 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (%s= ?k 2 1))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (%s= ?k 2 0))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (= ?k %s))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%(v2max,'%','%',k1)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_even_even(k1):
    k1=str(k1)
    
    
    filename = os.path.dirname(__file__)+'\Even-Even-Wythoff-with-set-{%s}.pddl'%(k1)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (%s= ?k 2 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (%s= ?k 2 0))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (%s= ?k 2 0) (>= ?v2 ?k) (= ?k %s))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%('%','%','%',k1)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return
def generate(k1):
    generate_normal(k1)
    # generate_odd_even(k1,v2max)
    generate_odd_odd(k1)
    generate_even_even(k1)

for v2max in range (0,6):
    for k1 in range (1,6):
                generate(k1)
