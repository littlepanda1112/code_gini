(define (domain chomp-game)
    (:objects ?v1 ?v2 ?v3)
    (:tercondition (and (= ?v1 1) (= ?v2 0) (= ?v3 0) (<= ?v3 1)))
    (:constraint (and (>= ?v1 1) (>= ?v2 0) (>= ?v3 0)))
    (:action eat1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 1))
        :effect (and  (assign ?v1 (- ?k 1)) (when (>= ?v2 ?k) (assign ?v2 (- ?k 1))) (when (>= ?v3 ?k) (assign ?v3 (- ?k 1))) ))
    (:action eat2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0))
        :effect (and  (assign ?v2 (- ?k 1)) (when (>= ?v3 ?k) (assign ?v3 (- ?k 1))) ))
    (:action eat3
        :parameters (?k)
        :precondition (and (>= ?v3 ?k) (> ?k 0))
        :effect (assign ?v3 (- ?k 1)))
)
