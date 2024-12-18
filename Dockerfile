# Use Python 3.12 as I have that version of Python locally
FROM python:3.12-slim

# Don't write .pyc files on disk
ENV PYTHONDONTWRITEBYTECODE=1

# Real time output
ENV PYTHONUNBUFFERED=1

# Use standard folder
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Open port 8000
EXPOSE 8000

# Start the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
