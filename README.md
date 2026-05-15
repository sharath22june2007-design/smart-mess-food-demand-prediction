# Smart Mess Food Demand Prediction

A Machine Learning project that predicts the number of students who will opt for meals each day in a college mess, helping reduce food wastage and optimize resource planning.

---

# Problem Statement

A college mess faces issues like food wastage or food shortage due to unpredictable student attendance. This project builds a regression model to forecast daily meal demand based on factors like day, weather, menu type, holidays, and exam schedules.

---

# Dataset

| Column         | Description                                              |
| -------------- | -------------------------------------------------------- |
| day            | Day of the week (Mon to Sun)                             |
| weather        | Weather condition (Sunny, Cloudy, Rainy)                 |
| menu           | Menu type (Regular, Special)                             |
| holiday        | Whether it is a holiday (Yes, No)                        |
| exam           | Whether exams are scheduled (Yes, No)                    |
| students_count | Number of students who opted for meals (Target Variable) |

### Dataset Information

* Total Records: 126
* No Missing Values

---

# Project Workflow

1. Import required libraries
2. Upload and load dataset
3. Check missing values
4. Apply Label Encoding
5. Split dataset into training and testing data
6. Train Linear Regression model
7. Evaluate model performance
8. Predict student attendance
9. Visualize results using graphs

---

# Data Preprocessing

Categorical text values such as:

* Mon
* Sunny
* Special
* Yes/No

were converted into numerical values using Label Encoding because Machine Learning models require numerical input.

---

# Train-Test Split

The dataset was divided into:

* 80% Training Data
* 20% Testing Data

Training data is used to teach the model, while testing data is used to evaluate prediction performance on unseen data.

---

# Algorithm Used

## Linear Regression

Linear Regression is used because the target variable (`students_count`) is numerical and continuous.

The model learns the relationship between:

* Day
* Weather
* Menu Type
* Holidays
* Exams

and predicts the estimated number of students attending the mess.

---

# Libraries Used

* pandas
* scikit-learn
* matplotlib

---

# Evaluation Metrics

## Mean Absolute Error (MAE)

MAE measures the average prediction error of the model.

Lower MAE indicates better prediction performance.

---

## R² Score

R² Score measures how well the model explains the relationship between input features and target output.

A value closer to 1 indicates better model performance.

---

# Results

* The model successfully predicts daily student attendance based on given conditions.
* Actual vs Predicted graph visually shows prediction performance.
* MAE and R² Score are displayed after evaluation.

---

# Output Screenshots



![Prediction](output_screenshot.png)



![Graph](graph__screenshot.png)

---



---

# Example Prediction

### Input

* Day: Friday
* Weather: Sunny
* Menu: Special
* Holiday: No
* Exam: No

### Output

* Predicted Students Count: 245

---

# How to Run the Project

1. Open Google Colab
2. Create a new notebook
3. Paste the project code
4. Run the notebook
5. Upload the dataset CSV file when prompted
6. Enter manual input values
7. View prediction result and graph output

---


# Future Improvements

* Use larger real-world datasets
* Build web-based interface
* Add advanced Machine Learning algorithms
* Improve prediction accuracy

---

# Team Details



Department: Computer Science / IT

Sharath T

Sharan H.S

Prajwal S.M

Rohith N.V

Subject: ETC515O - Introduction to AI and Its Applications

---

# Conclusion

This project successfully demonstrates the use of Machine Learning for predicting college mess food demand. The system helps estimate student attendance based on multiple daily conditions and can help reduce food wastage and improve mess planning efficiency.

