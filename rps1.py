
# function that reads from file a user

# function that saves all games for a user into a file

# how the file looks
#   username
#

# for easy mode the game is using just random strategy



# Care este starea ?

# pentru rock avem 1, pentru paper avem 2, pentru scissors avem 3
#                 'R'                  'P'                     'S'

import pymongo, random

# print(random.randint(0,2))

# list of moves (miscarea calculatorului, miscarea jucatorului
# [(1,0), (2,1), (0,0), (0,0)]
# probabilitaea o calculez asa: cat la 100 din toate  avem 0 etc..
#
# exemplu de probabilitate pe exemplul de pe randul anterior:
#           ce sanse sunt ca R sa apara dupa R : ,
#           ce sanse sunt ca P sa apara dupa P,
#           ce sanse sunt ca S sa apara dupa S


# apoi o alta strategie este pe baza tiparelor:
#  - pot inregistra mai multe tipare si le adaug scoruri in functie de cat de bune sunt.

# mai am o strategie : win-keep, lose-shift
# pot alege prezicatorul: jucatorul alege o mutare in functie de ce mutare am avut eu anterior
#                         jucatorul alege o mutare indiferent de ce mutare am avut eu anterior


# primele 3 jocuri folosim strategia random

# 3 niveluri: easy, medium, hard

# username

def play_hard_mode(old_player_moves):
    beats = {"R": "S", "P": "R", "S": "P"}
    moves = ["R", "P", "S"]
    winning_strategy_threshold = 5
    player_moves = list(old_player_moves)
    strategies_score = {"move_patterns": 10, "rotation": 10}
    move_patterns = []
    computer_points = player_points = ties = 0
    computer_move = ''
    last_computer_move = ''
    last_player_move = ''
    last_player_win = False

    while True:
        chosen_strategy = "rotation"
        if len(player_moves) < 3 or last_computer_move == '':
            # print("RANDOM1")
            computer_move_int = random.randint(0, 2)
            computer_move = moves[computer_move_int]

        else:

            # choose strategy based on their scores
            if strategies_score["move_patterns"] < strategies_score["rotation"]:
                chosen_strategy = "rotation"
            else:
                chosen_strategy = "move_patterns"

            if chosen_strategy == "rotation":
                # rotation strategy

                if last_player_win:
                    # means there is a better chance that player will do the same move
                    for key in beats:
                        if beats[key] == last_player_move:
                            computer_move = key
                else:
                    # means there is a better chance that player will change to a move that beats computer's last move
                    if last_computer_move == "R":
                        computer_move = "S"
                    elif last_computer_move == "P":
                        computer_move = "R"
                    else:
                        computer_move = "P"

            # if chosen_strategy == "move_patterns":
            #     pattern strategy

        # iau inputul
        player_move = input("choose 'R', 'P', 'S': ");

        if player_move != "R" and player_move != "P" and player_move != "S" and player_move != "quit":
            continue
        if player_move == "quit":
            break

        if computer_move == player_move:
            ties += 1
        elif beats[computer_move] == player_move:
            computer_points += 1
            last_player_win = False

            # modify scores for strategies
            if chosen_strategy == "rotation":
                strategies_score["rotation"] += 1
                strategies_score["move_patterns"] -= 1
        else:
            player_points += 1
            last_player_win = True

            # modify scores for strategies
            if chosen_strategy == "rotation":
                strategies_score["rotation"] -= 1
                strategies_score["move_patterns"] += 1
        print('computer points:', computer_points)
        print('player points:', player_points)
        print('ties:', ties)
        print('strategies_score:', strategies_score)

        last_computer_move = computer_move
        last_player_move = player_move



    return player_moves











