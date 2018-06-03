################################
#Problem Set 01 - Exercise 01
################################

# Paste your code into this box 
count = 0
for i in range(len(s)):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        count = count + 1

print "Number of vowels: ", count

################################
#Problem Set 01 - Exercise 02
################################

# Paste your code into this box 
count = 0
for i in range(len(s)-2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count = count + 1

print "Number of times bob occurs is: ", count

################################
#Problem Set 01 - Exercise 03
################################

# Paste your code into this box 
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest
