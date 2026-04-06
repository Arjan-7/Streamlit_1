import streamlit as st

st.title("Simple Feedback Form")

with st.form("feedback_form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age", min_value=10, max_value=100, step=1)
    favorite_subject = st.selectbox("Favorite subject", ["Math", "Physics", "CS", "Other"])
    feedback = st.text_area("Any feedback")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Thanks, {name}! Your response is recorded.")
    st.write("Summary:")
    st.write({"age": age, "favorite_subject": favorite_subject, "feedback": feedback})