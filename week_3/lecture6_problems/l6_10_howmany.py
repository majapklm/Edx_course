def howmany(adict):
	r=0
	for v in adict.values():
		r=r+len(v)
	return r



print howmany({'O': [17], 't': [], 'g': []})
