from django.shortcuts import render
from flask import Flask,render_template
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/index")

#‘/’ URL is bound with first_flask function.
def student_webpage():
    name = "Bartosz"
    return render_template("index.html",student_name=name) 
    
#run the application on local server
app.run(debug=True)
