// Автор: И.В.Свистун
##
uses school; 
var c:=(33333..55555)
      .Where( t -> (t mod 6<>0)and (t mod 7<>0) and (t mod 8<>0)
      and(t.digits[0].isOdd) and (t.digits[1].isOdd)and(t.digits[2].isEven) 
      and (t.digits[3].isOdd)and (t.digits[4].isEven));
var k:=c.Count.Println;
var d:=(c.Last- c.First).print
      
     
 