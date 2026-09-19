import streamlit as st
import pandas as pd
import joblib
# Dark theme
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
        color: white;
    }

    h1, h2, h3 {
        color: white;
    }

    .stTextInput label,
    .stNumberInput label,
    .stSelectbox label {
        color: white !important;
    }

    .stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 25px;
        font-size: 16px;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Load the trained model
model = joblib.load("student_performance_model.pkl")

# Page title
st.title("🎓 AI Study Performance Predictor")

st.write("Enter the student's details to predict the Final Grade.")

# User inputs
StudyHours = st.number_input("Study Hours", min_value=0.0, max_value=24.0, value=5.0)

Attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=75.0)

Resources = st.selectbox("Resources", [0, 1])

Extracurricular = st.selectbox("Extracurricular", [0, 1])

Motivation = st.selectbox("Motivation", [0, 1, 2, 3, 4, 5])

Internet = st.selectbox("Internet", [0, 1])

Gender = st.selectbox("Gender", [0, 1])

Age = st.number_input("Age", min_value=10, max_value=100, value=20)

LearningStyle = st.selectbox("Learning Style", [0, 1, 2])

OnlineCourses = st.number_input("Online Courses", min_value=0, max_value=20, value=2)

Discussions = st.number_input("Discussions", min_value=0, max_value=20, value=2)

AssignmentCompletion = st.number_input(
    "Assignment Completion (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

EduTech = st.selectbox("EduTech", [0, 1])

StressLevel = st.selectbox("Stress Level", [0, 1, 2, 3, 4, 5])

# Prediction button
if st.button("Predict Performance"):

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "StudyHours": StudyHours,
        "Attendance": Attendance,
        "Resources": Resources,
        "Extracurricular": Extracurricular,
        "Motivation": Motivation,
        "Internet": Internet,
        "Gender": Gender,
        "Age": Age,
        "LearningStyle": LearningStyle,
        "OnlineCourses": OnlineCourses,
        "Discussions": Discussions,
        "AssignmentCompletion": AssignmentCompletion,
        "EduTech": EduTech,
        "StressLevel": StressLevel
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(f"Predicted FinalGrade: {prediction}")