import streamlit as st
import pandas as pd

st.set_page_config(page_title="BMI Calculator", layout="centered")


st.markdown(
    """
    <style>
     /* Style sliders */
        .stSlider {
            background-color: #222 !important; /* Dark background */
            padding: 10px;
            border-radius: 10px;
        }
        /* Style slider labels and numbers */
        div[data-testid="stSlider"] div[role="slider"] {
            background-color: white !important; 
        }
        div[data-testid="stSlider"] span {
            color: white !important; /* White text for better contrast */
            font-weight: bold;
        }

        .big-font { font-size:24px !important; font-weight: bold; color: #4CAF50; }
        .result { font-size:22px !important; font-weight: bold; }
        .underweight { color: #FFA500; } /* Orange */
        .normal { color: #4CAF50; } /* Green */
        .overweight { color: #FF9800; } /* Darker Orange */
        .obese { color: #F44336; } /* Red */
        .stSlider { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMI Calculator</h1>", unsafe_allow_html=True)


height = st.slider('Height in cm', 100, 250, 170)
weight = st.slider('Weight in kg', 30, 200, 70)

# Convert height to feet and inches
height_inches = height / 2.54
feet = int(height_inches // 12)
inches = int(height_inches % 12)

st.markdown(f"<p class='big-font'>Height: {feet} feet {inches} inches</p>", unsafe_allow_html=True)

bmi = weight / (height / 100) ** 2

st.markdown(f"<p class='result'>Your BMI: {bmi:.2f}</p>", unsafe_allow_html=True)

if bmi < 18.5:
    st.markdown("<p class='underweight'><b>You are underweight</b></p>", unsafe_allow_html=True)
elif bmi < 25:
    st.markdown("<p class='normal'><b>You have a normal weight</b></p>", unsafe_allow_html=True)
elif bmi < 30:
    st.markdown("<p class='overweight'><b>You are overweight</b></p>", unsafe_allow_html=True)
else:
    st.markdown("<p class='obese'><b>You are obese</b></p>", unsafe_allow_html=True)

st.write('BMI Categories:')
st.write('Underweight: <18.5')
st.write('Normal weight: 18.5–24.9')
st.write('Overweight: 25–29.9')
st.write('Obesity: BMI of 30 or greater')