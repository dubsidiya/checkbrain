###
var a:=readlines('17-435.txt').Sel(x->x.Toi).ToA;
var m12:=a.Wh(x-> (abs(x)>=100)and(abs(x)<=999) and (abs(x) mod 100=12)).Min;
var r:=new List<integer>;
for var k:=0 to a.High-2 do
begin
  var t:=a[k:k+3]; 
  If (t.All(x->x>0) or t.All(x->x<0)) and (BigInteger(t.Min)*t.Max>m12*m12) then r.Add(t.min*t.Max);
end;
print(r.Cnt,r.Min)