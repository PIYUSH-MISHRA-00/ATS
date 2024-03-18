# Use official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/scripts:${PATH}"

# Set working directory in the container
WORKDIR /app

# Copy only the necessary files to the container
COPY requirements.txt /app/requirements.txt
COPY ATS.py /app/ATS.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port where Streamlit will run
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "ATS.py"]