def play_medium_mode(old_player_moves, old_counts):
    beats = {"R": "S", "P": "R", "S": "P"}
    moves = ["R", "P", "S"]
    counts = {
        "RR": 0,
        "RS": 0,
        "RP": 0,
        "PR": 0,
        "PS": 0,
        "PP": 0,
        "SR": 0,
        "SS": 0,
        "SP": 0,
    }

    computer_points = player_points = ties = 0

    if len(old_counts) == 9:
        counts = dict(old_counts)
    player_moves = list(old_player_moves)
    print('player_moves:', player_moves)
    last_player_move = player_moves[-1]

    while True:
        # print("player_moves: ", player_moves)
        # print("counts: ", counts)
        # print("last_player_move: ", last_player_move)

        # calculul strategiei
        if len(player_moves) < 3:
            # fac random
            # print("RANDOM1")
            computer_move_int = random.randint(0,2)
            computer_move = moves[computer_move_int]
        else:
            # aleg din istoric in functie de frecvente
            if random.random() > 0.5:
                if counts[last_player_move + "R"] == counts[last_player_move + "P"] == counts[last_player_move + "S"]:
                    # print("RANDOM2")
                    computer_move_int = random.randint(0,2)
                    computer_move = moves[computer_move_int]
                elif counts[last_player_move + "R"] > counts[last_player_move + "P"] and counts[last_player_move + "R"] > counts[last_player_move + "S"]:
                    computer_move = "P"
                elif counts[last_player_move + "P"] > counts[last_player_move + "S"]:
                    computer_move = "S"
                else:
                    computer_move = "R"
            else:
                # print("RANDOM3")
                computer_move_int = random.randint(0, 2)
                computer_move = moves[computer_move_int]

        # iau inputul
        player_move = input("choose 'R', 'P', 'S': ");

        if player_move != "R" and player_move != "P" and player_move != "S" and player_move != "quit":
            continue
        if player_move == "quit":
            break

        if computer_move == player_move:
            ties += 1
        elif beats[computer_move] == player_move:
            computer_points += 1
        else:
            player_points += 1

        print("computer move: ", computer_move)
        print("player move: ", player_move)
        leaderboard = "computer_points %d  player_points: %d, ties: %d" % (computer_points, player_points, ties)
        print(leaderboard)
        print("\n--------------------------------------------------\n")

        # adaugam mutarea playerului in istoric
        player_moves.append(player_move)

        # crestem counts
        if last_player_move != '':
            print('last_player_move:', last_player_move)
            print('player_move:', player_move)
            counts[last_player_move + player_move] += 1

        last_player_move = player_move

    return player_moves, counts


# function that configures the game at the begining: dificulty level, username, searches in the file for old games
#  with the same username



# beat dictionary: "R":"S", "S":"P", "P":"R"



# I need a score to keep: computer_points, player_points, ties

# for easy mode the computer choose randomly from moves with 1/3 prob each
def play_easy_mode():
    beats = {"R": "S", "P": "R", "S": "P"}
    moves = ["R", "P", "S"]
    computer_points = player_points = ties = 0

    while True:
        computer_move_int = random.randint(0,2)
        computer_move = moves[computer_move_int]

        # print("computer_move", computer_move)

        player_move = input("give your move(R,P,S) or type quit:")

        if player_move != "R" and player_move != "P" and player_move != "S" and player_move != "quit":
            continue
        if player_move == "quit":
            break

        if computer_move == player_move:
            ties += 1
        elif beats[computer_move] == player_move:
            computer_points += 1
        else:
            player_points += 1

        print("computer move: ", computer_move)
        print("player move: ", player_move)
        leaderboard = "computer_points %d  player_points: %d, ties: %d" % (computer_points, player_points, ties)
        print(leaderboard)
        print("\n--------------------------------------------------\n")



def main():
    # username = input("give me an username")
    username = "cristi"
    level = input("choose a level: 1->easy, 2->medium, 3->hard")

    print(level)
    if level == '1':
        # play in easy mode
        play_easy_mode()

    if level != '1':
        client = pymongo.MongoClient('localhost', 27017)
        users = client.test.users
        data = users.find_one({"username": username}, {"_id": 0, "player_moves": 1, "counts": 1})
        old_player_moves = []
        old_counts = {}
        if data is None:
            users.insert_one({"username": username, "player_moves": (), "counts": {}})
        else:
            old_player_moves = data["player_moves"]
            old_counts = data["counts"]
        if level == '2':
            new_player_moves, new_counts = play_medium_mode(old_player_moves, old_counts)

        if level == '3':
            new_moves = play_hard_mode(old_player_moves)
        # new_player_moves = [10, 10]
        # new_counts = {'RR': 0}
        #users.update_one({"username": username}, {'$set': {"player_moves": new_player_moves, "counts": new_counts}})

        client.close()


main()

#play_easy_mode()
# play_medium_mode()
