import random

def generateQuestions():
  questions = []
  i = 5
  while i > 0:
    value1 = random.randint(1,500)
    value2 = random.randint(1,500)
    solvalue = random.randint(1,3)
    #1: velocity (m/s), 2: distance (m), 3: time (s)
    if solvalue == 1:
      questions.append("If distance is " + str(value1) + "m and time is " + str(value2) + " seconds, what is the velocity?")
    elif solvalue == 2:
      questions.append("If velocity is " + str(value1) + "m/s and time is " + str(value2) + " seconds, what is the distance?")
    elif solvalue == 3:
      questions.append("If velocity is " + str(value1) + "m/s and distance is " + str(value2) + "m, what is the time?")
    i = i - 1
  endqs = {
    "q1": questions[0],
    "q2": questions[1],
    "q3": questions[2],
    "q4": questions[3],
    "q5": questions[4]
  }
  return endqs
