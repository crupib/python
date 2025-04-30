from flask import Flask
app = Flask('flaskapp')
@app.route('/')
@app.route('/hello')
def hello():
  return 'Hello, Freak!'
if __name__ == '__main__':
   app.run()
