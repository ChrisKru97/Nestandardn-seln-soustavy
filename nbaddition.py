import sys

def add(n1, n2):
	[n1,n2] = [n1,n2] if len(n1) > len(n2) else [n2,n1]
	diff = len(n1)-len(n2)
	ec = 0
	c = 0
	res = ''
	l = len(n2)
	i = l-1
	while c or ec or (i+diff)>=0:
		sum = c + ec
		if (i+diff) >= 0:
			sum = sum + int(n1[i+diff])
		if i >= 0:
			sum = sum + int(n2[i])
		ec = c
		c = 0
		if sum == 2:
			if (i)>=0:
				sum = 0
				c = 1
			else:
				sum=1
		if sum == 3:
			if(i)>=0:
				c = 1
				sum = 1
		if sum == 4:
			sum = 0
	#		if (i)>=0:
			c = 1
			ec = 1
		res = str(sum) + res
		i = i - 1
	print(res)

if __name__ == "__main__":
        add(sys.argv[1],sys.argv[2])
