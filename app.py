from flask import Flask, render_template, request
import apis_testing_flask as atf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    return render_template("generate.html", advice=atf.advice, smallInt=atf.smallInt, fName=atf.fName, lName=atf.lName, city=atf.city, job_title=atf.job_title)

if __name__ == "__main__":
    app.run(debug=True)
