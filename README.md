# Equator

Equator is a tool to generate questions to test your knowledge of GCSE Physics formulae. It is part of the Material Revision project.

Equator uses:

* [Material Design Lite](https://github.com/google/material-design-lite)
* [Material Design Icons](https://github.com/Templarian/MaterialDesign)

## Running Equator

Enter the directory with the files from this repository. Then, use the command `python app.py` and head to [127.0.0.1:5000](http://127.0.0.1:5000) in a browser. Equator should run fine in both Python 2 and Python 3, and should also work offline as MDL is included (you may need to install a local copy of [Roboto](https://fonts.google.com/specimen/Roboto)).

## Progress

Equator is very much a WIP, but you can use it. Currently, Equator can:

* Generate and offer five questions
* Allow the user to select a module of the syllabus from which to generate questions
* Accept user input for these questions
* Mark these questions correct/incorrect and offer the correct answer when wrong
* Offer a percentage score for the user's results
* Look fancy (drop shadows make everything better)

## Soon™

Currently working on making Equator able to:

* Support a customisable number of questions (the question marker is now extensible but the results page still has 5 hardcoded)
* Use an improved method for generating questions that doesn't result in lots of huge numbers
