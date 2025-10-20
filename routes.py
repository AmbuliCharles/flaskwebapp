#from portfolio import app
from flask import render_template, url_for, Flask


'''@app.get("/")
def homepage():
    return render_template('homepage.html')'''


app = Flask(__name__)

@app.get("/")
def homepage():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)