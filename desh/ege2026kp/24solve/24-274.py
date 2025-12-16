# Автор: Е. Джобс

s = open('24-274.txt').readline()

lets = set(s)
#  PCSGO   -> PC  SGO   -> P CSGO
# PCSGO -> PC CSGO
s = s.replace('PCSGO', 'PC CSGO')
s = s.replace('PC', '**').replace('CSGO', '****')
for c in lets:
    s = s.replace(c, ' ')

print(max(map(len, s.split())))
