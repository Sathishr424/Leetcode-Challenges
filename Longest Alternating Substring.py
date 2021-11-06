from test import Test

def longest_substring(digits):
	ret = ''
	tmp = str(digits[0])
	odd = True
	if int(digits[0])%2 == 0: odd = False
	for i in range(1,len(digits)):
		if odd and int(digits[i])%2==0:
			tmp+=str(digits[i])
			odd = False
		elif not odd and int(digits[i])%2!=0:
			tmp+=str(digits[i])
			odd = True
		else:
			if len(tmp) > len(ret):
				ret = tmp
			tmp=str(digits[i])
			if int(digits[i])%2 != 0: odd = True
			else: odd = False
	if len(tmp) > len(ret): ret = tmp
	return ret
	
Test.assert_equals(longest_substring("844929328912985315632725682153"), "56327256")
Test.assert_equals(longest_substring("769697538272129475593767931733"), "27212947")
Test.assert_equals(longest_substring("937948289456111258444958189244"), "894561")
Test.assert_equals(longest_substring("736237766362158694825822899262"), "636")
Test.assert_equals(longest_substring("369715978955362655737322836233"), "369")
Test.assert_equals(longest_substring("345724969853525333273796592356"), "496985")
Test.assert_equals(longest_substring("548915548581127334254139969136"), "8581")
Test.assert_equals(longest_substring("417922164857852157775176959188"), "78521")
Test.assert_equals(longest_substring("251346385699223913113161144327"), "638569")
Test.assert_equals(longest_substring("483563951878576456268539849244"), "18785")
Test.assert_equals(longest_substring("853667717122615664748443484823"), "474")
Test.assert_equals(longest_substring("398785511683322662883368457392"), "98785")
Test.assert_equals(longest_substring("368293545763611759335443678239"), "76361")
Test.assert_equals(longest_substring("775195358448494712934755311372"), "4947")
Test.assert_equals(longest_substring("646113733929969155976523363762"), "76523")
Test.assert_equals(longest_substring("575337321726324966478369152265"), "478369")
Test.assert_equals(longest_substring("754388489999793138912431545258"), "545258")
Test.assert_equals(longest_substring("198644286258141856918653955964"), "2581418569")
Test.assert_equals(longest_substring("643349187319779695864213682274"), "349")
Test.assert_equals(longest_substring("919331281193713636178478295857"), "36361")
