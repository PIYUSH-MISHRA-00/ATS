![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
# ATS (Applicant Tracking System)

ATS is a resume parser and Applicant Tracker System designed for checking and scoring resumes against job requirements. It streamlines the recruitment process by automating the initial screening of resumes and evaluating candidates based on specified criteria.

## Features

- **Resume Parsing:** Parses resumes uploaded in PDF format to extract relevant information such as skills, experience, and education.
- **Requirement Matching:** Matches parsed resume data with job requirements to determine candidate suitability.
- **Scoring System:** Calculates a score for each candidate based on the degree of match between their resume and the job requirements.
- **User-Friendly Interface:** Provides an intuitive interface for uploading resumes, entering job requirements, and viewing scores.

## Installation

To use ATS, follow these steps:

1. Clone this repository to your local machine:

```
git clone https://github.com/your_username/ATS.git
```

Navigate to the project directory:
```
cd ATS
```

Install the required dependencies:

```
pip install -r requirements.txt
```

# Usage

Run the ATS application:
```
streamlit run ATS.py
```

Upload resumes in PDF format and enter job requirements using the provided interface.
Click the "Calculate Score" button to evaluate candidates against the job requirements.
View the calculated scores and make informed decisions about candidate suitability.

# Link to Docker Image
[Link to Docker Image](https://hub.docker.com/r/piyushmishradocker/ats)
