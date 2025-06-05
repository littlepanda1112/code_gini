import os


def getStrk(i):
    stri='?k'   
    while i >1:
        stri='(+ ?k %s)'%stri
        i=i-1
    return stri
def getStrl(i):
    stri='?l'   
    while i >1:
        stri='(+ ?l %s)'%stri
        i=i-1
    return stri

def generate_normal(l,m,v2):
    kstr=getStrk(l)
    lstr=getStrl(m)

    l=str(l)
    m=str(m)
    v2=str(v2)

    filename = os.path.dirname(__file__)+'\Wyt[%s,%s]v2-%s.pddl'%(l,m,v2)
    # filename = os.path.dirname(__file__)+'\st(lm)wythoff(l-1,m-1)v2-1.pddl'

    print(filename)
    content='''(define (domain Three-vectors-game)
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
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?l) (> ?l 0) (> ?k 0) (= %s %s))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    '''%(v2,kstr,lstr)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return


def generate_odd_odd(l,m,v2):
    kstr=getStrk(l)
    lstr=getStrl(m)

    l=str(l)
    m=str(m)
    v2=str(v2)

    filename = os.path.dirname(__file__)+'\Odd-Odd-Wyt[%s,%s]v2-%s.pddl'%(l,m,v2)

    print(filename)
    content='''(define (domain Three-vectors-game)
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
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?l) (> ?l 0) (> ?k 0) (= %s %s))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    '''%(v2,'%','%',kstr,lstr)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return


def generate_odd_even(l,m,v2):
    kstr=getStrk(l)
    lstr=getStrl(m)

    l=str(l)
    m=str(m)
    v2=str(v2)

    filename = os.path.dirname(__file__)+'\Odd-Even-Wyt[%s,%s]v2-%s.pddl'%(l,m,v2)

    print(filename)
    content='''(define (domain Three-vectors-game)
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
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?l) (> ?l 0) (> ?k 0) (= %s %s))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    '''%(v2,'%','%',kstr,lstr)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return


def generate_even_even(l,m,v2):
    kstr=getStrk(l)
    lstr=getStrl(m)

    l=str(l)
    m=str(m)
    v2=str(v2)

    filename = os.path.dirname(__file__)+'\Even-Even-Wyt[%s,%s]v2-%s.pddl'%(l,m,v2)

    print(filename)
    content='''(define (domain Three-vectors-game)
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
        :precondition (and (>= ?v1 ?k) (>= ?v2 ?l) (> ?l 0) (> ?k 0) (= %s %s))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    '''%(v2,'%','%',kstr,lstr)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return


def generate(l,m,v2):
    generate_normal(l,m,v2)
    generate_odd_even(l,m,v2)
    generate_odd_odd(l,m,v2)
    generate_even_even(l,m,v2)

for v2 in range (0,6):
    for l in range (1,6):
        for m in range (1,6):
                if l!=m:
                    generate(l,m,v2)
