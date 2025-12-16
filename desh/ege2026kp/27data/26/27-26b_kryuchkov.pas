// Автор: М. Крючков
##
// uses Turtle;
var t := Matrbyrow(ReadAllLines('27-26b.txt').Skip(1).JoinToString
                  .ToReals(',').Batch(3));
var n := t.RowCount;

//DrawPoints(t.col(0), t.col(1));

var k1:=t.rows.where(\(x,y,h) -> (x in -100..0) and (y in 0..100));
var k2:=t.rows.where(\(x,y,h) -> (x in -250..-50) and (y in -150..-50));
var k3:=t.rows.where(\(x,y,h) -> (x in 100..200) and (y in -100..100));

var (d1, k1x, k1y) :=
   k1.select(\(x1, y1, h1) ->
            (k1.Sum(\(x,y,h) -> h*sqrt((x-x1)**2 + (y-y1)**2)), x1, y1)
   ).order.First;
var (d2, k2x, k2y) :=
   k2.select(\(x2, y2, h2) ->
           (k2.Sum(\(x,y,h) -> h*sqrt((x-x2)**2 + (y-y2)**2)), x2, y2)
   ).order.First;
var (d3, k3x, k3y) :=
   k3.select(\(x3, y3, h3) ->
           (k3.Sum(\(x,y,h) -> h*sqrt((x-x3)**2 + (y-y3)**2)), x3, y3)
   ).order.First;
   
println('Центроиды:'); 
println(k1x, k1y);
println(k2x, k2y);
println(k3x, k3y);
println('Ответ:');
println(integer((k1x+k2x+k3x)/3*100000), integer((k1y+k2y+k3y)/3*100000));
