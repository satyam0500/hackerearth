"""

You have been given a String S consisting of uppercase and lowercase English alphabets.
You need to change the case of each alphabet in this String.
All the uppercase letters should be converted to lowercase & all the lowercase letters should be converted to uppercase.
You need to then print the resultant String to output.

Input Format
The first and only line of input contains the String S

Output Format
Print the resultant String on a single line.

Constraints
 where S denotes the length of string S.

SAMPLE INPUT
abcdE

SAMPLE OUTPUT
ABCDe

"""

a = input()
a = a.swapcase()
print(a)
