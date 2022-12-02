with open("input.txt") as f:
    lines = f.read().splitlines()


def did_win_rps(opponent_move, my_move):
    # Opponent
    # A = Rock
    # B = Paper
    # C = Scissors
    # Me
    # X = Rock
    # Y = Paper
    # Z = Scissors
    # Return
    # 0 for loss
    # 3 for draw
    # 6 for win

    if opponent_move == "A":
        if my_move == "X":
            return 3
        if my_move == "Y":
            return 6
        if my_move == "Z":
            return 0
    elif opponent_move == "B":
        if my_move == "X":
            return 0
        if my_move == "Y":
            return 3
        if my_move == "Z":
            return 6
    elif opponent_move == "C":
        if my_move == "X":
            return 6
        if my_move == "Y":
            return 0
        if my_move == "Z":
            return 3


def win_score_calc(line):
    opponent = line[0]
    me = line[2]
    return did_win_rps(opponent, me)


def move_calc(line):
    my_move = line[2]
    return calc_move_value(my_move) + 1


def calc_move_value(move):
    if move == "X":
        return 0
    if move == "Y":
        return 1
    if move == "Z":
        return 2
    if move == "A":
        return 0
    if move == "B":
        return 1
    if move == "C":
        return 2


result_sum = sum(map(win_score_calc, lines))
my_move_sum = sum(map(move_calc, lines))
print(f"Q1 Solution: {result_sum+my_move_sum}")
# 11475

# Part 2


def calc_best_move(line):
    opponent = line[0]
    me = line[2]
    opponent_score = calc_move_value(opponent)

    # Y means we need a draw
    # X means we need to lose
    # Z means we need to win

    # Y means we play the same as opponent
    # and get a draw (3 pts)
    if me == "Y":
        return opponent_score + 3 + 1
    # X means we need to lose
    # so we get 0 for losing
    # and we play the losing move
    # Combinations (Opp + Me)
    # Rock + Sci (return 3)
    # Paper + Rock (return 1)
    # Sci + Paper (return 2)
    if me == "X":
        return (opponent_score - 1) % 3 + 1
    # Z means we need to win
    # so we get 6 for winning
    # and we play the winning move
    # Combinations (Opp + Me)
    # Rock + Paper (return 2)
    # Paper + Sci (return 3)
    # Sci + Rock (return 1)
    if me == "Z":
        return (opponent_score + 1) % 3 + 6 + 1


calc_best_move_sum = sum(map(calc_best_move, lines))
print(f"Q2 Solution: {calc_best_move_sum}")
# 16862
