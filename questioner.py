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
    order = random.randint(1,3)
    if order == 1:
      #v × t = d
      questions["q" + str(i)] = "If the " + form[eq + "2"] + " is " + str(value1) + unit[eq + "2"] + " and the " + form[eq + "3"] + " is " + str(value2) + unit[eq + "3"] + ", what is the " + form[eq + "1"] + "?"
      questions["a" + str(i)] = f(value1 * value2, 3)
      questions["u" + str(i)] = unit[eq + "1"]
    elif order == 2:
      #d ÷ t = v
      questions["q" + str(i)] = "If the " + form[eq + "1"] + " is " + str(value1) + unit[eq + "1"] + " and the " + form[eq + "3"] + " is " + str(value2) + unit[eq + "3"] + ", what is the " + form[eq + "2"] + "?"
      questions["a" + str(i)] = f(value1 / value2, 3)
      questions["u" + str(i)] = unit[eq + "2"]
    elif order == 3:
      #d ÷ v = t
      questions["q" + str(i)] = "If the " + form[eq + "1"] + " is " + str(value1) + unit[eq + "1"] + " and the " + form[eq + "2"] + " is " + str(value2) + unit[eq + "2"] + ", what is the " + form[eq + "3"] + "?"
      questions["a" + str(i)] = f(value1 / value2, 3)
      questions["u" + str(i)] = unit[eq + "3"]
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
