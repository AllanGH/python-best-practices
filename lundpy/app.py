from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Return a welcome message
    return "Welcome to the Python Best Practices Workshop!"

if __name__ == '__main__':
    app.run(debug=True)
