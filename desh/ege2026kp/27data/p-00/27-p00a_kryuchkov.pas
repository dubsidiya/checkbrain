// Автор: М. Крючков

## uses Turtle;

var t := Matrbyrow(ReadAllLines('27-p00a.txt').JoinToString
                  .ToReals(',').Batch(2));

DrawPoints(t.col(0), t.col(1));

var KL1 := t.Rows.Where(\(x,y) -> y>3);
var KL2 := t.Rows.Where(\(x,y) -> y<3);

var (k1x, k1y):=(0.0, 0.0);

var sumD := real.MaxValue;
foreach var (cx,cy) in KL1 do begin
	var sum1 := KL1.Sum(\(x,y) -> sqrt((cx-x)**2 + (cy-y)**2));
	if sum1 < sumD then 
      (sumD, k1x, k1y):=(sum1, cx, cy);
end;

var (k2x,k2y) := KL2.OrderBy(\(cx,cy) -> 
                 KL2.Sum(\(x,y) -> sqrt((cx-x)**2+(cy-y)**2))).First;

Println( floor((k1x+k2x)/2*10000), floor((k1y+k2y)/2*10000) );
