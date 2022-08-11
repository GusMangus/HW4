import json

def load_candidates(filename):
    """загрузит данные из файла"""
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data

class Candidate():
    def __init__(self, pk, name, picture, position, skills):
        self.pk = pk
        self.name = name
        self.picture = picture
        self.position = position
        self.skills = skills

    def __repr__(self):
        return f"{self.name} \n"\
               f"{self.position} \n"\
               f"{self.skills} \n"\
               f"\n"\



def get_all(data):
    '''покажет всех кандидатов'''
    candidates = []
    for item in data:
        pk = item['pk']
        name = item['name']
        picture = item['picture']
        position = item['position']
        skills = item['skills']
        candidate = Candidate(pk, name, picture, position, skills)
        candidates.append(candidate)
    return candidates

def get_by_pk(pk, data):
    'вернет кандидата по pk'
    for item in data:
        if item.pk == pk:
            return item

def get_by_skill(skill_name, data):
    '''вернет кандидатов по навыку'''
    candidates =[]
    for item in data:
        if skill_name in item['skills']:
            name = item['name']
            candidates.append(name)
    return candidates