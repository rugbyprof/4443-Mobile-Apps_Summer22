from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from rich import print

import json
import sys
import random
import math

description = """
Quizzler API 🚀

## Provides quiz questions for genuis people.
"""

quizApp = FastAPI(
    title="Quiz questions extroidanaire",
    description=description,
    version="0.0.1",
    terms_of_service="http://killzonmbieswith.us/terms/",
    contact={
        "name": "Cha Cha Schwarzenegger",
        "url": "http://killzonmbieswith.us/contact/",
        "email": "chacha@killzonmbieswith.us",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


class QuizBrain:

    def __init__(self):
        """ Setup the quiz brain class which opens a json file of questions and 
            loads them into our class. 
        """
        with open("questions.json") as f:
            self.questions = json.load(f)

        #print(self.questions)

        self.numQuestions = len(self.questions)

        self.id = 0

    def setCurrent(self, n):
        """ Sets the current question id
        Params:
           (int) id : value from 0 to max question item
        """
        self.id = n

    def getCurrentId(self):
        return self.id

    def nextQuestion(self):
        self.id += 1
        return self.id

    def getNumQuestions(self):
        return self.numQuestions

    def getQuestionText(self):
        return self.questions[self.id]['question']

    def getCorrectAnswer(self):
        return self.questions[self.id]['answer']

    def isFinished(self):
        return self.id == len(self.questions) - 1

    def reset(self):
        self.id = 0

    def addQuestion(self, question):
        self.questions.append(question)


"""
  ___  ___  _   _ _____ ___ ___ 
 | _ \/ _ \| | | |_   _| __/ __|
 |   / (_) | |_| | | | | _|\__ \
 |_|_\\___/ \___/  |_| |___|___/
"""


class Question(BaseModel):
    question: str
    answer: int


Q = QuizBrain()


@quizApp.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


@quizApp.post("/question/")
async def addQuestion(question: Question):
    Q.addQuestion(question)
    #print(Q.questions)
    return Q.questions


@quizApp.get("/question/")
async def getQuestion():
    """
    ### Description:
        Get a quiz question
    ### Params:
        None
    ### Returns:
        str: question text
    """
    question = None

    question = Q.getQuestionText()
    id = Q.getCurrentId()

    if question:
        return {"id": id, "question": question}

    return {"success": False}


@quizApp.get("/answer/")
async def getQuestionAns():
    """
    ### Description:
        Get a quiz question answer
    ### Params:
        None
    ### Returns:
        bool: question answer
    """
    answer = None

    answer = Q.getCorrectAnswer()

    if answer:
        return {"answer": answer}

    return {"success": False}


@quizApp.get("/next/")
async def next():
    """
    ### Description:
        Increment current question id
    ### Params:
        None
    ### Returns:
        int: question id
    """
    id = None

    id = Q.nextQuestion()

    if id:
        return {"id": id}

    return {"success": False}


@quizApp.get("/numQuestions/")
async def numQuestions():
    """
    ### Description:
        Get total questions
    ### Params:
        None
    ### Returns:
        int: total
    """
    count = 0

    count = Q.getNumQuestions()

    if count:
        return {"count": count}

    return {"success": False}


@quizApp.get("/finished/")
async def finished():
    """
    ### Description:
        Are you done?
    ### Params:
        None
    ### Returns:
        bool: finished answering all questions
    """
    done = 0

    done = Q.isFinished()

    if done in [True, False]:
        return {"done": done}

    return {"success": False}


@quizApp.get("/reset/")
async def reset():
    """
    ### Description:
        Reset id to 0 
    ### Params:
        None
    ### Returns:
        bool
    """
    id = None

    Q.reset()

    id = Q.getCurrentId()

    if id == 0:
        return {"reset": True}

    return {"success": False}


if __name__ == "__main__":
    #host="0.0.0.0" for running on server with domain name
    #or
    #host="ip.add.ress" for server ip

    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8888
    uvicorn.run("api:quizApp",
                host="127.0.0.1",
                port=port,
                log_level="info",
                reload=True)
