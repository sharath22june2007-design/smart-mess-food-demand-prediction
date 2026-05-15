# Step 1: Import libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Step 2: Load dataset (Google Colab upload)
from google.colab import files
import io
uploaded = files.upload()
df = pd.read_csv(io.BytesIO(list(uploaded.values())[0]))
print("Dataset shape:", df.shape)
print(df.head())

# Step 3: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Label Encoding (convert text to numbers)
le_day     = LabelEncoder()
le_weather = LabelEncoder()
le_menu    = LabelEncoder()
le_holiday = LabelEncoder()
le_exam    = LabelEncoder()

df['day']     = le_day.fit_transform(df['day'])
df['weather'] = le_weather.fit_transform(df['weather'])
df['menu']    = le_menu.fit_transform(df['menu'])
df['holiday'] = le_holiday.fit_transform(df['holiday'])
df['exam']    = le_exam.fit_transform(df['exam'])

print("\nEncoded Dataset:")
print(df.head())

# Step 5: Split features and target
X = df.drop('students_count', axis=1)
y = df['students_count']

# Step 6: Train test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTrain size:", X_train.shape[0], "| Test size:", X_test.shape[0])

# Step 7: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained")

# Step 8: Evaluate the model
y_pred = model.predict(X_test)
print("\nMAE:     ", round(mean_absolute_error(y_test, y_pred), 2))
print("R2 Score:", round(r2_score(y_test, y_pred), 4))

# Step 9: Plot Actual vs Predicted
plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred, color='steelblue', edgecolors='black', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Students')
plt.ylabel('Predicted Students')
plt.title('Actual vs Predicted Student Count')
plt.savefig('output.png', dpi=150)
plt.show()

# Step 10: Manual user input prediction
print("\n========== MANUAL PREDICTION ==========")
print("Available Days:    ", list(le_day.classes_))
print("Available Weather: ", list(le_weather.classes_))
print("Available Menu:    ", list(le_menu.classes_))
print("Holiday options:   ", list(le_holiday.classes_))
print("Exam options:      ", list(le_exam.classes_))

day     = input("\nEnter day: ")
weather = input("Enter weather: ")
menu    = input("Enter menu type: ")
holiday = input("Holiday? (Yes/No): ")
exam    = input("Exam? (Yes/No): ")

day_val     = le_day.transform([day])[0]
weather_val = le_weather.transform([weather])[0]
menu_val    = le_menu.transform([menu])[0]
holiday_val = le_holiday.transform([holiday])[0]
exam_val    = le_exam.transform([exam])[0]

prediction = model.predict([[day_val, weather_val, menu_val, holiday_val, exam_val]])

print("\n========== RESULT ==========")
print("Predicted Students Count:", round(prediction[0]))