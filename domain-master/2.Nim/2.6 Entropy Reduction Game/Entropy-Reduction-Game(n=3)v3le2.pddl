(define (domain Entropy-Reduction-Game)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (<= (- ?v2 ?v1) 1) (<= (- ?v1 ?v2) 1) (<= (- ?v3 ?v2) 1) (<= (- ?v2 ?v3) 1) (<= (- ?v1 ?v3) 1) (<= (- ?v3 ?v1) 1)))
    (:constraint (and (>= ?v1 1) (>= ?v2 1) (>= ?v3 1) (<= ?v3 2)))
    (:action take1
        :parameters (?k1 ?k2)
        :precondition (or (and (= ?k1 2) (> ?v1 ?v2) (> ?k2 0) (> (- ?v1 ?v2) ?k2)) (and (= ?k1 3) (> ?v1 ?v3) (> ?k2 0) (> (- ?v1 ?v3) ?k2)))
        :effect (and (assign ?v1 (- ?v1 ?k2)) (when (= ?k1 2) (assign ?v2 (+ ?v2 ?k2))) (when (= ?k1 3) (assign ?v3 (+ ?v3 ?k2)))))
    (:action take2
        :parameters (?k1 ?k2)
        :precondition (or (and (= ?k1 1) (> ?v2 ?v1) (> ?k2 0) (> (- ?v2 ?v1) ?k2)) (and (= ?k1 3) (> ?v2 ?v3) (> ?k2 0) (> (- ?v2 ?v3) ?k2)))
        :effect (and (assign ?v2 (- ?v2 ?k2)) (when (= ?k1 1) (assign ?v1 (+ ?v1 ?k2))) (when (= ?k1 3) (assign ?v3 (+ ?v3 ?k2)))))
    (:action take3
        :parameters (?k1 ?k2)
        :precondition (or (and (= ?k1 1) (> ?v3 ?v1) (> ?k2 0) (> (- ?v3 ?v1) ?k2)) (and (= ?k1 2) (> ?v3 ?v2) (> ?k2 0) (> (- ?v3 ?v2) ?k2)))
        :effect (and (assign ?v3 (- ?v3 ?k2)) (when (= ?k1 1) (assign ?v1 (+ ?v1 ?k2))) (when (= ?k1 2) (assign ?v2 (+ ?v2 ?k2)))))
)