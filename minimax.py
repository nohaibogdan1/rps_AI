import math
import numpy as np

ROUND_LIMIT = 8
scores = [0.0, -0.5, 0.5, 0.5, 0.0, -0.5, -0.5, 0.5, 0.0]
counts = [0] * 9
actionTable = {
    'RR': 0,
    'RP': 1,
    'RS': 2,
    'PR': 3,
    'PP': 4,
    'PS': 5,
    'SR': 6,
    'SP': 7,
    'SS': 8
}

# is final state?
def is_final(state):
    if state[0] == ROUND_LIMIT or state[1] == ROUND_LIMIT:
        return True
    return False

# get next states
def get_next(state, action):
    pass

def minimax(currDepth, actions, maxTurn, probs, targetDepth=2):
    # if we have reached the target depth
    # target depth = 2 (computer takes turn than player takes turn)
    if currDepth == targetDepth:
        # get the heuristic value from the probability vector/matrix
        return scores[actionTable[actions]] - probs[actionTable[actions]]

    # if it's maximizers turn
    if maxTurn:
        # return the index of the action that provides maximum benefit
        return np.argmax(np.array(
            [minimax(currDepth + 1, actions + 'R', False, probs, targetDepth),
             minimax(currDepth + 1, actions + 'P', False, probs, targetDepth),
             minimax(currDepth + 1, actions + 'S', False, probs, targetDepth)]))

    # minimizers turn
    else:
        return min(minimax(currDepth + 1, actions + 'R', True, probs, targetDepth),
                   minimax(currDepth + 1, actions + 'P', True, probs, targetDepth),
                   minimax(currDepth + 1, actions + 'S', True, probs, targetDepth))

def play_game():

    beats = {"R": "S", "P": "R", "S": "P"}
    moves = ["R", "P", "S"]
    computer_points = player_points = ties = 0

    # while we are not in a final state
    # (nobody won 8 games)
    while True:
        # update probabilities
        total = sum(counts)
        probs = [c/total if total != 0 else 0 for c in counts]
        # select computer move
        computer_move_int = minimax(0, '', True, probs)
        computer_move = moves[computer_move_int]

        # get player move
        player_move = input('Please enter your next move:')

        if player_move != "R" and player_move != "P" and player_move != "S" and player_move != "quit":
            continue
        if player_move == "quit":
            break

        if computer_move == player_move:
            ties += 1
        if beats[computer_move] == player_move:
            computer_points += 1
        if beats[player_move] == computer_move:
            player_points += 1

        # update counter
        counts[actionTable[computer_move + player_move]] += 1

        print("computer move: ", computer_move)
        print("player move: ", player_move)
        leaderboard = "computer_points %d  player_points: %d, ties: %d" % (computer_points, player_points, ties)
        print(leaderboard)
        print("\n--------------------------------------------------\n")

#initState = (0,0,0,0)
#scores = [3,5,2,9,12,5,23,23]
#treeDepth = math.log(len(scores), 2)
#print("The optimal value is:", end=" ")
#print(minimax(0, 0, True, scores, treeDepth))
# random:
# player history = 'RRSPSRPRPPSRPPSRPR'
# repeat sequence:
# player history = 'RRSRRSRRSRRSRRSRRS'
# repeat move:
# player history = 'RRRRRRRRRRRRRRRRRR'
# sequence of frequencies of player actions = (R = 22, P = 35, S = 43)
# probabilities = (22/sum, 35/sum, 43/sum)
# matrix of pair frequencies M = [[8, 11, 3]
#                                 [5, 10, 9]
#                                 [7, 12, 4]]
# probabilities = M / sum

play_game()
