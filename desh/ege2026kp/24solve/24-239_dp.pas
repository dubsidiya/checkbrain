##
var s := ReadAllText('24-239.txt');

s := '.' + s;
var N := s.Length;
var dp := |0|*(N+1);

foreach var i in (3..N) do begin
  if s[i-1:i+1] in ['XY', 'YZ'] then
    dp[i] := dp[i-2] + 2;
  if (i > 3) and (s[i-2:i+1] = 'YZZ') then
    dp[i] := max( dp[i], dp[i-3] + 3 );
end;    

Print( max(dp) )
