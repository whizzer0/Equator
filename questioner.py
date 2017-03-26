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
      questions["u" + str(i)] = " m/s"
    elif solvalue == 2:
      questions["q" + str(i)] = "If velocity is " + str(value1) + " m/s and time is " + str(value2) + " seconds, what is the distance?"
      questions["a" + str(i)] = f(value1 * value2, 3)
      questions["u" + str(i)] = "m"
    elif solvalue == 3:
      questions["q" + str(i)] = "If velocity is " + str(value1) + " m/s and distance is " + str(value2) + "m, what is the time?"
      questions["a" + str(i)] = f(value1 * value2, 3)
      questions["u" + str(i)] = " seconds"
    i = i - 1
  #print(questions)
  return questions

def processResults(questions, q1, q2, q3, q4, q5):
  corrects = {}
  if f(q1,3) == questions["a1"]:
    corrects["q1"] = True
    corrects["s1"] = "✓"
    corrects["c1"] = "#4CAF50"
  else:
    corrects["q1"] = False
    corrects["s1"] = "✗"
    corrects["c1"] = "#F44336"
  if f(q1,3) == questions["a2"]:
    corrects["q2"] = True
    corrects["s2"] = "✓"
    corrects["c2"] = "#4CAF50"
  else:
    corrects["q2"] = False
    corrects["s2"] = "✗"
    corrects["c2"] = "#F44336"
  if f(q1,3) == questions["a3"]:
    corrects["q3"] = True
    corrects["s3"] = "✓"
    corrects["c3"] = "#4CAF50"
  else:
    corrects["q3"] = False
    corrects["s3"] = "✗"
    corrects["c3"] = "#F44336"
  if f(q1,3) == questions["a4"]:
    corrects["q4"] = True
    corrects["s4"] = "✓"
    corrects["c4"] = "#4CAF50"
  else:
    corrects["q4"] = False
    corrects["s4"] = "✗"
    corrects["c4"] = "#F44336"
  if f(q1,3) == questions["a5"]:
    corrects["q5"] = True
    corrects["s5"] = "✓"
    corrects["c5"] = "#4CAF50"
  else:
    corrects["q5"] = False
    corrects["s5"] = "✗"
    corrects["c5"] = "#F44336"
  print(corrects)
  return(corrects)
