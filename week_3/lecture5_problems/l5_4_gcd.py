def gcd(a,b):
	v=min(a,b)
	while a%v !=0 or b%v !=0:
		v=v-1
	return v




print gcd(2,12)
