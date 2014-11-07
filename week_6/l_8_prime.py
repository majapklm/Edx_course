def prime():
	p=[]
	i=1
	while True:
		i=i+1
		for v in p:
			if i%v==0:
				break
		else:
			p.append(i)
			yield i



i.next()
