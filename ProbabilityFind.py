#Find the condition where p > p^3 + 3*p^2(1-p^2)

p=0.0

while(p<=0.1):
	z = ( (p*p*p)+ (3 *p*p)*(1-p*p))
	#print("fdd" + str(f))
	if p <z:
		break
	else:
		p = p + 0.01
		#print("looping" + str(p))

print("Result" + str(p))