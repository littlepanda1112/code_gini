(define (domain odd-or-even-nim)
	(:objects ?v1 ?v2)
	(:tercondition (or (= ?v2 0) (and (= ?v1 0)(= ?v2 1))) )
	(:constraint (and (>= ?v2 0) (>= ?v1 0) (<= ?v1 2)) )
	(:action specify
		:parameters (?k)
		:precondition (and (= ?v1 2)(or(= ?k 0)(= ?k 1)))
		:effect (assign ?v1 ?k) )
	(:action take-then-even
		:parameters (?k)
		:precondition (and (!= ?v1 2) (>= ?k 1) (%= ?k 2 ?v1)(>= ?v2 ?k))
		:effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v1 0)) )
	(:action take-then-odd
		:parameters (?k)
		:precondition (and (!= ?v1 2) (>= ?k 1) (%= ?k 2 ?v1)(>= ?v2 ?k))
		:effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v1 1)) )
)

