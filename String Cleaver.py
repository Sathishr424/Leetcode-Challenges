from test import Test

def checkIfThere(lst,start,end,string):
    last = ""; index = end
    for i in range(end,len(string)):
        if string[start:i+1] in lst:
            if last != '':
                word = False
                for j in range(i,len(string)):
                    if string[i:j+1] in lst:
                        word = True; break
                if not word:
                    last = string[start:i+1]
                    index = i+1
                else: break
            else:
                last = string[start:i+1]
                index = i+1
    return index,last

def cleave(string, lst):
    ret = ""; last = 0
    for i in range(len(string)):
        index,val = checkIfThere(lst,last,i,string)
        if len(val) > 0 and i >= last:
            ret += val + " "
            last = index
    if len(ret.replace(' ','')) != len(string): return "Cleaving stalled: Word not found"
    return ret[:-1]
    
        
        
    
word_list = ['a', 'after', 'all', 'an', 'and', 'are', 'as', 'by', 'continued', 'deadlines', 'doubly', 'fish', 'for', 'go',
             'happen', 'happened', 'i', 'illusion', 'is', 'long', 'love', 'lunchtime', 'make', 'moment', 'noise', 'nothing',
             'of', 'or', 'people', 'problem', 'second', 'so', 'summarize', 'summary', 'thanks', 'the', 'then', 'they', 'time',
             'to', 'whooshing']

s1='solongandthanksforallthefish'
s2= 'solongandthanksforalllthefish'
s3= 'tosummarizethesummaryofthesummarypeopleareaproblem'
s4= 'timeisanillusionlunchtimedoublyso'
s5= 'ilovedeadlinesilovethewhooshingnoisetheymakeastheygoby'
s6= 'ilovedeadlinesilovethewheezingnoisetheymakeastheygoby'
s7= 'foramomentnothinghappenedthenafterasecondorsonothingcontinuedtohappen'

Test.assert_equals(cleave(s1, word_list), 'so long and thanks for all the fish')
Test.assert_equals(cleave(s2, word_list), "Cleaving stalled: Word not found")
Test.assert_equals(cleave(s3, word_list), 'to summarize the summary of the summary people are a problem')
Test.assert_equals(cleave(s4, word_list), 'time is an illusion lunchtime doubly so')
Test.assert_equals(cleave(s5, word_list), 'i love deadlines i love the whooshing noise they make as they go by')
Test.assert_equals(cleave(s6, word_list), "Cleaving stalled: Word not found")
Test.assert_equals(cleave(s7, word_list), 'for a moment nothing happened then after a second or so nothing continued to happen')

#Quotes credit: Douglas Adams