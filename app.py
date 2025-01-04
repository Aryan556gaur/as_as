import streamlit as st
from prompts import generate_tech_questions

def main():
    st.title("TalentScout Hiring Assistant")

    # Collect candidate details
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    
    with open('interviewers.txt', 'a') as f:
        f.write(f"name: {name}, email: {email}, phone: {phone}, experience: {experience}, position: {position}, location: {location} \n")

    tech_stack = st.text_area("Enter your Tech Stack (e.g., Python, Django, PostgreSQL)")

    if st.button("Generate Questions"):
        if tech_stack:
            questions = generate_tech_questions(tech_stack)
            st.write(f"{questions}")
        else:
            st.warning("Please enter a tech stack.")

if __name__ == "__main__":
    main()