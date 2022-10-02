(define (problem blocks)
(:domain homework)
(:objects 
          b1  - box
          tb - tb3
          box_1 - boxlocation
          tblocation - tb3location
          sl - location
          boxstart - location
          tholder - tbholder
          crane - crane
          pickup - pickuppoint
          
          ;crane holer
          cholder - craneholder
          
          ;drop first
          tower - towerpoint
          
          ; multiple boxes
          b2 - box
          box_2 - boxlocation
          b3 - box
          box_3 - boxlocation
          
          flag - firstbox
          )
(:init (samelocation tblocation sl) (samelocation boxstart box_1) (is_first flag)
(not(samelocation sl boxstart)) (in tb tblocation) 
(crane_empty crane) (in b1 box_1) (box_clear b1) (tb3_empty tb) (pickup_empty pickup)

; dettach
(not(should_rev tb))
(not(samelocation pickup box_1))
(not(samelocation pickup tblocation))
(samelocation pickup pickup)
(in tb tblocation)
;pickup (crane)
(samelocation tblocation tholder)

; drop first

; multiple boxes
(in b2 box_2) (not(samelocation box_2 box_1)) (box_clear b2) (samelocation box_2 box_2)
(in b3 box_3) (not(samelocation box_3 box_1)) (box_clear b3) (samelocation box_3 box_3)

)
(:goal 
;(in b1 tholder)
;(and (in b1 tholder)
;(in tb sl  ))
;(in b1 pickup)

; crane pickup
;(in b1 cholder)


;drop first
;(in b1 tower)


;mutiple boxes
(and (in b1 tower) (box_on b2 b1) (box_on b3 b2))

)
)