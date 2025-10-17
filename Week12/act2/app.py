from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/show_image', methods=['POST'])
def show_image():
    image_url = request.form['image_url']
    return render_template('show_image.html', image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)