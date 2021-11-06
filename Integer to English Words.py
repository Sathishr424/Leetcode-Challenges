import random

words = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', \
         'Eleven','Tweleve','thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen',\
         'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'] #4

class Solution():
    def getWord(self, num):
        if len(num) < 4:
            if len(num) == 2:
                if num[0] == '1':
                    return words[int(num)-1]
                elif num[0] == '0':
                    return self.getWord(str(num[1:]))
                else:
                    return words[int(num[0])+17] + " " + self.getWord(str(num[1:]))
            elif len(num) == 1:
                if num == '0': return ' '
                return words[int(num[0])-1]
            else:
                if num[0] == '0': return self.getWord(str(num[1:]))
                else: return words[int(num[0])-1] + " Hundred " + self.getWord(str(num[1:]))
        elif len(num) < 7:
            tmp = self.getWord(str(num[:-3]))
            if len(tmp.strip()) == 0: return self.getWord(str(num[-3:]))
            else: return tmp + " Thousand " + self.getWord(str(num[-3:]))
        elif len(num) < 10:
            tmp = self.getWord(str(num[:-6]))
            if len(tmp.strip()) == 0: return self.getWord(str(num[-6:]))
            else: return self.getWord(str(num[:-6])) + " Million " + self.getWord(str(num[-6:]))
        else:
            return self.getWord(str(num[:-9])) + " Billion " + self.getWord(str(num[-9:]))
        
    def numberToWords(self, num):
        if num == 0: return "Zero"
        return ' '.join(self.getWord(str(num)).split()) + " Only"
            
print(Solution().numberToWords(2131))          
for i in range(10):        
    print(Solution().numberToWords(random.randint(0,125246535)))
