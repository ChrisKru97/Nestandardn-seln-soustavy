def getLargest(n):
	i=1
	inew=1
	inewlast=1
	index=0
	while(inew<=n):
		inew = i + inew
		i = inewlast
		index = index + 1
		inewlast = inew
	return [i,index]	

def encode(n):
	res = ''
	i = 0
	while(n > 0):
		[f,index] = getLargest(n)
		n = n - f
		off = i - index
		#if(off < 0):
		#	off = 0 - off
		for k in range(off-1):
			res = '0' + res
		res = '1' + res
		i = index
	for k in range(i-1):
		res = '0' + res
	return res
