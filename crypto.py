# Python program to check if two strings are isomorphic
MAX_CHARS = 256
 
# This function returns true if str1 and str2 are isomorphic
def areIsomorphic(string1, string2, mapping):
    m = len(string1)
    n = len(string2)
 
    # Length of both strings must be same for one to one
    # corresponance
    if m != n:
        return False
 
    # To mark visited characters in str2
    marked = [False] * MAX_CHARS
 
    # To store mapping of every character from str1 to
    # that of str2. Initialize all entries of map as -1
    map = [-1] * MAX_CHARS
 
    # Process all characters one by one
    for i in xrange(n):
 
        # if current character of str1 is seen first
        # time in it.
        if map[ord(string1[i])] == -1:
 
            # if current character of st2 is already
            # seen, one to one mapping not possible
            if marked[ord(string2[i])] == True:
                return False
 
            # Mark current character of str2 as visited
            marked[ord(string2[i])] = True
 
            # Store mapping of current characters
            map[ord(string1[i])] = string2[i]
 
        # If this is not first appearance of current
        # character in str1, then check if previous
        # appearance mapped to same character of str2
        elif map[ord(string1[i])] != string2[i]:
            return False
        #string2 is dictionary
        #string1 is encrypted
        if mapping != None:
            if mapping[ord(string1[i])-97] != string2[i] and mapping[ord(string1[i])-97] != -1:
                return False
    return True

def findPossible(content, possible, cipherString, mapping = None): 
    for f in content:
        if areIsomorphic(cipherString, f, mapping):
            possible.append(f)    

import sys

with open("dictionary.lst") as f:
    content = [line.rstrip("\n").lower() for line in f]

cipher = []
for line in sys.stdin:
    cipher.append(line)

cipher = cipher[0].split()    

mapping = [-1] * 26
solved = []
for word in cipher: 
    possible = []  
    findPossible(content, possible, word)

    if len(possible) == 1:
        #make mapping and replace word
        solved.append(possible[0])
        for char1, char2 in zip(possible[0], word):
            mapping[ord(char2)-97] = char1
    else:
        solved.append('1234')
               
alpha = []
for i in range(97,123):
    alpha.append(chr(i))
#print mapping
newSolved = []
for i in range(len(solved)):
    possible = []
    if solved[i] == '1234':
        findPossible(content, possible, cipher[i], mapping)
        if len(possible) == 1:
             newSolved.append(possible[0])
             for char1, char2 in zip(possible[0], cipher[i]):
                mapping[ord(char2)-97] = char1   
        else: 
            #print cipher[i]
            #print possible
            newSolved.append('shit')
    else:
        newSolved.append(solved[i])
#print mapping
final = []
for i in range(len(newSolved)):        
       if newSolved[i] == 'shit':
            newWord = ''
            for letter in cipher[i]:
                if mapping[ord(letter)-97] != -1:
                    newWord += mapping[ord(letter)-97]
                else:
                    print cipher[i]
            final.append(newWord)
       else:
            final.append(newSolved[i])        
print ' '.join(final)
