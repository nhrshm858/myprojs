import math

def findprimes(num):
	emp=[]
	i=2
	while (i<=num):
		while (num%i==0):
			emp.append(i)
			num /= i 
		i += 1
	return emp




def isprime(n):
	root=int(math.sqrt(n))
	plist=findprimes(root)
	primes=plist.append(n)
	for i in primes:
		if (n%i==0):
			return 'false'
		else:
			return 'true'
 




