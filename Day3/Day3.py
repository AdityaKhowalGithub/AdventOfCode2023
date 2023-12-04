symbols = ('!','@','#','$','%','^','&','*','(',')')
def part1(fileName):
    file = open(fileName, 'r')
    pp = []
    numbs = []
    for line in file:
        l = line.strip()
        #print(list(l))
        pp.append(list(l))
    total = 0
    for i in range(len(pp)):
        start = -1
        end = -1
        for j in range(len(pp[i])):
            if pp[i][j].isdigit():
                if start == -1:
                    start = j 
                end = j
            
            else:

                print(pp[i][start:end+1])
                if is_symbol(pp[i][j]) or j <= len(pp[i])-1:
                    if start  != -1 and end !=-1:
                        
                        numbs.append(pp[i][start:end+1])
                        current = pp[i][start:end+1]
                        if nextToSymbol(pp,i,start, end):
                            total += int(''.join(current))
                start = -1
                end = -1
    print(numbs)
    return total

        
   #print(i)
def is_symbol(char):
    if char == '.':
        return False
    return not char.isdigit()

def nextToSymbol(schematic, i, start, end):
    rows = len(schematic)
    cols = len(schematic[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for j in range(start, end+1):
        for dx, dy in directions:
            x = i + dx
            y = j + dy 
            if 0 <= x < rows and 0 <= y < cols and is_symbol(schematic[x][y]):
                return True
    return False

#def nextToSymbol(schematic, i, start, end):
#    rows = len(schematic)
#    cols = len(schematic[0])
#    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
#    for j in range(start, end+1):
#        for dx, dy in directions:
#            x =i+dx
#        #for j in range( start, end+1):
#            y= j +dy 
#           #print(schematic[i:dx][y:dy])
#            if 0<=x<=rows and 0<=y<=cols and is_symbol(schematic[x][y]):
#                return True
#    return False


def symbolSearch():
    pass







print(part1('./input.txt'))
