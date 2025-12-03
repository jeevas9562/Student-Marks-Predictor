from flask import Flask, render_template, request
import joblib
import os
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

# Get absolute path of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct path to model file
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "student_marks_model.pkl")

# Load the model
model = joblib.load(MODEL_PATH)


#app = Flask(__name__)
#model = joblib.load("../models/student_marks_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", marks=predicted_marks)


@app.route("/", methods=["GET", "POST"])
def home():
    marks = ""
    if request.method == "POST":
        values = [float(request.form[key]) for key in ['study','sleep','attendance','extra','revision']]
        marks = round(model.predict([values])[0], 2)
    return render_template("index.html", marks=marks)

if __name__ == "__main__":
    app.run(debug=True)
