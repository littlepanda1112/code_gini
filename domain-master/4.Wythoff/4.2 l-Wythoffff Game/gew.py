import os


def generate_noraml(k):
    k = str(k)
    filename = os.path.dirname(__file__)+'\l(%s)-wythoff.pddl' % (k)
    print(filename)
    content = '''(define (domain a-Wythoff_game)
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
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v2 ?l) (> ?l 0)  (or (and (< (- ?k ?l) %s) (>= ?k ?l)) (and (< (- ?l ?k) %s) (>=  ?l ?k))))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    ''' % (k, k)
    fp = open(filename, 'w')

    fp.write(content)

    fp.close()
    return


def generate_odd_odd(k):
    k = str(k)

    filename = os.path.dirname(__file__)+'\Odd-Odd-l(%s)-wythoff.pddl' % (k)
    print(filename)
    content = '''(define (domain a-Wythoff_game)
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
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v2 ?l) (> ?l 0)  (or (and (< (- ?k ?l) %s) (>= ?k ?l)) (and (< (- ?l ?k) %s) (>=  ?l ?k))))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    ''' % ('%', '%', k, k)
    fp = open(filename, 'w')

    fp.write(content)

    fp.close()
    return


def generate_odd_even(k):
    k = str(k)

    filename = os.path.dirname(__file__)+'\Odd-Even-l(%s)-wythoff.pddl' % (k)
    print(filename)
    content = '''(define (domain a-Wythoff_game)
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
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v2 ?l) (> ?l 0)  (or (and (< (- ?k ?l) %s) (>= ?k ?l)) (and (< (- ?l ?k) %s) (>=  ?l ?k))))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    ''' % ('%', '%', k, k)
    fp = open(filename, 'w')

    fp.write(content)

    fp.close()
    return


def generate_even_even(k):
    k = str(k)

    filename = os.path.dirname(__file__)+'\Even-Even-l(%s)-wythoff.pddl' % (k)
    print(filename)
    content = '''(define (domain a-Wythoff_game)
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
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v2 ?l) (> ?l 0)  (or (and (< (- ?k ?l) %s) (>= ?k ?l)) (and (< (- ?l ?k) %s) (>=  ?l ?k))))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    ''' % ('%', '%', k, k)
    fp = open(filename, 'w')

    fp.write(content)

    fp.close()
    return


def generate(k):
    generate_noraml(k)
    generate_odd_even(k)
    generate_odd_odd(k)
    generate_even_even(k)


# my=3
for k in range(1, 6):
    generate(k)
