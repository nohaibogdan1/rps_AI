
# function that reads from file a user

# function that saves all games for a user into a file

# how the file looks
#   username
#

# for easy mode the game is using just random strategy



# Care este starea ?

# pentru rock avem 1, pentru paper avem 2, pentru scissors avem 3
#                 'R'                  'P'                     'S'

import pymongo, json, random

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

def play_medium_mode():
    moves = list()

    nr_games = 0

    while True:
        nr_games += 1

        # calculul strategiei
        if nr_games < 3:
            # fac random
            computer_move_int = random.randint(0,2)





        # iau inputul
        player_move = input("choose 'R', 'P', 'S'");




# function that configures the game at the begining: dificulty level, username, searches in the file for old games
#  with the same username


def before_game():
# get the username from player

    # username = input("give me an username")
    username="cristi"
    level = input("choose a level: 1->easy, 2->medium, 3->hard")


# get the difficulty level

# if level is greater then easy lookup into the database for the username

    return username, level



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

        print("computer_move", computer_move)

        player_move = input("give your move(R,P,S) or type quit:")

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


        print("computer move: ", computer_move)
        print("player move: ", player_move)
        leaderboard = "computer_points %d  player_points: %d, ties: %d" % (computer_points, player_points, ties)
        print(leaderboard)
        print("\n--------------------------------------------------\n")








def db_settings():
    client = pymongo.MongoClient()
    db = client.test
    users = db.users
    print(users)
    users.insert_one({"username":"Smith"})

    client.close()


# db_settings()




def main():
    username, level = before_game()
    print(level)
    if level == '1':
        # play in easy mode
        play_easy_mode()



# main()

play_easy_mode()