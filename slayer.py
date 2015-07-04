#To check if slayer+slayer+slayer==layers
print "Enter a 6-digit number: "
n=int(raw_input())
new=repr(3*n)
if new[0]==(n//10000)%10:
	if new[1]==(n//1000)%10:
		if new[2]==(n//100)%10:
			if new[3]==(n//10)%10:
				if new[4]==n%10:
					if new[5]==(n//100000)%10:
						print "true"
else:
	print "false"
