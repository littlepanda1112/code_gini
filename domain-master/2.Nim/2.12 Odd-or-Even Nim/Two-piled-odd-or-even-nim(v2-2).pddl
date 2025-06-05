(define (domain odd-or-even-nim)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (or (and (= ?v2 0) (= ?v3 0)) (and (= ?v1 0)(<= ?v2 1)(<= ?v3 1)) ) )
	(:constraint (and (>= ?v2 0)(>= ?v3 0)(>= ?v1 0)(<= ?v1 2)(<= ?v2 2)(<= ?v3 2) ))
	(:action specify
		:parameters (?k)
		:precondition (and (= ?v1 2)(or(= ?k 0)(= ?k 1)))
		:effect (assign ?v1 ?k) )
	(:action take1-then-even
		:parameters (?k)
		:precondition (and (!= ?v1 2) (>= ?k 1) (%= ?k 2 ?v1)(>= ?v2 ?k))
		:effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v1 0)) )
	(:action take1-then-odd
		:parameters (?k)
		:precondition (and (!= ?v1 2) (>= ?k 1) (%= ?k 2 ?v1)(>= ?v2 ?k))
		:effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v1 1)) )
	(:action take2-then-even
		:parameters (?k)
		:precondition (and (!= ?v1 2) (>= ?k 1) (%= ?k 2 ?v1)(>= ?v3 ?k))
		:effect (and (assign ?v3 (- ?v3 ?k)) (assign ?v1 0)) )
	(:action take2-then-odd
		:parameters (?k)
		:precondition (and (!= ?v1 2) (>= ?k 1) (%= ?k 2 ?v1)(>= ?v3 ?k))
		:effect (and (assign ?v3 (- ?v3 ?k)) (assign ?v1 1)) )
)