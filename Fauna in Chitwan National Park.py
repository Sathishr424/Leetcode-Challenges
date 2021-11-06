from test import Test

animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]

def fauna_number(txt):
    txt = txt.replace(',',' ')
    txt = txt.replace('.',' ')
    ret = []
    last = 0
    for i in range(len(txt)):
        if (txt[i].isdigit() and i > last):
            numEnd = txt[i:].find(' ')
            name = txt[i+numEnd+1:txt[i+numEnd+1:].find(' ')+i+numEnd+1]
            if name in animals:
                ret.append((name,txt[i:i+numEnd]))
            last=i+numEnd

    return ret

# print(fauna_number("There are 24 one-hornedrhino,50 python and 20000 bees."))
Test.assert_equals(fauna_number("There are 24 one-hornedrhino,50 python and 20000 bees."),[('one-hornedrhino', '24'), ('python', '50')])
Test.assert_equals(fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples."),[('bengaltiger', '244'), ('monitorlizard', '200')])
Test.assert_equals(fauna_number("There are 2444 saltrees,2000 cobra and 5000 mangotrees."),[])
Test.assert_equals(fauna_number("There are 180 muggercrocodile,20 krait and 500 taipan."),[('muggercrocodile', '180')])