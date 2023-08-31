import streamlit as st

# Title
st.title('Find the Largest Number')

# Description
st.write("This Streamlit app finds the largest number among the three numbers you input.")

# Getting input numbers from user
num1 = st.number_input("Enter the first number:", format="%f")
num2 = st.number_input("Enter the second number:", format="%f")
num3 = st.number_input("Enter the third number:", format="%f")

# Calculate the largest number
largest_num = max(num1, num2, num3)

# Display the largest number
st.write(f"The largest number among {num1}, {num2}, and {num3} is {largest_num}.")
streamlit run find_largest_number.py
