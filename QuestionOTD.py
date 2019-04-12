#QuestionOTD.py
#author: HunterM267
#usage: python3 QuestionOTD.py <.in filename> <webhook url>
#input format: new-line separated questions. '#' at the beginning of the line indicates a used question
#behavior: when run, selects a random, unused question from the .in file. if no unused questions exist,
#          all questions will be 'unmarked', thus repeating questions

import sys
from random import randint
import requests

def main(args):
    if len(args) < 3:
        print('Syntax: python3', args[0], '<.in filename> <webhook url>')
    fileName = args[1]
    url = args[2]

    newQuestions, questions = getQuestions(fileName)
    if len(questions) == 0:
        print("ERROR: input file cannot be empty")
        sys.exit(1)
    if (len(newQuestions) == 0): #check if all the questions are marked as sent, and if so, unmark all of them
        unmarkQuestions(fileName)
        newQuestions, questions = getQuestions(fileName)
    question = selectQuestion(newQuestions, questions, fileName)

    post2Discord(question, url)

def getQuestions(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        questions = [x.strip() for x in lines]
        newQuestions = [x for x in lines if x[0] != '#'] #exclude 'marked' (already sent) questions
    return newQuestions, questions


def selectQuestion(newQuestions, questions, fileName):
    if len(newQuestions) == 1:
        question = newQuestions[0].strip()
    else:
        question = newQuestions[randint(1,len(newQuestions)-1)].strip()
    with open(fileName, "w") as f:
        for line in questions:
            if line == question:
                f.write("#"+line+'\n')
            else:
                f.write(line+'\n')
    return question

def unmarkQuestions(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
    with open(fileName, "w") as f:
        for line in lines:
            if line.strip("\n")[0] == '#':
                f.write(line[1:])

def post2Discord(question, url):
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, json={"content": question}, headers=headers)
    if r.status_code != 204:
        print("WARNING: error sending message to discord")


if __name__ == '__main__':
    main(sys.argv)