from flask import Flask
app = Flask('flaskapp')
@app.route('/')
def hello():
  return 'Hello, Freak!'
if __name__ == '__main__':
   app.run()
