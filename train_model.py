import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/student_performance.csv", sep="\t")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Show number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Show column names
print("\nColumn names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())
print("\nFinalGrade values:")
print(df["FinalGrade"].value_counts().sort_index())
print("\nFinalGrade data type:")
print(df["FinalGrade"].dtype)
# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Select input features
X = df.drop(["FinalGrade", "ExamScore"], axis=1)

# Select target
y = df["FinalGrade"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)
# Feature importance
print("\nFeature Importance:")

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print(importance)
from sklearn.metrics import classification_report, confusion_matrix

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
import joblib

# Save the trained model
joblib.dump(model, "student_performance_model.pkl")

print("\nModel saved successfully!")