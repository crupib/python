from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def result():
  students=[('Anil',55),('Rajeev',40),('Leela',60),('Zuber',75),('John',30)]
  return render_template('langs.html', students=students)
