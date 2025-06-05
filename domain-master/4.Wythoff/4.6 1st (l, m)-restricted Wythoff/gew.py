import os

def generate_normal(l,m):
    l=str(l)
    m=str(m)

    filename = os.path.dirname(__file__)+'\(l,m)-1st-wythoff(l-%s,m-%s).pddl'%(l,m)
    # filename = os.path.dirname(__file__)+'\st(lm)wythoff(l-1,m-1)v2-1.pddl'

    print(filename)
    content='''(define (domain Wythoff-Game-k-l-limited)
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
		:precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (> ?k 0) (or (and (>= ?v1 ?v2) (>= (- ?v1 ?k) %s) (>= (- ?v2 ?k) %s)) (and (>= ?v2 ?v1) (>= (- ?v2 ?k) %s) (>= (- ?v1 ?k) %s))))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%(m,l,m,l)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_odd(l,m):
    l=str(l)
    m=str(m)
    

    filename = os.path.dirname(__file__)+'\(l,m)-1st-Odd-Odd-wythoff(l-%s,m-%s).pddl'%(l,m)
    # filename = os.path.dirname(__file__)+'\st(lm)wythoff(l-1,m-1)v2-1.pddl'

    print(filename)
    content='''(define (domain Wythoff-Game-k-l-limited)
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
		:precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (> ?k 0) (or (and (>= ?v1 ?v2) (>= (- ?v1 ?k) %s) (>= (- ?v2 ?k) %s)) (and (>= ?v2 ?v1) (>= (- ?v2 ?k) %s) (>= (- ?v1 ?k) %s))))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%('%','%',m,l,m,l)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_odd_even(l,m):
    l=str(l)
    m=str(m)
    

    filename = os.path.dirname(__file__)+'\(l,m)-1st-Odd-Even-wythoff(l-%s,m-%s).pddl'%(l,m)
    # filename = os.path.dirname(__file__)+'\st(lm)wythoff(l-1,m-1)v2-1.pddl'

    print(filename)
    content='''(define (domain Wythoff-Game-k-l-limited)
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
		:precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (> ?k 0) (or (and (>= ?v1 ?v2) (>= (- ?v1 ?k) %s) (>= (- ?v2 ?k) %s)) (and (>= ?v2 ?v1) (>= (- ?v2 ?k) %s) (>= (- ?v1 ?k) %s))))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%('%','%',m,l,m,l)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate_even_even(l,m):
    l=str(l)
    m=str(m)
    

    filename = os.path.dirname(__file__)+'\(l,m)-1st-Even-Even-wythoff(l-%s,m-%s).pddl'%(l,m)
    # filename = os.path.dirname(__file__)+'\st(lm)wythoff(l-1,m-1)v2-1.pddl'

    print(filename)
    content='''(define (domain Wythoff-Game-k-l-limited)
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
		:precondition (and (>= ?v1 ?k) (>= ?v2 ?k) (> ?k 0) (or (and (>= ?v1 ?v2) (>= (- ?v1 ?k) %s) (>= (- ?v2 ?k) %s)) (and (>= ?v2 ?v1) (>= (- ?v2 ?k) %s) (>= (- ?v1 ?k) %s))))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)
    '''%('%','%',m,l,m,l)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

def generate(l,m):
    generate_normal(l,m)
    generate_odd_even(l,m)
    generate_odd_odd(l,m)
    generate_even_even(l,m)
    	
for l in range (0,6):
    for m in range (0,6):
    		if l > m:
    			generate(l,m)

