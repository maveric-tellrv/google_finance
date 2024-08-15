# Use a Python base image
FROM python:3.11-slim

# Install Chrome browser
RUN apt-get update && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable

# Install the ChromeDriver
RUN apt-get install -yqq unzip \
    && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the Selenium test script into the container
COPY googleFinancePage.py /app/googleFinancePage.py && 
COPY test_googleFinancePage.py /app/test_googleFinancePage.py

# Set the working directory
WORKDIR /app

# Run the test script
CMD ["python", "test_googleFinancePage.py"]

