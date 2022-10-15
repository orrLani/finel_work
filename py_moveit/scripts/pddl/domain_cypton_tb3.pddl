( define (domain homework)

(:requirements :typing :strips )

(:types
	location physobj firstbox - object
	box crane tb3 - physobj
	tbholder tblocations - location
	craneholder  pickuppoint boxlocation tb3location towerpoint startlocation  - tblocations
	box - towerpoint
	
	
)
; box might need attached predicate
(:predicates
	(box_clear ?x - towerpoint)                        ;is something on top of the box
	(box_on ?x - box ?y - towerpoint)                  ;is the box on another box (x on top of y)
	(in ?x - physobj ?y - location)             ;location of object (x in location y)
	(samelocation ?x - location ?y - location)  ;are location equal (might be a problem)
	(tb3_empty ?x - tb3)                        ;is trutle bot carrying a box?
	(crane_empty ?x - crane)                    ;is the crane carrying a box?

    ; firstbox predicates
    
    (is_first ?x - firstbox)                    ;first box to be handled?
    (pickup_empty ?x - pickuppoint)             ;does the pickup location contains a box?
    (should_rev ?x - tb3)                       ; should the turtlebot reverse? (to not interrupt the crane)
)

(:action move
:parameters (?x - tb3 ?y - tblocations ?z - tblocations)
:precondition  (and(not(samelocation  ?y ?z)) (in ?x ?z )) 
:effect (and (not(in ?x ?z))  (in ?x ?y)  )
)

(:action Reverse
:parameters (?x - tb3 ?y - tblocations ?z - pickuppoint)
:precondition  (and(not(samelocation  ?y ?z)) (in ?x ?z ) (not(samelocation ?y ?z)) (should_rev ?x)) 
:effect (and (not(in ?x ?z))  (in ?x ?y) (not(should_rev ?x))  )
)


(:action attach
:parameters (?x - box ?y - boxlocation ?z - tb3location ?t - tb3 ?h - tbholder)
:precondition (and   (in ?x ?y) (tb3_empty ?t) (box_clear ?x) (in ?t ?y))
:effect (and (not(in ?x ?y )) (not(tb3_empty ?t )) (in ?x ?h))
)



(:action dettach
:parameters (?x - box ?y - pickuppoint ?t - tb3 ?h - tbholder )
:precondition (and (not (tb3_empty ?t ))  (in ?x ?h) (in ?t ?y)  (pickup_empty ?y) ) 
:effect (and (in ?x ?y) (in ?t ?y) (tb3_empty ?t) (not(in ?x ?h)) (not(pickup_empty ?y)) (should_rev ?t) )
)



(:action pickup
:parameters (?x - box  ?z - pickuppoint ?c - crane ?h - craneholder ?t - tb3)
:precondition (and (box_clear ?x) (in ?x ?z )  (crane_empty ?c) (not(in ?t ?z)) (not(should_rev ?t)) )
:effect (and (not(crane_empty ?c)) (not(in ?x ?z))  
		(in ?x ?h) (pickup_empty ?z))
)



;(:action firstdrop
;:parameters (?b1 - box ?y - towerpoint ?c - crane ?h - craneholder ?x - firstbox)
;:precondition (and (not(crane_empty ?c )) (in ?b1 ?h ) (is_first ?x) )
;:effect (and (in ?b1 ?y ) (crane_empty ?c ) (not(in ?b1 ?h )) (not(is_first ?x) ))
;)


(:action drop
:parameters (?b2 - box ?y - towerpoint ?c - crane ?h - craneholder)
:precondition (and   (in ?b2 ?h ) (not(crane_empty ?c )) (box_clear ?y ) )
:effect (and (in ?b2 ?y ) (crane_empty ?c ) (not(box_clear ?y )) (not(in ?b2 ?h )) (box_on ?b2 ?y))
)


)