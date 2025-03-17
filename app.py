import streamlit as st
from chatbot_logic import generate_questions_llm, greet_user, handle_fallback, end_conversation
from data_handler import save_candidate_data
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

st.set_page_config(page_title="TalentScout - Hiring Assistant", layout="centered")
st.title("💼 TalentScout - Hiring Assistant")

st.info("🔐 This application uses simulated/anonymized data. All candidate information is handled in compliance with data privacy best practices (e.g., GDPR).")

# Greeting
st.markdown(greet_user())

# Candidate Form
with st.form("candidate_form"):
    candidate_name = st.text_input("Full Name (Anonymized or Simulated)")
    candidate_email = st.text_input("Email Address (Anonymized or Simulated)")
    phone = st.text_input("Phone Number")
    experience = st.text_input("Years of Experience")
    desired_position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_input("Tech Stack (Languages, Frameworks, Databases, Tools)")
    consent = st.checkbox("I agree to the data processing and privacy terms.")
    submitted = st.form_submit_button("Generate Questions")

# Process Form Submission
if submitted:
    if not consent:
        st.warning("❗ You must provide consent to proceed.")
    elif tech_stack:
        candidate_info = {
            "Name": candidate_name,
            "Email": candidate_email,
            "Phone": phone,
            "Experience": experience,
            "Desired Position": desired_position,
            "Location": location,
            "Tech Stack": tech_stack,
        }
        save_candidate_data(candidate_info)

        st.subheader("📋 Technical Questions")
        try:
            st.success("✅ Candidate Info Recorded. Generating Technical Questions...")
            questions = generate_questions_llm(tech_stack)
            st.write(questions)
            st.markdown("---")
            st.success(end_conversation())
        except Exception as e:
            st.error(handle_fallback(str(e)))
    else:
        st.warning("❗ Please enter a tech stack.")