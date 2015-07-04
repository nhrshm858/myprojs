import random
print "Enter the number of flips: "
num=int(raw_input())
print "coin will be tossed %d times" %(num,)

def coinflip():
	flip=random.choice([0,1])
	if flip==0:
		return 'true'
	else:
		return 'false'



def main(num):
	heads=0
	tails=0
	res_str=" "
	for i in range(num):
		if (coinflip()):
			heads+=1
			res_str+="H"
		else:
			tails+=1
			res_str+="T"
	print "No. of Heads: %d \n No. of Tails: %d \n Result Sequence: %s" %(heads,tails,res_str) 
	

main(num)
