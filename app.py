from flask import Flask, render_template, request
from questioner import generateQuestions, processResults
app = Flask(__name__)
app.debug = True
questions = {}

@app.route("/example", methods=["GET"])
def example():
	return render_template("example.html", data=None)

@app.route("/", methods=["GET"])
def form():
  global questions
  questions = generateQuestions()
  return render_template("form.html", questions=questions)

@app.route("/results", methods=["POST"])
def results():
  marked = processResults(questions, [request.form["question1"], request.form["question2"], request.form["question3"], request.form["question4"], request.form["question5"]])
  return render_template("results.html", results=[request.form["question1"], request.form["question2"], request.form["question3"], request.form["question4"], request.form["question5"]], marked=marked, questions=questions)
	
if __name__ == "__main__":
	app.run()
