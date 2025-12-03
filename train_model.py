import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

df=pd.read_csv("data/student_scores.csv")

# Features & target
X = df[['StudyHours','SleepHours','Attendance','Extra_Curricular_Hours','Revision_Hours']]
y = df['Marks']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Save model
joblib.dump(model, "models/student_marks_model.pkl")
print("Model saved in 'models/student_marks_model.pkl'")