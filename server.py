from flask import Flask, request, jsonify, send_from_directory, render_template
from backtrack import find_all_solutions
from time import time
from sqlite3 import connect
app = Flask(__name__)

def to_list_sudoku(dictionary_sudoku):
    list_sudoku = [[] for _ in range(9)]
    try:
        for i in range(9):
            for j in range(9):
                square = int(dictionary_sudoku[str(i)+str(j)])
                if square not in range(10):
                    return False
                list_sudoku[i].append(square)
    except:
        return False
    return list_sudoku

def to_string_sudoku(list_sudoku):
    string = ""
    for row in list_sudoku:
        for cell in row:
            string += str(cell)
    return string

def check_timeout(unix_time):
    return time() - unix_time > 10 # Check if 10 seconds have passed since the problem was POSTed. 

@app.route('/solver', methods=['POST'])
def add_message():
    from copy import deepcopy
    content = request.json
    sudoku = to_list_sudoku(content)
    if type(sudoku) == list:
        problem = deepcopy(sudoku)
        solutions, timed_out, time_spent = find_all_solutions(sudoku, check_timeout)
        if not timed_out and len(solutions) == 1:
            database = connect("times.db")
            key = to_string_sudoku(problem)
            database.execute("INSERT or IGNORE INTO times VALUES(?, ?)", (key, time_spent))
            database.commit()
        return jsonify((solutions, timed_out))
    return jsonify(False)

@app.route('/problems')
def get_problems():
    database = connect("times.db")
    return jsonify(database.execute("SELECT * FROM times ORDER BY time DESC").fetchall())

@app.route("/")
def home():
   return send_from_directory('static', "index.html")

@app.route('/<path:path>')
def send_static_page(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
