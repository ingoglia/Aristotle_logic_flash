from flask import Flask, render_template
import random
app = Flask(__name__)

cat_sent = {'a':'Every B is A',
            'e':'No B is A',
            'i':'Some B is A', 
            'o':'Some B is not A'}
cat_sent_q = list(cat_sent.keys())
cat_q = random.choice(cat_sent_q)

@app.route("/")
def welcome():
    return render_template(
            'index.html')

@app.route("/categorical_sentence_types")
def types():
    return render_template(
            "cat_sent_type.html",
            cat_q = cat_q)

@app.route("/understand_figures")
def figures():
    return "Put fill in the blank tests"

@app.route("/major_minor")
def major_minor():
    return "find the major and minor term"

@app.route("/figure_names")
def figure_name():
    return "select which figure to study"

@app.route("/figure_names/first")
def first_fig():
    return "first figure tests"

@app.route("/figure_name/second")
def second_fig():
    return "second figure tests"

@app.route("/figure_name/third")
def third_fig():
    return "third figure tests"

@app.route("/figure_name/all")
def all_fig():
    return "Quiz yourself on all figures"

if __name__ == "__main__":
    app.run()

