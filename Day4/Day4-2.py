import os
MAX_SCORE = 1000000

def parse_card(card_str):
    winning, mine = card_str.split('|')
    winning = set([int(n) for n in winning.split() if n])
    mine = set([int(n) for n in mine.split() if n])
    return winning, mine


def parse_input(input_str):
    cards = {}
    for line in input_str.splitlines():
        if line: 
            id, card_str = line.strip().split(':')
            winning, mine = parse_card(card_str)
            cards[int(id)] = (winning, mine)
    return cards


def num_winning(winners, mine):
    return len(winners & mine)


def get_points(wins):
    points = min(MAX_SCORE, 2**(wins-1))  
    return max(0, points)


def score_cards(cards):
    return sum(get_points(num_winning(winners, mine)) 
               for id, (winners, mine) in cards.items())


input_txt = os.path.join(os.getcwd(), 'input.txt')  

with open(input_txt) as f:
    puzzle_input = f.read()

cards = parse_input(puzzle_input)  
print(score_cards(cards))
