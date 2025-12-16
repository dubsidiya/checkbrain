// Автор: И.В.Свистун
## 
uses School;
var s:=(525784203..728943762)
  .Where(K -> round(sqrt(k))=sqrt(k))
  .Select(n -> n.Divisors[1:^1])
  .Where(L -> L.Count = 3)
  .PrintLines(L -> L.First * L.Last + ' ' + L.Last)