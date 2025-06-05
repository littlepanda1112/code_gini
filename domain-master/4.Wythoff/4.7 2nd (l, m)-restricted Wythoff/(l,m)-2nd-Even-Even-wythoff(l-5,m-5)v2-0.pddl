(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (<= ?v2 0)))
    (:action take1
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (>= ?k 0) (%= ?k 2 0) (%= ?l 2 0) (>= ?v2 ?l) (>= ?l 0)  (> (+ ?k ?l) 0) (or (and (< (- ?k ?l) 5) (> ?k ?l)) (and (< (- ?l ?k) 5) (> ?l ?k))  (> 5 ?k)  (> 5 ?l) ))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    