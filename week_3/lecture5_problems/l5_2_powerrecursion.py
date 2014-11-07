def recurpower(base,exp):
	if exp <=0:
		return 1
	else:
		return base*recurpower(base,exp-1)



print recurpower(2,5)
