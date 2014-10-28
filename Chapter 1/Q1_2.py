#1.2
# using python slice
def reverse_str(string):
    return string[::-1]

# recursive implementation
def reverse_str_rec(s):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    elif len(s) == 2:
        return s[-1] + s[0]
    else:
        return s[-1] + reverse_str_rec(s[1:-1]) + s[0]


#--------------------test-------------------
inputstr = "abcdefghijk"
if reverse_str(inputstr)==reverse_str_rec(inputstr)=="kjihgfedcba":
    print "test passed"
else:
    print "failed"
#1.3
def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    dic = {}
    for char in string1:
        dic[char] = dic.get(char, 0) + 1
    for char in string2:
        if dic.get(char,0) <= 0:
            return False
        else:
            dic[char] -= 1
    return True



#------------------test-----------------
string1 = "abcdefghaa"
string2 = "aaabcdefgh"
string3 = "dkescvvade"
string4 = ""

if isPermutation(string1, string2):
    print "test 1 passed"
if not isPermutation(string1, string3):
    print "test 2 passed"
if not isPermutation(string1, string4):
    print "test 3 passed"
#1.4
# using a list to store each char and change space to '%20', then join list into a string
def replaceSpace(string):
	charList = []
	for char in string:
		if char == ' ':
			char = '%20'
		charList.append(char)
	return ''.join(charList)



#------------------test-----------------
inputStr = " Smith    q m "
expectOutput = "%20Smith%20%20%20%20q%20m%20"
if replaceSpace(inputStr) == expectOutput:
	print "test passed"
else:
	print "test failed"
#1.5
def strCompress(string):
    compressed = []
    lastchar = "" 
    charcount = 0
    for char in string:
        if char == lastchar:
            charcount += 1
        else:
            if lastchar != "":
                compressed.append(lastchar+str(charcount))
            lastchar = char
            charcount = 1
    compressed.append(lastchar+str(charcount)) #append the last character
    compressedStr = ''.join(compressed)  # join the list into a string
    if len(compressedStr)<len(string):
        return compressedStr
    else:
        return string
        


#-------------------------test-----------------------
inputStrs = ["abcdddefg", "aabbbcccaaffesttt", ""]
expectedOutputs = ["abcdddefg","a2b3c3a2f2e1s1t3", ""]

for i in range(0,len(inputStrs)):
    if strCompress(inputStrs[i])==expectedOutputs[i]:
        print "test "+ str(i+1) + " passed"
    else:
        print "test "+ str(i+1) + " failed"
#1.6
def rotate90Deg(matrix):
    n = len(matrix)
    for layer in range(0,(n+1)/2):
        first = layer
        last = n-layer-1
        for i in range(first, last):
            offset = i-first
            temp = matrix[first][i]                                         #save top
            matrix[first][i] = matrix[last-offset][first]                  #left to top
            matrix[last-offset][first] = matrix[last][last-offset]   #bottom to left
            matrix[last][last-offset] = matrix[i][last]               #right to bottom
            matrix[i][last] = temp                                          #top to righ
    return matrix
    


#----------------------test----------------------
# input 4*4 matrix
# 1  2 3 4
# 4  5 6 7
# 6  8 6 5
# 0 -1 4 2
# expected output
#  0 6 4 1
# -1 8 5 2
#  4 6 6 3
#  2 5 7 4
inputMatrix = [[1,2,3,4],[4,5,6,7],[6,8,6,5],[0,-1,4,2]]
expectedOutput = [[0,6,4,1],[-1,8,5,2],[4,6,6,3],[2,5,7,4]]
if rotate90Deg(inputMatrix) == expectedOutput:
    print "test passed"
else:
    print "test failed"
    print rotate90Deg(inputMatrix)
#1.7

def setZero(matrix):
    m = len(matrix)       
    n = len(matrix[0])
    rows = set()
    cols = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        for j in range(n):
            matrix[row][j]=0
    for col in cols:
        for i in range(m):
            matrix[i][col]=0



#-------------------test------------------
#inputMatrix
# 1,2,3,4
# 0,3,4,5
# 4,6,9,0
# 1,1,1,1
#expected output
# 0,2,3,0
# 0,0,0,0
# 0,0,0,0
# 0,1,1,0
inputMatrix = [[1,2,3,4],[0,3,4,5],[4,6,9,0],[1,1,1,1]]
setZero(inputMatrix)
print inputMatrix

#1.8
def isSubstring(s1, s2):
	return s2 in s1

def isRotation(s1,s2):
	s1s1 = s1 + s1
	return isSubstring(s1s1, s2)



#-----------------test-------------
s1 = "keitjkdss"
s2 = "itj"
print isRotation(s1,s2)  # True
