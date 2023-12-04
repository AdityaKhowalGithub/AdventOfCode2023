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


def getFirstInt(word):
    out =0
    temp = ''
    for i in word:
        
        if i.isdigit():
            out += int(i)
            return out
        else:
            temp += i
            for d in digits:
                if d in temp:
                    out +=digits[d]
                    return out
    return out

def getLastInt(word):
    out = 0

    temp = ''
            
    for j in range(len(word)-1,-1,-1):
        i = word[j]
        if i.isdigit():
            out += int(i)
            return out
        else:
            temp = i + temp
            for d in digits:
                if d in temp:
                    out +=digits[d]
                    return out
    return out
    



def getSum(word):
    print(word, getFirstInt(word), getLastInt(word))
    return int( str(getFirstInt(word)) + str( getLastInt(word)))
file = open('input.txt', 'r')
s = 0
for line in file:
      s+=getSum(line.strip())

print(s)
file.close()
