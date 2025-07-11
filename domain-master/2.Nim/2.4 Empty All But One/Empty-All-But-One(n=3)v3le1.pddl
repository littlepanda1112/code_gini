(define (domain Empty-All-But-One)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (< ?v1 3) (< ?v2 3) (< ?v3 3)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v3 0) (<= ?v3 1)))
    (:action keep1
        :parameters (?k1 ?k2 ?k3)
        :precondition (and (> ?k1 0) (> ?k2 0) (> ?k3 0) (<= (+ ?k1 (+ ?k2 ?k3)) ?v1))
        :effect (and (assign ?v1 ?k1) (assign ?v2 ?k2) (assign ?v3 ?k3)))
    (:action keep2
        :parameters (?k1 ?k2 ?k3)
        :precondition (and (> ?k1 0) (> ?k2 0) (> ?k3 0) (<= (+ ?k1 (+ ?k2 ?k3)) ?v2))
        :effect (and (assign ?v1 ?k1) (assign ?v2 ?k2) (assign ?v3 ?k3)))
    (:action keep3
        :parameters (?k1 ?k2 ?k3)
        :precondition (and (> ?k1 0) (> ?k2 0) (> ?k3 0) (<= (+ ?k1 (+ ?k2 ?k3)) ?v3))
        :effect (and (assign ?v1 ?k1) (assign ?v2 ?k2) (assign ?v3 ?k3)))
)