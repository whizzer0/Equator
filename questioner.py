import random
from sigfigs import f

form = {"vdt1":"velocity", "vdt2":"distance", "vdt3":"time"}
unit = {"vdt1":" m/s", "vdt2":"m", "vdt3":" seconds"}

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

def processResults(questions, results):
  corrects = {}
  i = 5
  while i > 0:
    if f(results[i-1],3) == questions["a"+str(i)]:
      corrects["q"+str(i)] = True
      corrects["s"+str(i)] = "✓"
      corrects["c"+str(i)] = "#4CAF50"
      corrects["a"+str(i)] = ""
    else:
      corrects["q"+str(i)] = False
      corrects["s"+str(i)] = "✗"
      corrects["c"+str(i)] = "#F44336"
      corrects["a"+str(i)] = questions["a"+str(i)] + questions["u"+str(i)]
    i = i - 1
  return(corrects)
