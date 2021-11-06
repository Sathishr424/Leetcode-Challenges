"""
String Compression from Characters Array
The function is given an array of characters. Compress the array into a string using the following rules. For each group of consecutively repeating characters:

If the number of repeating characters is one, append the string with only this character.
If the number n of repeating characters x is greater than one, append the string with "x" + str(n).
Examples
compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"

compress(["a"]) ➞ "a"

compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"

compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"
"""

def compress(chars):
	ret = ''
	cnt = 1
	val = chars[0]
	for i in range(1,len(chars)):
		if val == chars[i]:
			cnt += 1
		else:
			if cnt > 1: ret += val + str(cnt)
			else: ret += val
			cnt = 1
			val = chars[i]
	if cnt > 1: ret += val + str(cnt)
	else: ret += val
	return ret
	