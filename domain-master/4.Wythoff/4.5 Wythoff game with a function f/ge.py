import os



def generate_normal(i,v2max):
    i=str(i)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Wyt-with-function(f(k)=k+%s)-v2-le-%s.pddl'%(i,v2max)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (<= ?v2 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%(v2max,i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_odd(i,v2max):
    i=str(i)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Odd-Odd-Wyt-with-function(f(k)=k+%s)-v2-le-%s.pddl'%(i,v2max)
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
        :precondition (and (>= ?v2 ?k) (> ?k 0) (%s= ?k 2 1))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%(v2max,'%','%',i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_even(i,v2max):
    i=str(i)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Odd-Even-Wyt-with-function(f(k)=k+%s)-v2-le-%s.pddl'%(i,v2max)
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
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%(v2max,'%','%',i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_even_even(i,v2max):
    i=str(i)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Even-Even-Wyt-with-function(f(k)=k+%s)-v2-le-%s.pddl'%(i,v2max)
    print(filename)
    content='''(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (<= ?v2 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (%s= ?k 2 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (%s= ?k 2 0))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%(v2max,'%','%',i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate(k1,v2max):
    generate_normal(k1,v2max)
    generate_odd_even(k1,v2max)
    generate_odd_odd(k1,v2max)
    generate_even_even(k1,v2max)


for v2max in range (0,6):
    for i in range (0,6):
        generate(i,v2max)
