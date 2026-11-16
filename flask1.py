
from flask import Flask


app=Flask(__name__)

@app.route("/")

def home():
    return "<h1>My first flask application in tutorials</h1>"

@app.route("/about")

def about():
    return "<h2>About page</h2>"

@app.route("/contact/<name>/<name1>")

def contact(name,name1):
    return f"Contact page of {name} and {name1}= {name+name1}"

if __name__=='__main__':
  
  app.run(host='0.0.0.0',debug=False)