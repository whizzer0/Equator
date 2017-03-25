import random
from sigfigs import f

def generateQuestions():
  questions = {}
  i = 5
  while i > 0:
    value1 = random.randint(1,500)
    value2 = random.randint(1,500)
    solvalue = random.randint(1,3)
    #1: velocity (m/s), 2: distance (m), 3: time (s)
    if solvalue == 1:
      if value1 > value2 or random.randint(1,5) == 1:
        questions["q" + str(i)] = "If distance is " + str(value1) + "m and time is " + str(value2) + " seconds, what is the velocity?"
        questions["a" + str(i)] = f(float(value1) / float(value2), 3)
      else:
        questions["q" + str(i)] = "If distance is " + str(value2) + "m and time is " + str(value1) + " seconds, what is the velocity?"
        questions["a" + str(i)] = f(float(value2) / float(value1), 3)
      questions["u" + str(i)] = "m/s"
    elif solvalue == 2:
      questions["q" + str(i)] = "If velocity is " + str(value1) + " m/s and time is " + str(value2) + " seconds, what is the distance?"
      questions["a" + str(i)] = value1 * value2
      questions["u" + str(i)] = "m"
    elif solvalue == 3:
      questions["q" + str(i)] = "If velocity is " + str(value1) + " m/s and distance is " + str(value2) + "m, what is the time?"
      questions["a" + str(i)] = value1 * value2
      questions["u" + str(i)] = "seconds"
    i = i - 1
  print(questions)
  return questions
