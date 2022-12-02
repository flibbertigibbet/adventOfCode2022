#!/usr/bin/env python3

plays = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

can_beat = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

need_to_do = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

with open("data_day2.txt") as data_file:
    data = [x.strip().split() for x in data_file]
 
total_score = 0
losses = 0
wins = 0
draws = 0

for x in data:
    (elf, mine) = x
    my_play = None
    if mine == 'Z':
        wins += 1
        total_score += 6
        for play in plays:
            if can_beat[play] == elf:
                my_play = play
                print(f"\n{plays[play]} beats {plays[elf]}")
    elif mine == 'Y':
        draws += 1
        my_play = elf
        total_score += 3
    else:
        losses += 1
        my_play = can_beat[elf]
        print(f"\n{plays[my_play]} loses to {plays[elf]}")
    
    for score, play in enumerate(('A', 'B', 'C'), 1):
        if play == my_play:
            total_score += score
    
    print(f"\nplay {plays[my_play]} against {plays[elf]} when I should {need_to_do[mine]}")

print(f"\n\nlosses: {losses} wins: {wins} draws: {draws}")
print(f"\ntotal score: {total_score}")
