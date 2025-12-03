import tkinter as tk
from tkinter import messagebox
import joblib
import os
import joblib


# Load model
#model = joblib.load("../models/student_marks_model.pkl")
#model = joblib.load("../models/student_marks_model.pkl".replace("/", "\\"))
#model = joblib.load(os.path.join(os.path.dirname(__file__), "..", "models", "student_marks_model.pkl"))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "student_marks_model.pkl")

model = joblib.load(MODEL_PATH)


root = tk.Tk()
root.title("Marks Predictor")

labels = ["Study Hours", "Sleep Hours", "Attendance", "Extra Curricular Hours", "Revision Hours"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

def predict_marks():
    inputs = [[float(entry.get()) for entry in entries]]
    prediction = model.predict(inputs)[0]
    messagebox.showinfo("Predicted Marks", f"Marks: {prediction:.2f}")

tk.Button(root, text="Predict", command=predict_marks).grid(row=len(labels), column=0, columnspan=2)
root.mainloop()
