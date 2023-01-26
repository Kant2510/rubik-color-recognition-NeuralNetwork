from Routes import recognition as recog, solver

from flask import Flask, render_template, request, jsonify
import collections.abc
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/recognition', methods=['GET', 'POST'])
def recognition():
    result = recog.Recognition(request)
    return jsonify(result)


@app.route('/solve', methods=['GET', 'POST'])
def solve():
    result = solver.Solver(request)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
