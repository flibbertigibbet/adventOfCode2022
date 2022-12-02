#!/usr/bin/env python3

rps_mine = {
    'X': 1, # rock
    'Y': 2, # paper
    'Z': 3  # scissors
}

me = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

elves = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

can_beat = {
    'X': 'C',
    'Z': 'B',
    'Y': 'A'
}

with open("data_day2.txt") as data_file:
    data = [x.strip().split() for x in data_file]
 
total_score = 0
losses = 0
wins = 0
draws = 0

for x in data:
    (elf, mine) = x
    total_score += rps_mine[mine]
    print(f"\nplay {me[mine]} against {elves[elf]}")
    print(f"{me[mine]} can beat {elves[can_beat[mine]]}")
    if elf == can_beat[mine]:
        total_score += 6
        wins += 1
        print("won")
    elif me[mine] == elves[elf]:
        total_score += 3
        draws += 1
        print("draw")
    else:
        losses += 1
        print("lost")

print(f"\n\nlosses: {losses} wins: {wins} draws: {draws}")
print(f"\ntotal score: {total_score}")
