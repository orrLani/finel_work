(define (problem blocks)
(:domain homework)
(:objects 
          ; objects
          tb - tb3      ; turtle bot`object
          crane - crane     ;crane object
          b1  - box     ; box 1
          b2 - box      ; box 2
          b3 - box      ; box 3
          
          
          ; locations
          tblocation - tb3location      ; turtle bot locations
          start_location - location     ; start location for turtlebot
          boxstart - location           ; ?
          tholder - tbholder            ; trutlebot holder (grasper, location to make sure we holding 1 box)
          pickup - pickuppoint          ;pickup location (where crane picks up box)
          cholder - craneholder         ; crane grasper
          tower - towerpoint            ; location to build tower on
          
          box_1 - boxlocation  ; box 1 location
          box_2 - boxlocation  ; box 2 location
          box_3 - boxlocation  ; box 3 location
          
          
          ;drop first
          
          flag - firstbox
)
          
          
(:init (samelocation tblocation start_location) (samelocation boxstart box_1) (is_first flag)
(not(samelocation start_location boxstart)) (in tb tblocation) 
(crane_empty crane) (in b1 box_1) (box_clear b1) (tb3_empty tb) (pickup_empty pickup)
(box_clear tower)
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