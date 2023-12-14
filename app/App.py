from flask import Flask, render_template, request

app = Flask(__name__)    # set FLASK_APP=App.py    flask run


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about.html')
def index():
    return render_template('about.html')

@app.route('/index.html')
def About():
    return render_template('index.html')


@app.route('/services.html')
def Services():
    return render_template('services.html')


@app.route('/contact.html')
def Contact():
    return render_template('contact.html')

@app.route('/careers.html')
def Careers():
    return render_template('careers.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html')


if __name__ == "__main__":
        app.run()






