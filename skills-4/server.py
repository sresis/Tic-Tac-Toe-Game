"""Flask server for Javascript assessment.

IMPORTANT: you don't need to change this file at all to finish
the assessment!
"""

from flask import Flask, render_template, jsonify
from random import choice

app = Flask(__name__)

COLORS = ['olive', 'yellow', 'navy', 'blue', 'teal', 'aqua', 'aliceblue',
          'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque',
          'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown',
          'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral',
          'cornflowerblue', 'cornsilk', 'crimson', 'cyan', ]


@app.route('/')
def show_index():
    """Show the index page"""

    return render_template('index.html')


@app.route('/randomcolor')
def random_color():
    """Get a random color."""

    return choice(COLORS)


@app.route('/todos')
def get_todos():
    return jsonify({'todos': [{'title': 'Get groceries',
                               'is_done': False},
                              {'title': 'Take a break',
                               'is_done': True},
                              {'title': 'Take a nice long nap',
                               'is_done': True},
                              {'title': 'Eat a big sandwich',
                               'is_done': False},
                              {'title': 'Bake cookies',
                               'is_done': False},
                              {'title': 'Talk to friends',
                               'is_done': True}, ]})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
