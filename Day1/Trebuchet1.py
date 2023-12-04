digits = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9}
def getInts(word):
    ints = []
    temp = ''
    for i in word:
        if i.isdigit():
            ints.append(str(i))
            temp = ''
        else:
            temp += i
            for d in digits:
                if d in temp:
                    ints.append(str(digits[d]))
                    temp = ''
            #if temp in digits:
            #    ints.append(str(digits[temp]))
            #    temp = ''
    return ints
def lineSum(lister):
    l = getInts(lister)
    print(lister, l[0],l[-1])
    return int(str(l[0]) + str(l[-1]))
file = open('i.txt', 'r')
s = 0
for line in file:
      s+=lineSum(line.strip())
      print(s)# strip() is used to remove the newline character at the end of the line
print(s)
file.close()

print(getInts("onetwothreefourfivesixseveneighteeeighteninetwoneeightwo"))

