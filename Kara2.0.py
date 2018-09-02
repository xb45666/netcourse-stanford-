def Kara(x,y):
	
	x=str(x)
	y=str(y)

	if len(x)!=1 and len(y)!=1:
		"""to get a,b,c,d
		"""
		a=x[0:int(len(x)/2)]
		b=x[int(len(x)/2):int(len(x))]
		c=y[0:int(len(x)/2)]
		d=y[int(len(y)/2):int(len(y))]
		"""position
		"""

		ac_pos=10**(len(a)+len(c))
		ad_pos=10**len(a)
		bc_pos=10**len(c)

		"""to get ac bd ab cd"""

		ac=Kara(a,c)
		bd=Kara(b,d)
		ad=Kara(a,d)
		bc=Kara(b,c)

		return ac*ac_pos+bd+ad*ad_pos+bc*bc_pos
	else:

		x=int(x)
		y=int(y)
		return x*y

x=3141592653589793238462643383279502884197169399375105820974944592
y=2718281828459045235360287471352662497757247093699959574966967627

print(Kara(x,y))
