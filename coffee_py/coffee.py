from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/concept")
def concept():
    return render_template('concept.html', title='Concept')

@app.route("/menu")
def menu():
    return render_template('menu.html', title='Menu')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')



if __name__ == '__main__':
    app.run(debug=True)