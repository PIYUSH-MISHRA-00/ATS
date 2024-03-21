# Use Python 3.10 slim-buster base image
FROM python:3.10-slim-buster

# Set working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ghostscript python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --no-cache-dir -r requirements.txt

# Expose port 8501 to the outside world
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "ATS.py"]
