stack=[]
def insertintostack(item):
	stack.append(item)
	return stack

def deletefromstack():
	stack.pop()
	return stack


def viewstack():
	return ",".join(stack)
	


def main():
	while 'true':
		print "Implementing List as Stack \n Options: \n 1. Insert an item \n 2. delete an item \n 3. View stack \n 4. Exit program"
		print "what would you like to do?\n Please enter an Option: "
		input=int(raw_input())
		if input not in (range(1,5)):
			print "invalid Input!!!"
			break
		else:
			if input==1:
				print "Enter any item to add to stack: "
				item=raw_input()
				print "Item to be added: %s" %(item,)
				insertintostack(item)
				print "Item added to stack!!"
				
			elif input==2:
				if len(stack)!=0:
					deletefromstack()
					print "last inserted item deleted from stack!!"
				else:
					print "stack empty!!!"
			elif input==3:
				stack_view=viewstack()
				print stack_view
			else:
				print "Bye!!"
				break


main()
