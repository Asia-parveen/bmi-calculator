
import streamlit as st
import re  # Regular expressions for validation

# Set page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional and attractive styling
st.markdown("""
    <style>
    /* General Styling */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f5f5;
    }
    h1 {
        color: #2c3e50;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 20px;
    }
    h2 {
        color: #34495e;
        font-size: 1.8rem;
        text-align: center;
        margin-bottom: 15px;
    }
    p {
        color: #7f8c8d;
        font-size: 1rem;
        text-align: center;
    }

    /* Input Fields */
    .stNumberInput>div>div>input {
        border: 2px solid #3498db;
        border-radius: 10px;
        padding: 12px;
        font-size: 1rem;
        color: #2c3e50;
    }
    .stNumberInput>label {
        font-size: 1.1rem;
        color: #34495e;
        font-weight: bold;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #3498db; /* Blue background */
        color: #ffffff; /* White text color */
        padding: 12px 24px;
        border-radius: 10px;
        border: none;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease; /* Smooth transition for all properties */
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #2980b9; /* Darker blue on hover */
        color: #ffffff; /* White text color on hover */
        transform: scale(1.05); /* Slightly increase size on hover */
    }

    /* Result Styling */
    .stSuccess {
        background-color: #d5f5e3;
        color: #27ae60;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        margin-top: 20px;
    }
    .stWarning {
        background-color: #fcf3cf;
        color: #f39c12;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        margin-top: 20px;
    }
    .stError {
        background-color: #fadbd8;
        color: #e74c3c;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        margin-top: 20px;
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        margin-top: 30px;
        padding: 15px;
        background-color: #2c3e50;
        color: white;
        border-radius: 10px;
        font-size: 1rem;
    }
    .footer a {
        color: #3498db;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🧮 BMI Calculator")
st.markdown("Calculate your Body Mass Index (BMI) to assess your health status.")

# Input field for user's name
user_name = st.text_input("Enter your name:")

# Validate name input
if user_name:
    if not re.match("^[A-Za-z ]+$", user_name):  # Only alphabets and spaces allowed
        st.error("Invalid name! Please enter only letters and spaces.")

# Input fields for weight and height
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight (kg):", min_value=0.0, max_value=300.0, value=70.0, step=0.1)
with col2:
    height = st.number_input("Enter your height (cm):", min_value=0.0, max_value=300.0, value=170.0, step=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    if not user_name or not re.match("^[A-Za-z ]+$", user_name):  # Validate name again
        st.error("Please enter a valid name before calculating BMI.")
    elif height == 0:
        st.error("Height cannot be zero. Please enter a valid height.")
    else:
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        st.success(f"Your BMI is **{bmi:.2f}**")

        # BMI Categories
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    © 2025 BMI Calculator | Developed with ❤️ by <a href="https://next-js-portfolio-web-6ttt.vercel.app/" target="_blank"> Asia Parveen</a>
</div>
""", unsafe_allow_html=True)



