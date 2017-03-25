from flask import Flask, render_template, request
from questioner import generateQuestions
app = Flask(__name__)
app.debug = True

@app.route("/example", methods=["GET"])
def example():
	return render_template("example.html", data=None)

@app.route("/", methods=["GET"])
def form():
  questions = generateQuestions()
  return render_template("form-alt.html", questions=questions)

@app.route("/results-alt", methods=["POST"])
def results():
	return render_template("results-alt.html", data=results)
	
if __name__ == "__main__":
	app.run()
