# Коротков Михаил Сергеевич
# vk.com/mskorotkov

def quad(x, y):
	if x > 0 and  y > 0:
		return 1
	elif x < 0 and y > 0:
		return 2
	elif x < 0 and y < 0:
		return 3
	elif x > 0 and y < 0:
		return 4
	else:
		return 0

k = 0
for s in open("9-138.csv"):
	x1, x2, x3, y1, y2, y3 = map(int, s.split(";"))
	
	a = []
	for q in [quad(x1, y1), quad(x2, y2), quad(x3, y3)]:
		if q != 0:
			a.append(q)
			
	if len(a) == 3 and len(set(a)) == 2 or \
	   len(a) == 2 and len(set(a)) == 1:
		k += 1
		
print(k)
