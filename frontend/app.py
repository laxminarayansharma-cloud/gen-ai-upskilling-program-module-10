import streamlit as st
import requests

st.title("Calculator App With Streamlit depoyment")

number = st.number_input("Enter a number:", value=2)
# this is for external api calls
# if st.button("Calculate Square"):
#     response = requests.get(f"http://backend:8000/square/{number}")
#     data = response.json()
#     st.write(f"The square of {number} is {data['square']}")
if st.button("Calculate Square"):
    st.write(f"The square of {number} is {number**2}")

#for creating docker run steps
# cd frontend
# docker build -t streamlit-app .
# docker run -d -p 8501:8501 streamlit-app
# Visit http://localhost:8501

