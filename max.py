import streamlit as st

st.title("Find the Largest of 3 Numbers")

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

largest_number = max(a, b, c)

st.write("The largest number is:", largest_number)