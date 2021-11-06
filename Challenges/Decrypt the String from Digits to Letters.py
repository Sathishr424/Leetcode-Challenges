from test import Test

def decrypt(s):
    alp = list('abcdefghijklmnopqrstuvwxyz')
    s2 = ''
    ret = ''
    for i in range(len(s)):
        if s[i] == '#':
          s2 = s2[:-2] + alp[int(s2[-2:])-1]
        else:
            s2 += str(s[i])
    for i in range(len(s2)):
        if s2[i].isdigit(): ret += alp[int(s2[i])-1]
        else: ret += s2[i]
    return ret
            

from time import perf_counter
from random import randint
tic = perf_counter()

Test.assert_equals(decrypt("10#11#12"), "jkab")
Test.assert_equals(decrypt("1326#"), "acz")
Test.assert_equals(decrypt("25#"), "y")
Test.assert_equals(decrypt("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"), "abcdefghijklmnopqrstuvwxyz")

for _ in range(100):
    input_lst = []
    expected_lst = []
    for _ in range(randint(1, 100)):
        k = randint(1, 26)
        input_lst.append("{}{}".format(str(k), "#" if k > 9 else ""))
        expected_lst.append(chr(96 + k))
    Test.assert_equals(decrypt("".join(input_lst)), "".join(expected_lst))

print('t_sec = {:.6f}'.format(perf_counter() - tic))