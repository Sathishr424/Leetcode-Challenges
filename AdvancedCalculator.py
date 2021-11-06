def calc(n1,n2,c):
	if c=='+': return float(n1)+float(n2)
	elif c=='-': return float(n1)-float(n2)
	elif c=='*': return float(n1)*float(n2)
	elif c=='/': return float(n1)/float(n2)

def getAns(val):
	print("GET_ANS:",val)
	sym = 'n'
	ind = 0
	num1 = val
	for i in range(len(val)):
		if val[i] == '(':
			cnt = 1
			for j in range(i+1,len(val)):
				if val[j] == '(': cnt+=1
				elif val[j] == ')':
					cnt-=1
					if cnt==0: return getAns(str(val[:i])+str(getAns(val[i+1:j]))+str(val[j+1:]))
		elif not val[i].isdigit() and val[i] != '.':
			if sym == 'n':
				num1 = float(val[ind:i])
				ind = i+1
				sym = val[i]
			else:
				num1 = calc(num1,float(val[ind:i]),sym)
				sym = val[i]
				ind = i+1
	if sym != 'n': num1 = calc(num1,float(val[ind:len(val)]),sym)
	return num1

while True:
	ques = input("QUES:")
	if ques == 'q': break
	print(eval(ques),':',getAns(ques))
#ques = "(125+123)*((4+4)+(199/23)+(12*21))"
#print(eval(ques),':',getAns(ques))
