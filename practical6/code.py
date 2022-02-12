"""
Id-20CE126
Name- Hardi shah

Aim-
     You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 
Sample Input 
4 
bcdef 
abcdefg 
bcde 
bcdef 
Sample Output 
3 
2 1 1 
Explanation: There are 3 distinct words.
 Here, "bcdef" appears twice in the input at the first and last positions. 
The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

GitHub - 

https://github.com/Hardi9/pythonassigment
"""
import collections;
N = int(input())
d = collections.OrderedDict()
for i in range(N):
    word = input()
    if word in d:
        d[word] +=1
    else:
        d[word] = 1
print(len(d));
for k,v in d.items():
    print(v,end = " ");
