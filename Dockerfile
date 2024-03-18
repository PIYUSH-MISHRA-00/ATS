FROM python:3.12

WORKDIR /app

# Copy the entire application directory into the container
COPY . .


# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose port 80 for Streamlit app
EXPOSE 80

# Create Streamlit configuration directory and copy configuration files
RUN mkdir -p ~/.streamlit && \
    cp config.toml ~/.streamlit/config.toml && \
    cp credentials.toml ~/.streamlit/credentials.toml

# Set the entrypoint and default command to run the Streamlit app
ENTRYPOINT ["streamlit", "run"]
CMD ["ATS.py", "--server.enableCORS=false", "--server.enableWebsocketCompression=false", "--server.enableXsrfProtection=false"]
