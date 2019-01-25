from flask import Flask, render_template, request
from apis_testing_flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"] )
def generate():
    form_data = request.form
    user_animal = form_data["animal"]
    user_number = form_data["number"]
    extraValue = choose_extra_value()
    protagonist = generate_user(extraValue)
    advice = generate_advice()
    smallInt = no_of_pets(protagonist)
    fName = first_name(protagonist)
    lName = last_name(protagonist)
    ccity = city(protagonist)
    jjob_title = job_title(protagonist)
    pet = generate_pet(user_animal)
    vvisitor = choose_visitor(user_number)
    return render_template("generate.html", **locals())

if __name__ == "__main__":
    app.run(debug=True)
