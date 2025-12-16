
def f( start, end, needPalindrom=False, prog = '' ):
   if start > end: return 0
   if start == end:
      return int( prog == prog[::-1] ) if needPalindrom else 1
   return f( start+3, end, needPalindrom, prog+'A') + \
          f( start*4, end, needPalindrom, prog+'B') + \
          f( start*5, end, needPalindrom, prog+'C')

print( f(1, 16)*f(16, 152, True)*f(152, 725) )