// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=300000000;
while (ch<5) do
Begin   
  var f:=n.divisors.Where(l -> l>=189).Where(v -> v.Digits.sum=17).ToArray;
  if (f.count>=5)then 
    begin 
    var f1:=f[^5:];
    println(f1[0],f.count); 
    ch+=1;  
    end;
  n-=1;
end
// в ответ записываем пары в обратном порядке