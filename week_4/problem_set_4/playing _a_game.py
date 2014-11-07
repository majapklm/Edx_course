def playGame(wordList):
 
    player_option = None
    player_hand = None
    while player_option != 'e':
        player_option = raw_input("Enter n to deal a new hand, r to replay the" +
                                  "  last hand, or e to end game: ").lower()
        if player_option == 'n':
            player_hand = dealHand(HAND_SIZE)
            playHand(player_hand.copy(), wordList, HAND_SIZE)
            print
        elif player_option == 'r':
                if player_hand != None:
                    playHand(player_hand.copy(), wordList, HAND_SIZE)
                    print
                else:
                        print("You ve not played a hand yet. Please play a" +
                      " new hand first!\n")
        elif player_option != 'e':
                            print("Invalid command.")
