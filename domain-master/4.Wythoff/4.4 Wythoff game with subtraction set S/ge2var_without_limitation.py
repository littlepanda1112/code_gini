import os

def generate_normal(k1,k2):
    k1=str(k1)
    k2=str(k2)
    filename = os.path.dirname(__file__)+'\Wythoff-with-set-{%s,%s}.pddl'%(k1,k2)
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
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (or (= ?k %s) (= ?k %s)))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%(k1,k2)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_odd(k1,k2):
    k1=str(k1)
    k2=str(k2)
    filename = os.path.dirname(__file__)+'\Odd-Odd-Wythoff-with-set-{%s,%s}.pddl'%(k1,k2)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0)))
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
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (or (= ?k %s) (= ?k %s)))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%('%','%',k1,k2)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_even(k1,k2):
    k1=str(k1)
    k2=str(k2)
    filename = os.path.dirname(__file__)+'\Odd-Even-Wythoff-with-set-{%s,%s}.pddl'%(k1,k2)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0)))
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
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (or (= ?k %s) (= ?k %s)))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%('%','%',k1,k2)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_even_even(k1,k2):
    k1=str(k1)
    k2=str(k2)
    filename = os.path.dirname(__file__)+'\Even-Even-Wythoff-with-set-{%s,%s}.pddl'%(k1,k2)
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
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (or (= ?k %s) (= ?k %s)))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%('%','%',k1,k2)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return
def generate(k1,k2):
    generate_normal(k1,k2)
    generate_odd_even(k1,k2)
    generate_odd_odd(k1,k2)
    generate_even_even(k1,k2)

for i in range (1,6):
    for j in range (1,6):
            if (i<j):
                generate(i,j)
# generate(1,1)