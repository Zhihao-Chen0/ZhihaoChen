from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <h1>Hello Flask!</h1>
     <p>Try visiting <a href="/cal/5">/cal/5</a> to see the square of 5.</p>'''

@app.route('/username/<name>')
def show_username(name):
    return f"<h1>{name} is learning Flask!</h1>"

@app.route('/cal/<int:number>')
def show_square(number):
    return f"<h1>The square of {number} is {number**2}</h1>"

if __name__ == "__main__":
    app.run(debug=True)