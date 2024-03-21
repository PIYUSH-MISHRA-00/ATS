import streamlit as st
import PyPDF2
import re

class ApplicantTrackingSystem:
    def __init__(self):
        self.resume_text = None

    def upload_resume(self):
        uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
        if uploaded_file is not None:
            try:
                # Read the uploaded PDF file as binary data
                pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
                text = ""
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    text += page.extractText()
                self.resume_text = text
            except Exception as e:
                st.error(f"Error reading resume: {str(e)}")
                self.resume_text = None

    def calculate_score(self, requirements):
        if self.resume_text:
            # Perform matching logic between resume text and job requirements
            score = self.match_requirements(self.resume_text, requirements)
            st.success(f"Score: {score}/100")
        else:
            st.warning("No resume uploaded or reading error occurred.")

    def match_requirements(self, resume_text, requirements):
        # Clean the resume text and job requirements
        resume_text = self.clean_text(resume_text)
        requirements = self.clean_text(requirements)
        
        # Split the job requirements into words
        requirement_words = set(requirements.split())

        # Count the total number of matched words
        total_matched_words = sum(1 for word in requirement_words if word in resume_text)

        # Calculate the score based on the ratio of matched words to total words in the requirements
        total_words_in_requirements = len(requirements.split())
        score = round((total_matched_words / total_words_in_requirements) * 100)

        return score

    def clean_text(self, text):
        # Remove special characters, punctuation, and extra whitespaces
        text = re.sub(r'\W+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

# Instantiate the ApplicantTrackingSystem class
ats = ApplicantTrackingSystem()

# Streamlit app layout
st.title("Applicant Tracking System")
st.sidebar.title("Options")

# Sidebar widgets
with st.sidebar:
    ats.upload_resume()

# Main content
st.header("Enter Job Requirements:")
requirements = st.text_area("Enter job requirements here", height=200)

if st.button("Calculate Score"):
    ats.calculate_score(requirements)

st.sidebar.text("By: PIYUSH-MISHRA-00")
