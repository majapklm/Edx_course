def lenrecur(astr):
	if astr=='':
		return 0
	else:
		return 1+lenrecur(astr[1:])



print lenrecur("sujith")

