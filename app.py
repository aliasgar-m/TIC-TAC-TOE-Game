from flask import Flask, render_template
import os

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
