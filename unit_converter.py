import streamlit as st

# Custom CSS for gradient theme and modern styling
st.markdown(
    """
    <style>
    /* Main container styling with gradient background */
    .stApp {
        background: linear-gradient(135deg, #1e1e1e, #2c3e50); /* Dark gradient */
        color: #ffffff; /* White text */
        font-family: 'Arial', sans-serif;
    }

    /* Title styling */
    .stMarkdown h1 {
        color: #3498db; /* Blue for titles */
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 20px;
        font-weight: bold;
    }

    /* Subtitle styling */
    .stMarkdown h2 {
        color: #3498db; /* Blue for subtitles */
        font-size: 2rem;
        margin-bottom: 15px;
        font-weight: 600;
    }

    /* Button styling */
    .stButton button {
        background-color: #3498db; /* Blue buttons */
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
        border: none;
    }
    .stButton button:hover {
        background-color: #2980b9; /* Darker blue on hover */
        transform: scale(1.05);
    }

    /* Input field styling */
    .stTextInput input {
        border-radius: 8px;
        padding: 10px;
        border: 2px solid #444; /* Dark border */
        background-color: #34495e; /* Dark background */
        color: #ffffff; /* White text */
        transition: border-color 0.3s ease;
    }
    .stTextInput input:focus {
        border-color: #3498db; /* Blue border on focus */
        outline: none;
    }

    /* Dropdown styling */
    .stSelectbox div {
        border-radius: 8px;
        padding: 2px;
        border: 2px ; /* Dark border */
        background-color: #34495e; /* Dark background */
        color: #ffffff; /* White text */
        transition: border-color 0.3s ease;
    }
    .stSelectbox div:hover {
        border-color: #3498db; /* Blue border on hover */
    }

    /* Success message styling */
    .stSuccess {
        border-radius: 8px;
        padding: 15px;
        background-color: #27ae60; /* Green background */
        color: #ffffff; /* White text */
        border: 2px solid #2ecc71; /* Green border */
        font-weight: bold;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #2c3e50; /* Dark sidebar */
        color: white;
    }
    .css-1d391kg h1 {
        color: white;
    }
    .css-1d391kg .stSelectbox div {
        background-color: #34495e; /* Darker background for dropdowns */
        color: white; /* White text */
    }
    .css-1d391kg .stSelectbox div:hover {
        background-color: #3b536b; /* Slightly lighter on hover */
    }

    /* Dropdown options styling */
    .stSelectbox option {
        background-color: #2c3e50; /* Dark background for options */
        color: white; /* White text for options */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.markdown("<h1>Advanced Unit Converter App</h1>", unsafe_allow_html=True)

# Sidebar for category selection
st.sidebar.markdown("<h2>Select Category</h2>", unsafe_allow_html=True)
category = st.sidebar.radio("", ["Length", "Temperature", "Time"])

# Function for length conversion
def convert_length(value, input_unit, output_unit):
    conversion_factors = {
        "Meters": 1,
        "Feet": 3.28084,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
    }
    return value * (conversion_factors[output_unit] / conversion_factors[input_unit])

# Function for temperature conversion
def convert_temperature(value, input_unit, output_unit):
    if input_unit == "Celsius" and output_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif input_unit == "Fahrenheit" and output_unit == "Celsius":
        return (value - 32) * 5/9
    else:
        return value  # No conversion needed if units are the same

# Function for time conversion
def convert_time(value, input_unit, output_unit):
    conversion_factors = {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days": 86400,
    }
    return value * (conversion_factors[input_unit] / conversion_factors[output_unit])

# Main app logic
if category == "Length":
    st.markdown("<h2>Length Converter</h2>", unsafe_allow_html=True)
    length_units = ["Meters", "Feet", "Kilometers", "Miles"]
    input_value = st.number_input("Enter Value", min_value=0.0, format="%.2f", key="length_input")
    input_unit = st.selectbox("From", length_units, key="length_from")
    output_unit = st.selectbox("To", length_units, key="length_to")
    if st.button("Convert", key="length_convert"):
        result = convert_length(input_value, input_unit, output_unit)
        st.success(f"Converted Value: {result:.2f} {output_unit}")

elif category == "Temperature":
    st.markdown("<h2>Temperature Converter</h2>", unsafe_allow_html=True)
    temperature_units = ["Celsius", "Fahrenheit"]
    input_value = st.number_input("Enter Value", format="%.2f", key="temp_input")
    input_unit = st.selectbox("From", temperature_units, key="temp_from")
    output_unit = st.selectbox("To", temperature_units, key="temp_to")
    if st.button("Convert", key="temp_convert"):
        result = convert_temperature(input_value, input_unit, output_unit)
        st.success(f"Converted Value: {result:.2f} {output_unit}")

elif category == "Time":
    st.markdown("<h2>Time Converter</h2>", unsafe_allow_html=True)
    time_units = ["Seconds", "Minutes", "Hours", "Days"]
    input_value = st.number_input("Enter Value", min_value=0.0, format="%.2f", key="time_input")
    input_unit = st.selectbox("From", time_units, key="time_from")
    output_unit = st.selectbox("To", time_units, key="time_to")
    if st.button("Convert", key="time_convert"):
        result = convert_time(input_value, input_unit, output_unit)
        st.success(f"Converted Value: {result:.2f} {output_unit}")