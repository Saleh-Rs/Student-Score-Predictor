# 🎓 Student Score Predictor

A simple Machine Learning desktop application that predicts a student's expected score based on the number of hours they study.

The project uses Simple Linear Regression to learn the relationship between study hours and student scores, then provides a graphical prediction interface built with Tkinter.

---

## ✨ Features

- 📊 Student Score Prediction
  
  - Enter the number of study hours and get the predicted score.
  - The prediction is generated using a trained Linear Regression model.

- 🤖 Simple Linear Regression
  
  - Uses "LinearRegression" from Scikit-learn.
  - The model is trained using sample study-hours and score data.

- 📈 Data Visualization
  
  - Displays the actual data points.
  - Draws the Linear Regression line (Best Fit Line).
  - Shows the relationship between study hours and scores.

- 📉 Model Evaluation
  
  - Calculates and displays:
    - MAE — Mean Absolute Error
    - MSE — Mean Squared Error
    - RMSE — Root Mean Squared Error
    - R² — R-squared

- 🖥️ Graphical User Interface
  
  - Built with Tkinter.
  - Prediction and graph visualization are integrated into the same desktop application.

- ⚠️ Input Validation
  
  - Prevents negative study hours.
  - Handles invalid/non-numeric input.

---

## 📸 Preview

<p align="center">
<img src="images/preview.png"width="600">
</p>



## 🧠 How It Works

The application uses a small dataset containing:

- X: Study hours
- Y: Student score

The Linear Regression model is trained using this data:

x = [1, 2, 3, ..., 10]
y = [7, 9, 10, ..., 20]

The model learns the relationship between study time and score:

Study Hours → Linear Regression Model → Predicted Score

When the user enters a number of study hours, the trained model predicts the expected score.

---

## 📊 Model Evaluation

The application evaluates the trained model using four common regression metrics:

Metric| Description
MAE| Average absolute difference between actual and predicted values
MSE| Average squared difference between actual and predicted values
RMSE| Square root of MSE
R²| Measures how well the model explains the variation in the target values

These metrics are displayed directly in the application's interface.

---

## 📈 Visualization

By clicking the "نمایش نمودار" button, the application displays a graph containing:

- 🔵 Actual student score data
- 📈 Linear Regression line
- X-axis: Study Hours
- Y-axis: Score
- Grid and legend for easier interpretation

The graph is embedded directly inside the Tkinter interface using Matplotlib.

---

## 🛠️ Technologies Used

- Python
- Tkinter — GUI
- NumPy — Numerical data handling
- Scikit-learn — Machine Learning & model evaluation
- Matplotlib — Data visualization

---

## 📦 Installation

Make sure Python is installed on your system.

Install the required libraries:

pip install numpy scikit-learn matplotlib

Tkinter is included with most standard Python installations on Windows.

---

▶️ Run the Project

Clone the repository:

git clone https://github.com/Saleh-Rs/Student-Score-Predictor.git

Navigate to the project directory:

cd student-score-predictor

Run the application:

python main.py

---

🖥️ Application Workflow

1. Enter the number of hours studied.
2. Click "پیش بینی نمره".
3. The model calculates the predicted score.
4. Click "نمایش نمودار" to visualize the actual data and regression line.
5. Review the model evaluation metrics displayed in the application.

---

📁 Project Structure

Student-Score-Predictor/
│
├── main.py
└── README.md

---

🎯 Project Goal

The main goal of this project is to build a simple and practical Machine Learning application while understanding the basic workflow of a regression problem:

Data → Model Training → Prediction → Evaluation → Visualization

This project is designed as a beginner-friendly introduction to applying Machine Learning models inside a Python desktop application.

# 👨‍💻 Author

Saleh.Rs
