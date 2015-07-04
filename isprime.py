import math
import prime

print "Enter a number: "
n=int(raw_input())



if(n>1):
	prime_lst=prime.findprimes(n)
	primefacts=",".join(str(x) for x in prime_lst)
	print "prime factors are: " + primefacts

	bool_val=prime.isprime(n)
	if bool_val=='true':
		print "Entered no. %d is prime" %(n)
	else:
		print "Entered no. %d is not prime" %(n)
else:
	print "neither prime nor composite"








