import math
file = open("Day2/input.txt", "r")
rm, gm, bm = 12, 13,1
out = set() 
colors = { 
        "red" : 0,
        "green" : 1,
        "blue" : 2
        }

def dcvalid(sol):

    return (sol[0] <= 12 and sol[1] <= 13 and sol[2] <= 14)

def isValid(d):
    sol = [0,0,0]
    for count_color in d.split(', '):
        count, color = count_color.split(' ')
        count = int(count)
        sol[colors[color]] += count

    return sol 
gameDict = {}
for line in file:
    l = line.strip()
    game, draws = l.split(': ')
    _, game_id = game.split(' ')
    game_id = int(game_id)
    gameValid = True
    gameDict[game_id] = [0,0,0] 
    for d in draws.split('; '):
        gpx = isValid(d)
        for gp in range(len(gpx)):
            gameDict[game_id][gp] = max(gpx[gp], gameDict[game_id][gp])

        #print(game_id, isValid(d), dcvalid(isValid(d)))
        #if dcvalid(isValid(d)) != True:
        #    gameValid = False
    #if gameValid:
    #    out.add(game_id)
s = 0
for game, minValues in gameDict.items():
    s += math.prod(minValues)
print(s)




#print(sum(out))
