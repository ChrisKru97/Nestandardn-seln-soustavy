import sys
import math

def convert(n):
	n = float(n)
	t = (math.pow(4,math.floor(math.log(math.fabs(n)+1,4)+2))-1)
	t = (t*2)/3
	x = bin(int(t+n))
	t = bin(int(t))
	l = len(x) if len(x) > len(t) else len(t)
	res = ''
	for i in range(l):
		res = res + ('1' if x[i] != t[i] else '0')
	print(res[res.find('1'):])


if __name__ == "__main__":
	convert(sys.argv[1])
