from flask import Flask, render_template

app = Flask(__name__)

# Register the 'isodd' filter with Flask
@app.template_filter('isodd')
def isodd(x):
    if isinstance(x, int):  # Make sure x is an integer
        return x % 2 == 1  # Return True if odd, False if even
    return False  # If x is not an integer, return False

@app.route('/')
def index():
    a = 3  # Example value for a
    b = 4  # Example value for b
    return render_template('index.html', a=a, b=b)

if __name__ == '__main__':
    app.run(debug=True)

