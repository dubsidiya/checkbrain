// Автор: М. Крючков

## uses Turtle;

var t := Matrbyrow(ReadAllLines('27-p00b.txt').JoinToString
                  .ToReals(',').Batch(2));

DrawPoints(t.col(0), t.col(1));
 
var KL0 := t.Rows.Where(\(x,y) -> y in 0..3);
var KL1 := t.Rows.Where(\(x,y) -> y in 4..7);
var KL2 := t.Rows.Where(\(x,y) -> y in 7..10);

var (kx, ky) := (|0.0|*3, |0.0|*3);

(kx[0],ky[0]) := KL0.OrderBy(\(cx,cy) -> 
                   KL0.Sum(\(x,y) -> sqrt((cx-x)**2+(cy-y)**2))).First;
(kx[1],ky[1]) := KL1.OrderBy(\(cx,cy) -> 
                   KL1.Sum(\(x,y) -> sqrt((cx-x)**2+(cy-y)**2))).First;
(kx[2],ky[2]) := KL2.OrderBy(\(cx,cy) -> 
                   KL2.Sum(\(x,y) -> sqrt((cx-x)**2+(cy-y)**2))).First;

Println( floor(kx.Average*10000), floor(ky.Average*10000) );
