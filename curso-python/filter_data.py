from ctypes.wintypes import WPARAM


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():

    all_py = [worker["name"] for worker in DATA if worker["language"] == "python"]

    all_py_h = list(filter(lambda worker: worker["language"] == "python" , DATA))
    all_py_h = list(map(lambda worker: worker["name"], all_py_h))

    for worker in all_py_h:
        print("Sabe Python: " + worker)

    all_platzi = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    all_platzi_h = list(filter(lambda worker: worker["organization"] == "Platzi" , DATA))
    all_platzi_h = list(map(lambda worker: worker["name"], all_platzi_h))

    for worker in all_platzi_h:
        print("Trabaja en Platzi: "+ worker)

    adults= list(filter(lambda worker: worker["age"]>18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    adults_c = [worker["name"] for worker in DATA if worker['age']>18]

    old_people = list(map(lambda worker: worker | {"old": worker["age"]>70} , DATA))

    old_people_c = [worker | {"old":worker['age']>18} for worker in DATA]

    for worker in adults_c:
        print("Mayor de 18 años: "+ worker)

    for worker in old_people_c:
        print( worker)

if __name__ == '__main__':
    main()    