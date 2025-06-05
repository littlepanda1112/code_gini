import os

def generate_noraml(k,v2max):
    k=str(k)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Monotonic-l(%s)-Diet-wythoff-v2-le-%s.pddl'%(k,v2max)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v1 ?v2) (<= ?v2 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v1 (+ ?v2 ?k)) (<= ?k %s))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (> ?k 0) (<= ?k %s) (>= ?v2 ?k) )
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (> ?k 0) (<= ?k %s)(>= ?v1 ?k) (>= ?v2 ?k))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%(v2max,k,k,k)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_odd(k,v2max):
    k=str(k)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Odd-Odd-Monotonic-l(%s)-Diet-wythoff-v2-le-%s.pddl'%(k,v2max)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v1 ?v2) (<= ?v2 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v1 (+ ?v2 ?k)) (<= ?k %s)(%s= ?k 2 1))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (> ?k 0) (<= ?k %s) (%s= ?k 2 1) (>= ?v2 ?k))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (> ?k 0) (%s= ?k 2 1) (<= ?k %s)(>= ?v1 ?k) (>= ?v2 ?k))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%(v2max,k,'%',k ,'%','%',k)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_even(k,v2max):
    k=str(k)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Odd-Even--Monotonic-l(%s)-Diet-wythoff-v2-le-%s.pddl'%(k,v2max)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v1 ?v2) (<= ?v2 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v1 (+ ?v2 ?k)) (<= ?k %s) (%s= ?k 2 1))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (> ?k 0) (<= ?k %s) (%s= ?k 2 0) (>= ?v2 ?k))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (> ?k 0) (<= ?k %s)(>= ?v1 ?k) (>= ?v2 ?k))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%(v2max,k,'%',k,'%',k)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_even_even(k,v2max):
    k=str(k)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Even-Even--Monotonic-l(%s)-Diet-wythoff-v2-le-%s.pddl'%(k,v2max)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v1 ?v2) (<= ?v2 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v1 (+ ?v2 ?k)) (<= ?k %s) (%s= ?k 2 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (> ?k 0) (<= ?k %s) (%s= ?k 2 0) (>= ?v2 ?k))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (> ?k 0)(%s= ?k 2 0) (<= ?k %s)(>= ?v1 ?k) (>= ?v2 ?k))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%(v2max,k,'%',k,'%','%',k)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate(k,v2max):
    # generate_noraml(k,v2max)
    # generate_odd_even(k,v2max)
    generate_odd_odd(k,v2max)
    generate_even_even(k,v2max)
# my=3
for v2max in range (0,6):
    for k in range(1,6):
            generate(k,v2max)

