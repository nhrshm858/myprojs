import string
alphas=string.letters
nums=string.digits

print "Enter identifier to test(atleast 2 characters long): "
inp=raw_input()

if len(inp)>1:
	if inp[0] not in alphas:
		print"invalid identifier:first char must be alphabetic"
	else:
		for otherchar in inp:
			if otherchar not in alphas+nums:
				print "other chars must be alphanumeric"
				break
		else:
			print "valid identifier"
else:
	print "invalid input length"
