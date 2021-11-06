"""We have a string s of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to s are applied.

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= s.length = shifts.length <= 20000
0 <= shifts[i] <= 109"""

class Solution:
    def shiftingLetters(self, s, shifts):
        ret = list(s)
        cnt = 0
        for i in shifts:
            cnt += i
        for i in range(len(ret)):
            ret[i] = chr(int(int((ord(ret[i]) - 97)+cnt)%26)+97)
            cnt -= shifts[i]
        return ''.join(ret)


print(Solution().shiftingLetters("asdg",[25,32,25,999]))
        
