// Автор: И.В.Свистун
##
uses school; 
 for var i:=2 to 10000 do 
    begin
      var n:=i.Divisors; 
      var k:=i.DivisorsCount;
      if (n.sum - i = i)then Println(i,k-1);
      end;
      