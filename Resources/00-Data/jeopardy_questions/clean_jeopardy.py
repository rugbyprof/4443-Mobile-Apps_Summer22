import json
import sys
from rich import print


def getCategories(data):
    categories = {}
    for question in data:
        cat = question['category']
        if not cat in categories:
            categories[cat] = 0
        categories[cat] += 1

    return categories


if __name__ == '__main__':

    with open('jeopardy_questions_all.json') as f:
        data = json.load(f)
    print(len(data))

    cats = getCategories(data)
    print(cats)
    print(len(cats))
    sys.exit()

    with open('jeopardy_questions.json', 'w') as f:
        data = json.dump(data, f, indent=2)
