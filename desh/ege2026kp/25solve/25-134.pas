// Автор: И.В.Свистун
##
For var n:= 525784203 to 728943762 do
Begin
var K:=0; var d:=0; 
var n1:=round(sqrt(n));  
if (n1<>sqrt(n)) then k:=100
 else
For var j:=2 to n1 do
  begin
If (n mod j=0) and (j*j<>n) then 
Begin k:=k+2; 
if (k=2) then d:=n div j; end;
If (n mod j=0) and (j*j=n) then 
Begin k:=k+1; 
if (k=1) then d:=n div j; end;
if (k>3)then break;
end;
If (k=3) then writeln(n,'   ', d) ;
end;
