# backend/Dockerfile
FROM python:3.9

WORKDIR /app

# Copying requirements file and installing dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copying all files
COPY . .

# Exposing port 5000
EXPOSE 5000

# Command to run Flask application
CMD ["python", "app.py"]
