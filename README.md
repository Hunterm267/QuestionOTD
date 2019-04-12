#QuestionOTD.py
author: HunterM267
usage: `python3 QuestionOTD.py <.in filename> <webhook url>`
input format: new-line separated questions. '#' at the beginning of the line indicates a used question
behavior: when run, selects a random, unused question from the .in file. if no unused questions exist,
          all questions will be 'unmarked', thus repeating questions