// Автор: М. Крючков

## uses Turtle;

var t := Matrbyrow(ReadAllLines('27-p00b.txt').JoinToString
                  .ToReals(',').Batch(2));

DrawPoints(t.col(0), t.col(1));
 
var KL0 := t.Rows.Where(\(x,y) -> y in 0..3);
var KL1 := t.Rows.Where(\(x,y) -> y in 4..7);
var KL2 := t.Rows.Where(\(x,y) -> y in 7..10);

var kx := |1.5, 5.5, 3.5|;
var ky := |1.5, 5.5, 8.5|;

loop 10 do begin

	var avX := KL0.Average(\(x,y) -> x);
	var avY := KL0.Average(\(x,y) -> y);

	(kx[0], ky[0]) := KL0.OrderBy(\(x,y) -> 
                         sqrt((avX-x)**2+(avY-y)**2)).First;

	avX := KL1.Average(\(x,y) -> x);
	avY := KL1.Average(\(x,y) -> y);
	(kx[1], ky[1]) := KL1.OrderBy(\(x,y) -> 
                         sqrt((avX-x)**2+(avY-y)**2)).First;

	avX := KL2.Average(\(x,y) -> x);
	avY := KL2.Average(\(x,y) -> y);
	(kx[2], ky[2]) := KL2.OrderBy(\(x,y) -> 
                         sqrt((avX-x)**2+(avY-y)**2)).First;
end;

Println( floor(kx.Average*10000), floor(ky.Average*10000) );
