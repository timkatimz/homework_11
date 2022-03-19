import json


def load_candidates_from_json():
    with open("candidates.json") as file:
        candidates = json.load(file)
    return candidates


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate_id == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name):
    candidates = []
    for candidate in load_candidates_from_json():
        if candidate_name in candidate["name"]:
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name):
    skills = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"]:
            skills.append(candidate)
    return skills



# - `load_candidates_from_json(path)` – возвращает список всех кандидатов
# - `get_candidate(candidate_id)` – возвращает одного кандидата по его id
# - `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
# - `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку
