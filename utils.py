import json

#загружаем кандидатов из файла
def load_json() -> list[dict]:
#def load_candidates(data):
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        #print(candidates)
    return candidates


def format_candidates(candidates: list[dict]) -> str:
    """Форматирование списка кандидатов"""
    result = '<pre>'

    for candidate in candidates:
        result += f"""
            {candidate['name']}\n
            {candidate['position']}\n
            {candidate['skills']}
        """
    result +='</pre>'
    return result

def get_all_candidates() -> list[dict]:
    """Получение полного списка кандидатов"""
    return load_json()

def get_candidate_by_pk(uid: int) -> dict | None:
    """Определяем кандидата по номеру"""
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['pk'] == uid:
            return candidate
    return None

def get_candidate_by_skill(skill: str) -> list[dict]:
    """Выбираем кандидатов по навыку"""
    candidates = get_all_candidates()
    result =[]
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(", "):
            result.append(candidate)
    return result