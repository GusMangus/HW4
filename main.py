from flask import Flask
from functions import load_candidates, Candidate, get_all, get_by_pk, get_by_skill
import json
app = Flask(__name__)
data = get_all(load_candidates('candidates.json'))

@app.route('/')
def index():
    str = '<pre>'
    for i in data:
        str += f'{i}'
    str += '</pre>'
    return str

@app.route('/candidates/<int:pk>')
def get_candidate(pk):
    candidate = get_by_pk(pk,data)
    if candidate:
        str = f'<img src = "{candidate.picture}">'
        str += f'<pre> {candidate} </pre>'
    else:
        str = "Кандидат не найден"
    return str

@app.route('/skills/<x>')
def get_skills(x):
    x = x.lower()
    data = load_candidates('candidates.json')
    candidates = get_by_skill(x, data)
    if candidates:
        str = '<pre> \n'
        for i in candidates:
            str += f'{i} \n'
        str += f'</pre>'
    else:
        str = "Навык не найден"
    return str


if __name__ == "__main__":
    app.run(port=1984)
