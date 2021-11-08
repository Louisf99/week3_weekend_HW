class Game():
    def __init__(self):
        self.chosen = {"rock": 1, "paper": 2, "scissors": 3}

    def player_choice(self, player):
        return self.chosen[player.choice]


    def winner_result(self, player1, player2): 

        winner = None

        if self.player_choice(player1) == self.player_choice(player2):
            winner = None
        elif self.player_choice(player1) == 1 and self.player_choice(player2) == 3:
            winner = player1
        elif self.player_choice(player1) == 3 and self.player_choice(player2) == 1:
            winner = player2
        elif self.player_choice(player1) == 2 and self.player_choice(player2) == 1:
            winner = player1
        elif self.player_choice(player1) == 1 and self.player_choice(player2) == 2:
            winner = player2
        elif self.player_choice(player1) == 3 and self.player_choice(player2) == 2:
            winner = player1
        else:
            winner = player2

        return winner

  


    # def play_game(self):
    #     if self.player1.choice == 1  and self.player2.choice == 1:
    #         return None
    #     if self.player1.choice == 2  and self.player2.choice == 2:
    #         return None
    #     if self.player1.choice == 3  and self.player2.choice == 3:
    #         return None
    #     elif self.player1.choice == 1 and self.player2.choice == 3:
    #         return self.player1
    #     elif self.player1.choice == 3 and self.player2.choice ==1:
    #         return self.player2
    #     elif self.player1.chosen[player.choice] == 1 and self.player2.choice == 2:
    #         return self.player2
    #     else:
    #         return self.player1
        