from flask import Flask, render_template
from utils import *
from classes.candidates import Candidate

app = Flask(__name__)
candidates = load_candidates_from_json()


@app.route("/")
def candidates_list():
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id>")
def candidate_card(id):
    candidate = get_candidate(id)
    return render_template("card.html", candidate=candidate, )


@app.route("/search/<candidate_name>")
def search_candidate_by_name(candidate_name):
    candidate_by_name = get_candidates_by_name(candidate_name)
    return render_template("search_name.html", candidate_by_name=candidate_by_name)


@app.route("/skills/<skill>")
def search_candidate_by_skill(skill):
    candidate_by_skill = get_candidates_by_skill(skill)
    return render_template("search_skills.html", skill=skill, candidate_by_skill=candidate_by_skill)


app.run(debug=True)
