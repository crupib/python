from flask import Flask
app = Flask('flaskapp')
@app.route('/greeting')
@app.route('/welcome')
def welcome():
  return '<h2>Welcome to Freak Framework</h2>'
if __name__ == '__main__':
   app.run()
