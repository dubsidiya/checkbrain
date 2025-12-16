// Автор: М. Крючков
##
var ar:=ReadAllText('24-239a.txt');
var (i, x, maxL):=(0, 0, 0);
repeat
  i+=1;
  x:=ar.MatchValue('(XY|YZZ|YZ){'+i.ToString+'}').Length;
  maxL:=max(x, maxL);
until x=0;
Print(maxL);
