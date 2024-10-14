from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  list=[5, 8, 4, 6, 7]
  string='Hello World'
  return render_template('hello2.html', string=string)

