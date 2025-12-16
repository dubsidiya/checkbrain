// Автор: И.В.Свистун
##
uses school;  
  for var i:=190201 to 190280 do 
  begin
    var ch:=0;
    for var j:=1 to i.Divisors.Count-1 do
      if i.Divisors[j].IsEven then ch+=1; 
    if ch=4 then i.Divisors.Where(t -> t.IsEven).SortedDescending.Println;
  end;