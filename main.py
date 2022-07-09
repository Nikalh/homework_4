from flask import Flask

from utils import get_all_candidates, format_candidates, get_candidate_by_pk, get_candidate_by_skill

app = Flask(__name__)

@app.route("/")
def page_main():

    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result

@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    """Поиск кандидата по номеру"""
    candidate: dict = get_candidate_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result

@app.route("/skills/<skill>")
def page_skills(skill):
    """Поиск навыков"""
    skill_lower =skill.lower()
    candidate: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidate)
    return result


app.run()