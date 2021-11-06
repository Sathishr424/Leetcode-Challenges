from test import Test

letters = ['I','V','X','L','C', 'D','M']
value =   [ 1,  5, 10,  50, 100,500,1000]

def currentLetter(val):
    sVal = str(val)[0]
    for i in range(len(value)):
        if val == value[i]:
            return letters[i]
        elif value[i] > val and value[i-1] < val:
            if int(sVal[0]) <= 3:
                return letters[i-1] * int(sVal[0])
            elif int(sVal[0]) == 4:
                return letters[i-1] + letters[i]
            elif int(sVal[0]) > 5 and int(sVal[0]) < 9:
                return letters[i-1] + (letters[i-2] * (int(sVal[0]) - 5))
            elif int(sVal[0]) == 9:
                return letters[i-2] + letters[i]
    return letters[-1] * int(sVal[0])

def convert_to_roman(num):
    if num > 3999: return "Cannot convert larger than 3999.."
    sNum = str(num)
    ret = ''
    for i in range(0,len(sNum)):
        cDigit = int(str(sNum[i]) + ("0"*(len(sNum)-(i+1))))
        if sNum[i] != '0':
            ret += str(currentLetter(cDigit))
    return ret


Test.assert_equals(convert_to_roman(2), "II")
Test.assert_equals(convert_to_roman(12),"XII")
Test.assert_equals(convert_to_roman(16), "XVI")
Test.assert_equals(convert_to_roman(44), "XLIV")
Test.assert_equals(convert_to_roman(68), "LXVIII")
Test.assert_equals(convert_to_roman(400), "CD")
Test.assert_equals(convert_to_roman(798), "DCCXCVIII")
Test.assert_equals(convert_to_roman(1000), "M")
Test.assert_equals(convert_to_roman(3999),"MMMCMXCIX")
Test.assert_equals(convert_to_roman(649), "DCXLIX")