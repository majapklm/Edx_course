def recurpower(base,exp):
	if exp<=0:
		return 1
	elif exp%2==0:
		return recurpower(base*base,exp/2)
	else:
		return base*recurpower(base,exp-1)






print recurpower(0.91,8)
