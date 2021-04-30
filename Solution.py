#sorting the dictioinery in descending order based on the values
def  sortdictbasedonvalues(x):
    sorted_dict = {}
    sorted_keys = sorted(x, key=x.get,reverse=True)  
    for w in sorted_keys:
        sorted_dict[w] = x[w]   
    return sorted_dict

# Function to find longest common subsequence
def lcs(S1, S2, m, n):
    # making the matrix for dynamic programming
    L = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0             #making first column and row as zeros
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1   #if char match
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])     #if not

    index = L[m][n]
    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs_algo[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
  
    # Printing the sub sequences
    return lcs_algo


# creating tree
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


#main coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d





#   main 

#file reading
f1 = open("first.txt").readlines()
f2 = open("second.txt").readlines()
p=dict()
q=dict()

#getting common words from two log files
if len(f1) != 0 | len(f2) != 0:
    uniq1 = set(words for line in f1 for words in line.strip("\n\t").split(" "))
    uniq2 = set(wordss for lines in f2 for wordss in lines.strip("\n\t").split(" "))
    for words in uniq1:
        for wordds in uniq2:
            if words == wordds and words!="":
                p[words]=0
#copying p dict to q
q=p.copy()
#counting the common strings
for string in p:
    for line in f1:
        line=line.strip().split(" ")
        for word in line:
            if string==word:
                p[string]=p[string]+1
    for line in f2:
        line=line.strip().split(" ")
        for word in line:
            if string==word:
                q[string]=q[string]+1

# sorting both the dicts from two files
p=sortdictbasedonvalues(p)
q=sortdictbasedonvalues(q)
# Subtracting the same key values to find most common words
for i in p:
    r=p[i]-q[i]
    if r >0:
        p[i]=g[i]
    else:
        p[i]=p[i]
#again sorting the final dict in descending order based in the values 
p=sortdictbasedonvalues(p)
#deleting the dict q
del q
#The frequent words from two files
print("\nThe most frequent words from two files are: \n")
j=0
q=list()
for i in p:
    j+=1
    q.append(i)         #storing the top three strings in a list
    print(str(j)+". "+" \" "+str(i)+" \" "+" "+" common in both files for "+str(p[i])+" times.")
    if j==3:
        print()
        break
del p
# q=["ACXCXDAC","CADXDACADX","CXDACAXDAC"]
m = len(q[0])
n = len(q[1])
lcs_1=lcs(q[0], q[1], m, n)
S1=""
for letter in lcs_1:
    if letter!="" and letter!=" ":
        S1+=letter
S2=q[2]
m=len(S1)
n=len(q[2])
lcs_2=lcs(S1, q[2], m, n)
print("--> The longest Common Subsequence for the 3 Strings is: ",end="")
string=""
for letter in lcs_2:
    if letter!="" and letter!=" ":
        string+=letter
print(string)
print()
print("--> The encoded string for the Longest Common Subsequence is: ",end="")

# Calculating frequency
freq =dict()
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])


for char in string:
    print(huffmanCode[char],end="")









