import random
from sigfigs import f

eqs = ["dvt", "Fma", "mmv", "WFd", "WPT", "FPa", "mρV", "QIt", "WVQ", "VIR"]
form = {"dvt1":"distance", "dvt2":"velocity", "dvt3":"time", "Fma1":"force", "Fma2":"mass", "Fma3":"acceleration", "mmv1":"momentum", "mmv2":"mass", "mmv3":"velocity", "WFd1":"work done", "WFd2":"force", "WFd3":"distance", "WPT1":"energy transferred", "WPT2":"power", "WPT3":"time", "FPa1":"force", "FPa2":"pressure", "FPa3":"area", "mρV1":"mass", "mρV2":"density", "mρV3":"volume", "QIt1":"charge", "QIt2":"current", "QIt3":"time", "WVQ1":"energy transferred", "WVQ2":"voltage", "WVQ3":"charge", "VIR1":"voltage", "VIR2":"current", "VIR3":"resistance"}
unit = {"dvt1":"m", "dvt2":" m/s", "dvt3":" seconds", "Fma1":"N", "Fma2":"kg", "Fma3":" m/s²", "mmv1":"kg m/s", "mmv2":"kg", "mmv3":" m/s", "WFd1":"J", "WFd2":"N", "WFd3":"m", "WPT1":"J", "WPT2":"W", "WPT3":" seconds", "FPa1":"N", "FPa2":" Pa", "FPa3":"m²", "mρV1":"kg", "mρV2":" kg/m³", "mρV3":"m³", "QIt1":" C", "QIt2":" A", "QIt3":" seconds", "WVQ1":"J", "WVQ2":"V", "WVQ3":" C", "VIR1":"V", "VIR2":"A", "VIR3":"Ω"}
sets = {"all":eqs,"forces":["dvt", "Fma", "mmv"],"electricity":["QIt", "WVQ", "VIR"],"waves":[],"energy":["WFd", "WPT", "FPa"],"states":["FPa", "mρV"],"magnetism":[],"radioactivity":[]}

def generateQuestions(module):
  questions = {}
  i = 5
  while i > 0:
    value1 = random.randint(2,500)
    value2 = random.randint(2,500)
    eq = sets[module][random.randint(0,len(sets[module])-1)]
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
  print(results)
  i = 5
  while i > 0:
    if results[i-1] == "":
      results[i-1] = 0
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
