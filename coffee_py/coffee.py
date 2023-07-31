from flask import Flask, render_template, url_for
import pandas as pd
from flask_restful import Api, Resource

sheet_id = '1h8sowdIUH9332VHnB-XO0_E6pnHK1XCGdw6cB1MEYbM'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
records = df.to_dict(orient='records')
#print(records)


#instantiate new Flask Aplication Object
app = Flask(__name__)
# initialize API object for the Flask aplication
api = Api(app)

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
    return render_template('menu.html', title='Menu', records=records)

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


# Api requests
class All(Resource):

    def get(self):
        return records

# Register API Resources 
api.add_resource(All, '/api/')

if __name__ == '__main__':
    app.run(debug=True)