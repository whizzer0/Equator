from flask import Flask, render_template, request
from questioner import generateQuestions, processResults
app = Flask(__name__)
app.debug = True
questions = {}

@app.route("/example", methods=["GET"])
def example():
	return render_template("example.html", data=None)

@app.route("/", methods=["GET"])
def formAll():
  global questions
  questions = generateQuestions("all")
  return render_template("form.html", questions=questions)
  
@app.route("/forces", methods=["GET"])
def formForces():
  global questions
  questions = generateQuestions("forces")
  return render_template("form.html", questions=questions)
  
@app.route("/electricity", methods=["GET"])
def formElectricity():
  global questions
  questions = generateQuestions("electricity")
  return render_template("form.html", questions=questions)
  
@app.route("/waves", methods=["GET"])
def formWaves():
  global questions
  questions = generateQuestions("waves")
  return render_template("form.html", questions=questions)
  
@app.route("/energy", methods=["GET"])
def formEnergy():
  global questions
  questions = generateQuestions("energy")
  return render_template("form.html", questions=questions)
  
@app.route("/states", methods=["GET"])
def formStates():
  global questions
  questions = generateQuestions("states")
  return render_template("form.html", questions=questions)

@app.route("/magnetism", methods=["GET"])
def formMagnetism():
  global questions
  questions = generateQuestions("magnetism")
  return render_template("form.html", questions=questions)

@app.route("/radioactivity", methods=["GET"])
def formRadioactivity():
  global questions
  questions = generateQuestions("radioactivity")
  return render_template("form.html", questions=questions)

@app.route("/results", methods=["POST"])
def results():
  marked = processResults(questions, [request.form["question1"], request.form["question2"], request.form["question3"], request.form["question4"], request.form["question5"]])
  return render_template("results.html", results=[request.form["question1"], request.form["question2"], request.form["question3"], request.form["question4"], request.form["question5"]], marked=marked, questions=questions)
	
if __name__ == "__main__":
	app.run()
