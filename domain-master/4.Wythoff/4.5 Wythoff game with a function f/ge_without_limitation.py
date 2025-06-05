import os

def generate_normal(i,v2max):
    i=str(i)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\Wyt-with-function(f(k)=k+%s).pddl'%(i)
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
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%(i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_normal(i):
    i=str(i)
    filename = os.path.dirname(__file__)+'\Wyt-with-function(f(k)=k+%s).pddl'%(i)
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
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%(i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_odd(i):
    i=str(i)
    filename = os.path.dirname(__file__)+'\Odd-Odd-Wyt-with-function(f(k)=k+%s).pddl'%(i)
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
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%('%','%',i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_even(i):
    i=str(i)
    filename = os.path.dirname(__file__)+'\Odd-Even-Wyt-with-function(f(k)=k+%s).pddl'%(i)
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
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%('%','%',i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_even_even(i):
    i=str(i)
    filename = os.path.dirname(__file__)+'\Even-Even-Wyt-with-function(f(k)=k+%s).pddl'%(i)
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
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0)  (>= ?v2 ?l) (> ?l 0) (>= ?l ?k) (> (+ ?k %s) ?l ) )
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))

)
    '''%('%','%',i)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate(k1):
    generate_normal(k1)
    generate_odd_even(k1)
    generate_odd_odd(k1)
    generate_even_even(k1)
for i in range (0,6):
        generate(i)
