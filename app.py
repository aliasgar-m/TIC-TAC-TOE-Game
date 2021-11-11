from flask import Flask, render_template, url_for, jsonify, request
import os
from game import Game

template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def home_page(name=None):
    return render_template('home_page.html', name=name)


@app.route('/play')
def play_game(name=None):
    return render_template('game_page.html', name=name)


@app.route('/info')
def info_page(name=None):
    return render_template('info_page.html', name=name)


@app.route('/about')
def about_page(name=None):
    return render_template('about_page.html', name=name)


@app.route('/play/move', methods=['POST'])
def move():
    state = request.get_json()

    game = Game()
    game.board = state.get('board')
    game.player = state.get('player')
    game.computer = state.get('computer') # have doubts here

    move = game.calculate_move()

    return jsonify(computerMove=move)

if __name__ == "__main__":
    app.run()