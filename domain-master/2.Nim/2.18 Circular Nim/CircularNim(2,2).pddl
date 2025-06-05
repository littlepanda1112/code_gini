(define (domain CircularNIm)
	(:objects ?v1 ?v2)
	(:tercondition (and (= ?v1 0) (= ?v2 0) ))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) ))
    (:action take1
        :parameters (?k1 ?k2)
        :precondition (and (>= ?v1 ?k1) (>= ?v2 ?k2) (>= ?k1 0) (>= ?k2 0) (>= (+ ?k1 ?k2) 1))
        :effect (and (assign ?v1 (- ?v1 ?k1)) (assign ?v2 (- ?v2 ?k2))))
)