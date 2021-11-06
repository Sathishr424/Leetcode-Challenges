
alp = 'abcdefghijklmnopqrstuvwxyz'
alp = [i for i in alp]

def checkSpecialChar(txt):
    if txt[-1].lower() not in alp:
        return True
    return False

def pig_latin(txt):
    txt = txt.split(' ')
    ret = ""
    vowel = ['a','e','i','o','u']
    for i in range(len(txt)):
        if txt[i][0] in vowel or txt[i][0].lower() in vowel:
            if checkSpecialChar(txt[i]):
                ret += str(txt[i][:-1]) + 'way' + str(txt[i][-1])
            else: ret += str(txt[i]) + 'way'
    
            if i != len(txt)-1:
                ret += " "
        else:
            if txt[i][0].isupper():
                if checkSpecialChar(txt[i]):
                    ret += str(txt[i][1:-1]).capitalize() + str(txt[i][0]).lower() + 'ay' + txt[i][-1]
                else: ret += str(txt[i][1:]).capitalize() + str(txt[i][0]).lower() + 'ay'
            else:
                if checkSpecialChar(txt[i]):
                    ret += str(txt[i][1:-1]) + str(txt[i][0]).lower() + 'ay' + txt[i][-1]
                else: ret += str(txt[i][1:]) + str(txt[i][0]) + 'ay'
                
            if i != len(txt)-1:
                ret += " "
    return ret

class test:
    def assert_equals(self, ques, ans, tmp=""):
        if (ques == ans): print("PASS: " +  str(ques))
        else: print(ques,"!=",ans)

Test = test()
Test.assert_equals(pig_latin("Cats are great pets."), "Atscay areway reatgay etspay.")
Test.assert_equals(pig_latin("Tom got a small piece of pie."), "Omtay otgay away mallsay iecepay ofway iepay.")
Test.assert_equals(pig_latin("He told us a very exciting tale."), "Ehay oldtay usway away eryvay excitingway aletay.")
Test.assert_equals(pig_latin("A diamond is not enough."), "Away iamondday isway otnay enoughway.")
Test.assert_equals(pig_latin("Hurry!"), "Urryhay!")

#print(pig_latin("Cats are great pets."))
    
    
