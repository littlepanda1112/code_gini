(define (domain CircularNIm)
	(:objects ?v1)
	(:tercondition (and (= ?v1 0) ))
    (:constraint (and (>= ?v1 0) ))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0))
        :effect (and (assign ?v1 (- ?v1 ?k))))
)