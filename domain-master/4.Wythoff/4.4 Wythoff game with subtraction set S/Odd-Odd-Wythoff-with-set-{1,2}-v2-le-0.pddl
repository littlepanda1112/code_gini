(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (<= ?v2 0)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (%= ?k 2 1))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (%= ?k 2 1))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (%= ?k 2 1)(>= ?v2 ?k) (or (= ?k 1) (= ?k 2)))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)


    