// Автор: И.В.Свистун
##
uses school; 
var m:=400000; var ch:=0; var v:=0;
 for var i:=485617  to 529678 do 
   begin
     var p:= i.Divisors.where(L -> L.IsPrime=true); 
       if (p.Count=3) and (p.Product=i)then 
       begin
         var l:=p.ToArray;      
         if (l[0] mod 10=l[1] mod 10)and (l[0] mod 10=l[2] mod 10)then
            begin
              ch+=1; 
              if (l[2]-l[0]<m) then begin m:=l[2]-l[0]; v:=i; end;
                 end; end;end;
            print(ch, v);
