from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/<name>/<int:age>')
def hello(name,age):
  return render_template('hello.html',name=name, age=age)
