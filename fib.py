print "Enter 2 starting numbers of fibonacci series separated by space: "
nums=raw_input()
num_lst=nums.split()
fnum=int(num_lst[0])
snum=int(num_lst[1])

print "Enter limit: "
lim=int(raw_input())


def findfib(fnum,snum):
	sum=0
	emp=[]
	while 'true':
		sum=fnum+snum
		fnum=snum
		snum=sum
		if sum<=lim:
			emp.append(sum)
		else:
			break
	return emp

fib_lst=[fnum,snum]+findfib(fnum,snum)
print ",".join(str(x) for x in fib_lst)






