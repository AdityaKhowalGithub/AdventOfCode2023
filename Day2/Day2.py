file = open("Day2/input.txt", "r")
rm, gm, bm = 12, 13,14
out = []
for line in file:
    l = line.strip()
   #print(l)
    gb = l.split(':')
    print(gb[-2][-1])#gamenumber
    sets = gb[-1].split(';')
    canBeAdded = True

    for s in sets:
        w = s.split(',')
        for n in w:
            pp = n.split(' ')
            print(pp[1], pp[2])
            if pp[-1] == 'blue':
                if int(pp[1]) > bm:
                    canBeAdded = False
                    continue
                else:
                    bm -= int(pp[1])
            elif pp[-1] == 'red':
                if  int(pp[1]) > rm:
                    canBeAdded = False
                    continue 
                else:
                    rm -= int(pp[1])
            elif pp[-1] == 'green':
                if int(pp[1]) > gm:
                    canBeAdded = False
                    continue

                else:
                    gm -= int(pp[1])

        rm,gm,bm = 12, 13,14
        if canBeAdded == False:
            continue 
    #    out.append(int(gb[-2][-1]))
    #    canBeAdded = True
       #rm,gm,bm = 12, 13,14
                
    if canBeAdded:
        out.append(int(gb[-2][-1]))
    canBeAdded = True
            #print(w)
print(out)

file.close()

print(sum(out))
