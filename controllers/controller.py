from app import app #
from models.game import * #
from models.player import * #
from flask import render_template #

@app.route('/') #
def rules(): 
    return render_template('home.html') 

@app.route('/<hand1>/<hand2>') #
def play_RPS(hand1, hand2): #
    player1 = Player("Susan", hand1) #
    player2 = Player("Louis", hand2) #
    pvp = Game() #
    
    winner = pvp.winner_result(player1, player2) #

    return render_template('game.html', player1 = player1, player2 = player2, winner = winner)
