import random
from sigfigs import f

eqs = ["dvt"]
form = {"dvt1":"distance", "dvt2":"velocity", "dvt3":"time"}
unit = {"dvt1":"m", "dvt2":" m/s", "dvt3":" seconds"}

def generateQuestions():
  questions = {}
  i = 5
  while i > 0:
    value1 = random.randint(2,500)
    value2 = random.randint(2,500)
    eq = eqs[random.randint(0,len(eqs)-1)]
    order = 1
    if order == 1:
      questions["q" + str(i)] = "If the " + form[eq + "2"] + " is " + str(value1) + unit[eq + "2"] + " and the " + form[eq + "3"] + " is " + str(value2) + unit[eq + "3"] + ", what is the " + form[eq + "1"] + "?"
      questions["a" + str(i)] = f(value1 * value2, 3)
      questions["u" + str(i)] = unit[eq + "1"]
#   if solvalue == 1:
#     if value1 > value2 or random.randint(1,5) == 1:
#       questions["q" + str(i)] = "If distance is " + str(value1) + "m and time is " + str(value2) + " seconds, what is the velocity?"
#       questions["a" + str(i)] = f(float(value1) / float(value2), 3)
#     else:
#       questions["q" + str(i)] = "If distance is " + str(value2) + "m and time is " + str(value1) + " seconds, what is the velocity?"
#       questions["a" + str(i)] = f(float(value2) / float(value1), 3)
#     questions["u" + str(i)] = " m/s"
#   elif solvalue == 2:
#     questions["q" + str(i)] = "If velocity is " + str(value1) + " m/s and time is " + str(value2) + " seconds, what is the distance?"
#     questions["a" + str(i)] = f(value1 * value2, 3)
#     questions["u" + str(i)] = "m"
#   elif solvalue == 3:
#     questions["q" + str(i)] = "If velocity is " + str(value1) + " m/s and distance is " + str(value2) + "m, what is the time?"
#     questions["a" + str(i)] = f(value1 * value2, 3)
#     questions["u" + str(i)] = " seconds"
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
