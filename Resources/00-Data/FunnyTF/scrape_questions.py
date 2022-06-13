from bs4 import BeautifulSoup
from rich import print
import json


def getHtmlPage(fileName):

    with open(fileName) as f:
        data = f.read()

    return data


def cleanQuestions(questions):
    cleaned = []
    for question in questions:
        q = question.text.replace('\n', ' ')
        q = q.split()
        q = ' '.join(q[1:])
        cleaned.append(q)

    return cleaned


def cleanAnswers(answers):
    cleaned = []
    for answer in answers:
        #a = answer.text.replace('\n', ' ')
        ans = answer.text
        ans = ans.split()
        tf = ans[0].rstrip(',')
        exp = ' '.join(ans[1:])
        if len(exp) == 0:
            exp = None
        cleaned.append({'answer': tf, 'explanation': exp})

    return cleaned


def combineQA(questions, answers):
    for i in range(len(answers)):
        answers[i]['question'] = questions[i]
    return answers


if __name__ == '__main__':
    html = getHtmlPage('source.html')
    soup = BeautifulSoup(html, 'html.parser')

    questions = soup.find_all('h4', class_="wq-question-title")
    answers = soup.find_all('div', class_="desc")

    questions = cleanQuestions(questions)
    answers = cleanAnswers(answers)

    all = combineQA(questions, answers)

    with open('questions.json', 'w') as f:
        json.dump(all, f, indent=2)
