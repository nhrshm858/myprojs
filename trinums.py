#to find triangular no.s which can be adde to give a square number 
import math
num=int(raw_input("Enter a number which is a perfect square: "))
n=math.sqrt(num)
t1=((n**2)+n)/2
sn=n-1
t2=((sn**2)+sn)/2

if isinstance(n,int):
	print "The triangular nos that form square no %d are %d and %d" %(num,t1,t2)
else:
	print "invalid input!!"