import scrabble

# Set the game
def start():
    try:
        players = int(input("How many players? "))
    except TypeError as e:
        print("A number is expected")
        print(e)
        
    try:
        words = int(input("How many words per player? "))
    except TypeError as e:
        print("A number is expected")
        print(e)

    player_to_words = {}

    for num in range(players):
        print("Type the player's name " + str(num) + ": ")
        name = input()
        player_to_words[name] = []

    for player in player_to_words.keys():
        print("Type the words which player "+ "\"" + str(player) + "\"" + " wants to play: ")
        for num in range(words):
            word = input()
            player_to_words[player].append(word.upper())
    
    print("The settings are:")
    print(player_to_words)
    print("\nPress Enter to start")
    input()
    
    print(scrabble.play_game(player_to_words))


# Score a Game
start()