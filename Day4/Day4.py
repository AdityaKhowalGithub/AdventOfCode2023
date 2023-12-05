def get_inptut(fileName):
    file = open('./'+fileName, 'r')
    
    cards = {}

    for line in file:
        l = line.strip()
        #print('l',l)
        card, numbers = l.split(':')
        #print(card)
        winning, actual = numbers.split('|')
        #print(card.split(' '))
        cardNumber = card.split(' ')[-1]
    #    cards[cardNumber] = [winning.split(' '), actual.split(' ')]
        cards[int(cardNumber)] = [[int(num) for num in winning.split(' ') if num], [int(num) for num in actual.split(' ') if num]]
    return cards

def numberOfWinningCards(winners, actuals):
    wins = 0
    #return len(set(winners) & set(actuals))
    for winner in winners:
        wins += actuals.count(winner)
    return wins

def get_points(wins):
    points = 2**(wins-1)
    if points >=1:
        return points
    else:
        return 0
    

def part1():
    map = get_inptut("input.txt")
    #print(map[1][0])
    sum = 0
   
    for card in map:
       #print(card)
       print(numberOfWinningCards(map[card][0],map[card][-1]),get_points(numberOfWinningCards(map[card][0],map[card][-1]))
       )
       sum += get_points(numberOfWinningCards(map[card][0],map[card][-1]))

    print(sum)
part1()

def getDuplicates(cardNumber, numberOfWinningCards):
    return [x for x in range(cardNumber+1, cardNumber + numberOfWinningCards+1)]

def part2():
    
    f = open("input.txt").readlines()#better than my old method lol

    s = 0
    cards = [1 for _ in f]

    for index, line in enumerate(f):
        line = line.split(":")[1]
        a, b = line.split("|")
        a, b = a.split(), b.split()

        n = len(set(a) & set(b))

    #if n > 0:
    #    s += 2 ** (n - 1)

        for i in range(n):
            cards[index + i + 1] += cards[index]

    print(sum(cards))

   



part2()
