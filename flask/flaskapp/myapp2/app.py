from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  langs=['C', 'C++', 'Java', 'Python', 'PHP']
  return render_template('langs.html', langs=langs)
